import Functions
import pandas as pd
import os

# Obtener listas con los ya traducidos
traducidos = []
Functions.explorar("../../Rinnes_Utopia_files/Traducidos", traducidos)

Dir_1 = [i for i in os.listdir(path="../../Rinnes_Utopia_files/Originales/1st") if i not in traducidos] #217 total
Dir_2 = [i for i in os.listdir(path="../../Rinnes_Utopia_files/Originales/2nd") if i not in traducidos] #252 total
Dir_3 = [i for i in os.listdir(path="../../Rinnes_Utopia_files/Originales/3rd") if i not in traducidos] #62 total

if __name__ == "__main__":
    # cant_arch = int(input("Cuantos archivos deseas traducir? : "),)
    # Dir = int(input("De que directorio deseas traducir? : "),)

    # if (Dir == 1):
    #     for i in range(0,cant_arch):
            
    