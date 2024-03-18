import os
import shutil
from borrarArchivosViejos import removeFields
from dirsync import sync

rutaorigen = "/opt/na/respaldos/"
rutadestino = "/mnt/disco2/home/administrador/respaldos/"

sync(rutaorigen, rutadestino, 'sync')
"""shutil.copytree(rutaorigen, rutadestino)"""

removeFields(rutadestino)
