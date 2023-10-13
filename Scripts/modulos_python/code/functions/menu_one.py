import alredylist
import createDF
import time
import cleartext

def menu_one_main():
    menu1 = """\n
    ###################################################
                Elige carpeta a traducir:
        1. 1st
        2. 2nd
        3. 3rd
    ###################################################
    """
    return menu1

def menu_one_choose(name_arch):

    menu1 = f"""\n
    ###################################################
            Archivo a traducir es {name_arch}
        1. Traducir
        2. Ingresa nombre del archivo
    ###################################################
    """
    return menu1

def menu_asegurar():
    menu1 = f"""\n
                Seguro?
        1. Si
        2. No"""
    return menu1

def trad_existoso(name_arch, tiempo):
    menu1 = f"""\n
    ###################################################
        Archivo {name_arch} traducido con exito!
        En {round(tiempo/60)} minutos!
    ###################################################\n
    """
    return menu1

#aqui si necesito la pos y la carpeta seleccionada
def traducir(tsv_list, pos, select_folder):
    dataframe, nombre_arch = createDF.createdf(tsv_list, pos, select_folder)
    new_df = dataframe.copy()
    text_list = new_df["Key"]

    inicio = time.time()
    text_trad = cleartext.clear_trad(text_list)
    fin = time.time()
    tiempo_transcurrido = fin - inicio

    for i in range(0,len(text_trad)):
        new_df.iloc[i,3] = text_trad[i]

    return new_df, nombre_arch, tiempo_transcurrido
    


#pos y select_folder no los uso pero los necesito para crear una opcion sin errores
def change(tsv_list, pos, select_folder):
    seguro = True
    traducido1, traducido2 , traducido3 = alredylist.traducidos()
    while seguro == True:
        search_name = input("\nNombre del archivo: ")

        if search_name in traducido1 or search_name in traducido2 or search_name in traducido3:
            print("\nArchivo ya traducido")
            continue
        else:
            new_pos = tsv_list.index(search_name)
            print(new_pos)

        print(menu_asegurar())
        aux = int(input("\nElige: "))

        if aux == 1:
            seguro = False
        else:
            continue
    return traducir(tsv_list, new_pos, select_folder)

        


    

def choose(tsv_set, pos, select_folder):
    tsv_list = list(tsv_set)
    select_arch = tsv_list[pos]
    print(menu_one_choose(select_arch))
    opcion = int(input("\nElige: "))

    list_com = [traducir, change]
    menu_com = dict(enumerate(list_com, start=1))

    selected_com = menu_com[opcion]
    return selected_com(tsv_list,pos, select_folder)
        