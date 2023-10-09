# Importar Librerias
import deepl
import pandas as pd

def Traducir(archivo):
    df = pd.read_csv(archivo, delimiter="\t")
    #Crear lista con dialogos
    Dialogos = df['Key']
    #Traducir Dialogos con Deepl
    #!!!!!NO TOCAR!!!!!!
    auth_key = "894818a4-a49a-6b8c-e1c6-8ccd29cbf5b3:fx"
    translator = deepl.Translator(auth_key)
    # Obtener lista con los dialogos
    Dialogos_Traducidos = []

    for i in Dialogos:
        result = translator.translate_text(str(i), target_lang="ES")
        Dialogos_Traducidos.append(result)
        #print(result.text)
    # Agregar dialogos a traducidos
    for i in range(0,len(Dialogos_Traducidos)):
        df.iloc[i,3] = str(Dialogos_Traducidos[i])
    return df
