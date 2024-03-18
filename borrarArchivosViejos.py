import os
import time
 
def removeFields(path, days=30):
    """
    Funcion para eliminar los archivo mas viejos de una carpeta dada
    @param string path - carpeta donde buscar
    @param int days - numero de dias para eliminar un archivo
    @return int - numero de archivos eliminados
    """
    limit = time.time() - days * 86400
    count = 0
 
    for f in os.listdir(path):
        pathFile=os.path.join(path, f)
        if os.path.isfile(pathFile) and os.stat(pathFile).st_mtime < limit:
            try:
                os.remove(pathFile)
                count+=1
            except:
                pass
    return count


