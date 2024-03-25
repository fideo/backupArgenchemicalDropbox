import os
import shutil

####### BACKUP PADRONDERIESGO ########

# Directorio de origen y destino
directorio_origen = '/mnt/disco2/home/administrador/respaldos/padronderiesgo/'
directorio_destino = '/home/administrador/Dropbox/backups/padronderiesgo/'

# Obtener la lista de archivos con sus fechas de modificación
archivos = [(nombre, os.path.getmtime(os.path.join(directorio_origen, nombre))) for nombre in os.listdir(directorio_origen) if nombre.endswith('.zip')]

# Ordenar la lista de archivos por fecha de modificación
archivos.sort(key=lambda x: x[1], reverse=True)

# Copiar los dos últimos archivos al directorio de destino
for nombre, _ in archivos[:2]:
    ruta_origen = os.path.join(directorio_origen, nombre)
    ruta_destino = os.path.join(directorio_destino, nombre) 

    shutil.copy(ruta_origen, ruta_destino)
    print(f"Archivo '{nombre}' copiado correctamente.")


########### CAMBIO EL USUARIO A LOS ARCHIVOS ###########

archivos_destino = [(nombre, os.path.getmtime(os.path.join(directorio_destino, nombre))) for nombre in os.listdir(directorio_destino) if nombre.endswith('.zip')]
# Ordenar la lista de archivos por fecha de modificación
archivos.sort(key=lambda x: x[1], reverse=True)

# Cambio los permisos del archivo para poderlo subir a Dropbox
for zip, _ in archivos_destino:
    # Cambiar el propietario del archivo
    os.chown("/home/administrador/Dropbox/backups/padronderiesgo/"+str(zip), 1000, 1000)  # UID y GID del usuario administrador


########### DEJO LOS DOS ARCHIVOS MAS NUEVOS DE LA BASE PADRONDERIESGO ###########
archivos_destino.sort(key=lambda x: x[1], reverse=True)

# Eliminar los archivos más antiguos en el directorio de origen
for nombre, _ in archivos_destino[2:]:
    ruta_archivo = os.path.join(directorio_destino, nombre)
    os.remove(ruta_archivo)
    print(f"Archivo '{nombre}' eliminado correctamente.")
