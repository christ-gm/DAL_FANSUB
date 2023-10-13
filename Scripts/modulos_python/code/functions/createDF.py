import os
import pandas as pd
import dial_errors
import sys

def createdf(tsv_list, pos, select_folder):
    error_msg = False
    error_dial = False
    nombre_arch = tsv_list[pos]
    ruta_act = os.getcwd()
    ruta_archivo = f'{ruta_act}/archivos/{select_folder}/{nombre_arch}'
    dataframe = pd.read_csv(ruta_archivo, delimiter="\t")
    
    #si falta algun mensaje
    if dial_errors.error_message(dataframe) == True:
        dial_errors.find_error(dataframe)
        error_msg = True
    #si hay mensajes dentro de los dialogos
    error_dial = dial_errors.mess_in_dial(dataframe)

    if error_msg == True:
        sys.exit()
    if error_dial == True:
        sys.exit()


    return dataframe, nombre_arch