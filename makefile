info:
	@echo ':::::::::::::::::::::::::::::'
	@echo 'ejecutando archivo makefike'
	@echo 'Archivo para contenedores'
	@echo 'Author Dianfer'
	@echo 'Empresa Dbjsystem'
	@echo ':::::::::::::::::::::::::::::'

mostrar:
	@echo 'Mostrando Contenedores'
	docker ps
mostrar_inactivos:
	@echo 'Mostrando Contenedores'
	docker ps -a

levantar:
	@echo 'Levantando Contenedores'
	docker-compose up -d

bajar:
	@echo 'Bajando Contenedores'
	docker-compose stop $(service)


logs_services:
	@echo 'mostrando logs por servicio'
	docker-compose logs -f $(service)

reiniciar:
	@echo 'Reiniciando contenedores'
	docker-compose restart $(service)