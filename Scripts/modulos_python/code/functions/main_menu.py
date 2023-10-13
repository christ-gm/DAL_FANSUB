import os
import sys
rutapath = os.getcwd()
sys.path.append(rutapath + "/functions")
import alredylist
import time
import menu_one

def menu():
    options = """
    ----------------------------------------
                    OPCIONES:
    1: Traducir
    2: Faltantes
    3: Traducidos
    4: Salir
    ----------------------------------------"""
    return options
    
    
def one():
    menu1 = menu_one.menu_one_main()
    print(menu1)
    opcion = int(input("\nElige: "))

    lista1, lista2, lista3 = alredylist.faltantes()
    list_miss = [lista1, lista2, lista3]
    menu_miss = dict(enumerate(list_miss, start=1))

    names_list = ['1st', '2nd', '3rd']
    menu_names = dict(enumerate(names_list, start=1))

    if opcion in (1, 2, 3):
        selected_miss = menu_miss[opcion]
        select_folder = menu_names[opcion]

        dataframe, nombre_arch, tiempo_trans = menu_one.choose(selected_miss, 0, select_folder)

    ruta_act = os.getcwd()
    ruta_destino = os.path.abspath(os.path.join(ruta_act,"..",".." , "..", "Rinnes_Utopia_files", "Traducidos", f"{select_folder}"))
    ruta_completa = os.path.abspath(os.path.join(ruta_act,"..",".." , "..", "Rinnes_Utopia_files", "Traducidos", f"{select_folder}", f"{nombre_arch}"))
    if not os.path.exists(ruta_destino):
        os.makedirs(ruta_destino)

    dataframe.to_csv(ruta_completa, sep='\t', index=False)

    print (menu_one.trad_existoso(nombre_arch, tiempo_trans))
    sys.exit()


        


def two():
    lista1, lista2, lista3 = alredylist.faltantes()

    faltantes = f"""
    ###################################################
        Archivos que faltan por traducir 1st: {len(lista1)}
        Archivos que faltan por traducir 2nd: {len(lista2)}
        Archivos que faltan por traducir 3rd: {len(lista3)}
    ###################################################"""
    print(faltantes + "\n")

    

def three():
    menu = """
    ###################################################
        1. Traducidos 1st
        2. Traducidos 2nd
        3. Traducidos 3rd
    ###################################################"""

    print(menu)
    opcion = int(input("\nElige: "))
    
    if opcion in (1, 2, 3):
        comunes1, comunes2, comunes3 = alredylist.traducidos()

        list_com = [comunes1, comunes2, comunes3]
        menu_com = dict(enumerate(list_com, start=1))

        selected_com = menu_com[opcion]
        if not selected_com:
            print("\nNada aún")
        else:
            for name in selected_com:
                print(name)
    else:
        three()
    

def four():
    sys.exit()


def main():
    functions_names = [one, two, three, four]
    menu_items = dict(enumerate(functions_names, start=1))

    while True:
        print(menu())
        try:
            selection = int(input("\nElige: "))
            selected_value =menu_items[selection]
            selected_value()
        except (KeyError, ValueError):
            print(f"\nELIGE UNA OPCION BIEN")
        time.sleep(1)

