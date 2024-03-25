# Backup de Argenchemical a Dropbox

Acá dejo una serie de instrucciones que sirven para subir los 2 últimos archivos .zip a Dropbox como Backup

Para esto se tiene que tener en cuenta que se debe tener instalado Dropbox.
Seguir las instrucciones que se muestran en este sitio 
https://www.dropbox.com/install-linux
en la sección que lleva de título **Instalación de Dropbox en un equipo sin periféricos a través de la línea de comandos**

En el código se debe especificar la ruta de origen de los archivos a respaldar y la ruta origen
También se les realiza un cambio de propietario por temas de permisos al momento de subir los archivos a Dropbox.

Ejecutar una variable de entorno venv con python -m venv venv 
Activar la variable de entorno con source venv/bin/activate
Ejecutar pip install -r requirements.txt
Revisar el código para chequar que las rutas sean las correctas
Ejecutar python listarYCopiarDropbox.sh

Fin

