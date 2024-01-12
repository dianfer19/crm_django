from django.db import models


# Create your models here.
class Cargos(models.Model):
    nombre = models.CharField(max_length=50)
    estado = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre
    class Meta:
        verbose_name = 'Cargo'
        verbose_name_plural = 'Cargos'
        db_table = 'crm_cargo'


class Empleado(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    fecha_nacimiento = models.DateField()
    cargo = models.ForeignKey(Cargos,blank=True, null=True, to_field='id', related_name='fk_cargo_empleado',
                              on_delete=models.DO_NOTHING, )
    estado = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Empleado'
        verbose_name_plural = 'Empleados'
        db_table = 'crm_empleado'
