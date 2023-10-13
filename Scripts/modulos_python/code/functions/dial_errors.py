import re

def error_message(df):
    if any((df['Operator'] != 'Message') & (df['Operator'] != 'Choice') & (df['Operator'] != 'MapMarker')):
        return True
    else:
        print("\nNo hay errores de mensajes")

def find_error(df):
    for num in range(len(df['Operator'])):
        if df.loc[num, 'Operator'] != 'Message' and df.loc[num, 'Operator'] != 'Choice' and df.loc[num, 'Operator'] != 'MapMarker':
            print(f"\nerror en la fila {num+1}")
            print(df.iloc[num])

def mess_in_dial(df):
    error = False
    for num in range(len(df['Key'])):
        patron = r'^Message,.*,.*$'

        contenido = df.loc[num, 'Key']
        coincidencia = re.findall(patron, str(contenido), re.MULTILINE)

        if coincidencia:
            print(coincidencia)
            error = True
            print(f"Se encontro un mensaje dentro de la fila: {num+2}")
    if error == False:
        print("No hay ningun mensaje dentro de los dialogos")
        return error
    else:
        return error