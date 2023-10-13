import os
ruta_act = os.getcwd()

# Rutas de las dos carpetas que deseas comparar
carpeta1 = os.path.abspath(os.path.join(ruta_act,"..",".." , "..", "Rinnes_Utopia_files", "Originales", "1st"))
carpeta2 = os.path.abspath(os.path.join(ruta_act,"..",".." , "..", "Rinnes_Utopia_files", "Traducidos", "1st"))
carpeta3 = os.path.abspath(os.path.join(ruta_act,"..",".." , "..", "Rinnes_Utopia_files", "Originales", "2nd"))
carpeta4 = os.path.abspath(os.path.join(ruta_act,"..",".." , "..", "Rinnes_Utopia_files", "Traducidos", "2nd"))
carpeta5 = os.path.abspath(os.path.join(ruta_act,"..",".." , "..", "Rinnes_Utopia_files", "Originales", "3rd"))
carpeta6 = os.path.abspath(os.path.join(ruta_act,"..",".." , "..", "Rinnes_Utopia_files", "Traducidos", "3rd"))

# Obtiene la lista de archivos en la primera carpeta
archivos_carpeta1 = os.listdir(carpeta1)
archivos_carpeta2 = os.listdir(carpeta2)
archivos_carpeta3 = os.listdir(carpeta3)
archivos_carpeta4 = os.listdir(carpeta4)
archivos_carpeta5 = os.listdir(carpeta5)
archivos_carpeta6 = os.listdir(carpeta6)

def faltantes():
    # Encuentra los archivos en carpeta1 que no están en carpeta2
    archivos_faltantes_1 = set(archivos_carpeta1) - set(archivos_carpeta2)
    archivos_faltantes_2 = set(archivos_carpeta3) - set(archivos_carpeta4)
    archivos_faltantes_3 = set(archivos_carpeta5) - set(archivos_carpeta6)

    return archivos_faltantes_1, archivos_faltantes_2, archivos_faltantes_3

def traducidos():
    # Encuentra los archivos comunes (mismos nombres en ambas carpetas)
    archivos_comunes_1 = set(archivos_carpeta1).intersection(archivos_carpeta2)
    archivos_comunes_2 = set(archivos_carpeta3).intersection(archivos_carpeta4)
    archivos_comunes_3 = set(archivos_carpeta5).intersection(archivos_carpeta6)

    return archivos_comunes_1, archivos_comunes_2, archivos_comunes_3
