# Aplicacion Encuestas
Pequeña aplicación web que permite crear y votar encuestas.

La aplicación web ha sido creada usando el tutorial de [Django](https://docs.djangoproject.com/en/1.8/intro/tutorial01/) para la asignatura infraestructura virtual

##Uso

Para ejecutar la aplicación una vez descargada hay que usar `python manage.py runserver`

Una vez levantada podemos gestionar las encuestas escribiendo `http://127.0.0.1:8000/admin/` en nuestro navegador

El usuario es `admin` y la contraseña `hola`

![admin](http://i1045.photobucket.com/albums/b460/Alejandro_Casado/pollaplication/admin_zps4vvtzbcr.png)


Para crear y borrar encuestas vamos a `http://127.0.0.1:8000/createpoll/` y `http://127.0.0.1:8000/deletepoll/` respectivamente
Para votar encuestas vamos a `http://127.0.0.1:8000` donde nos aparecerán todas las que hayamos creado

![cuestiones](http://i1045.photobucket.com/albums/b460/Alejandro_Casado/pollaplication/cuestiones_zpsixvqb8yb.png)

Seleccionamos una y nos mostrará las opciones posibles

![opciones](http://i1045.photobucket.com/albums/b460/Alejandro_Casado/pollaplication/cuestion1_zpskbbylwgw.png)

Tras esto, se almacenará nuestro voto

![resultados](http://i1045.photobucket.com/albums/b460/Alejandro_Casado/pollaplication/resultado_zpsnyo2sp0p.png)


**[Licencia](https://github.com/acasadoquijada/pollaplication/blob/master/README.md)**
