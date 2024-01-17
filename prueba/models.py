import uuid

from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.db import models
from django.template.loader import get_template


# Create your models here.
class Cargos(models.Model):
    nombre = models.CharField(max_length=50)
    estado = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre

    def save(self, *args, **kwargs):
        if self.pk:
            super(Cargos, self).save()
        else:
            super(Cargos, self).save()

    class Meta:
        verbose_name = 'Cargo'
        verbose_name_plural = 'Cargos'
        db_table = 'crm_cargo'


class Empleado(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    fecha_nacimiento = models.DateField()
    cargo = models.ForeignKey(Cargos, blank=True, null=True, to_field='id', related_name='fk_cargo_empleado',
                              on_delete=models.DO_NOTHING, )
    estado = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.nombre} {self.apellido}'

    class Meta:
        verbose_name = 'Empleado'
        verbose_name_plural = 'Empleados'
        db_table = 'crm_empleado'


class Etapas(models.Model):
    nombre = models.CharField(max_length=50)
    estado = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Etapa'
        verbose_name_plural = 'Etapas'
        db_table = 'crm_etapa'


class Clientes(models.Model):
    razon_social = models.CharField(max_length=50)
    ruc = models.CharField(max_length=50)
    mail = models.EmailField()
    direccion = models.CharField(max_length=50)
    estado = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        if self.pk is None:
            super(Clientes, self).save()
            mail = self.mail
            print("Enviar Mail")
            copia = {}
            copia = 'dbajana@codeec.com.ec'
            context = {'usuario': self.razon_social}
            template = get_template('mail/notification.html')
            asunto = "Notificaciones CRM"
            content = template.render(context)
            from_email = settings.EMAIL_HOST_USER
            print(from_email)
            to_email = {mail}
            to_cc = {copia}
            email = EmailMultiAlternatives(
                asunto,
                '',
                from_email,
                to_email,
                cc=to_cc,
            )
            email.attach_alternative(content, 'text/html')
            email.send()
        else:
            super(Clientes, self).save()

    def __str__(self):
        return self.razon_social

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        db_table = 'crm_cliente'


class TipoActividad(models.Model):
    nombre = models.CharField(max_length=50)
    estado = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Tipo de actividad'
        verbose_name_plural = 'Tipo de actividades'
        db_table = 'crm_tipo_actividad'


class PlanActividad(models.Model):
    nombre = models.CharField(max_length=50)
    etapa = models.ForeignKey(Etapas, blank=True, null=True, to_field='id',
                              related_name='fk_etapa_plan',
                              on_delete=models.DO_NOTHING, )
    estado = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Plan Actividad'
        verbose_name_plural = 'Plan Actividades'
        db_table = 'crm_plan_actividad'


class DetallePlanActividad(models.Model):
    notas = [
        ('A', 'Reunión Obligatoria'),
        ('B', 'Reunión Virtual'),
        ('C', 'No necesita Reunión'), ]
    descripcion = models.CharField(max_length=200)
    plan_actividad = models.ForeignKey(PlanActividad, blank=True, null=True, to_field='id',
                                       related_name='fk_plan_detalle',
                                       on_delete=models.DO_NOTHING, )
    tipo_actividad = models.ForeignKey(TipoActividad, blank=True, null=True, to_field='id',
                                       related_name='fk_tipo_actividad_detalle',
                                       on_delete=models.DO_NOTHING, )
    nota = models.CharField(max_length=1, choices=notas)
    estado = models.BooleanField(default=True)

    def __str__(self):
        return self.tipo_actividad.nombre

    class Meta:
        verbose_name = 'Detalle de Plan de Actividad'
        verbose_name_plural = 'Detalle de Plan de Actividades'
        db_table = 'crm_detalle_plan_actividad'


class Oportunidades(models.Model):
    descripcion = models.CharField(max_length=200, blank=False, null=False)
    ingreso_esperado = models.DecimalField(max_digits=10, decimal_places=2, )
    cliente = models.ForeignKey(Clientes, blank=True, null=True, to_field='id',
                                related_name='fk_cliente_oportunidad',
                                on_delete=models.DO_NOTHING, )
    estado = models.BooleanField(default=True)

    def __str__(self):
        return self.cliente.razon_social

    def save(self, *args, **kwargs):
        if self.pk:
            super(Oportunidades, self).save()
        else:
            super(Oportunidades, self).save()
            vo = FlujoCrm()
            vo.oportunidad = self
            vo.estado = True
            vo.save()
            vo_detalle = DetalleFlujoCrm()
            vo_detalle.flujo_crm = vo
            vo_detalle.etapa = Etapas.objects.filter(id=1).first()
            vo_detalle.save()

    class Meta:
        verbose_name = 'Oportunidad'
        verbose_name_plural = 'Oportunidades'
        db_table = 'crm_oportunidad'


class FlujoCrm(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    oportunidad = models.OneToOneField(Oportunidades, blank=False, null=False, to_field='id',
                                       related_name='fk_oprtunidad_flujo',
                                       on_delete=models.DO_NOTHING, )
    estado = models.BooleanField(default=True)

    def __str__(self):
        return self.oportunidad.descripcion

    class Meta:
        verbose_name = 'Flujo CRM'
        verbose_name_plural = 'Flujos CRM'
        db_table = 'crm_flujo'


class DetalleFlujoCrm(models.Model):
    flujo_crm = models.ForeignKey(FlujoCrm, blank=False, null=False, to_field='id',
                                  related_name='fk_plan_detalle_flujo',
                                  on_delete=models.DO_NOTHING, )
    empleado = models.ForeignKey(Empleado, blank=True, null=True, to_field='id',
                                 related_name='fk_empleado_detalle_flujo',
                                 on_delete=models.DO_NOTHING, )
    etapa = models.ForeignKey(Etapas, blank=True, null=True, to_field='id',
                              related_name='fk_etapa_detalle_flujo',
                              on_delete=models.DO_NOTHING, )
    estado = models.BooleanField(default=True)

    def __str__(self):
        return self.etapa.nombre

    class Meta:
        verbose_name = 'Detalle de Flujo'
        verbose_name_plural = 'Detalles de Flujo'
        db_table = 'crm_detalle_flujo'
