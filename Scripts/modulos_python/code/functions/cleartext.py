import deepl

auth_key = "AQUI VA TU API KEY DE DEEPL"
translator = deepl.Translator(auth_key)

def clear_trad(text_list):
    text_trad = []
    print("\n#############-TRADUCIENDO-#############")
    for text in text_list:
        texto_modificado = text.replace('\n', ' ')
        texto_modificado = texto_modificado.replace('\r', ' ')

        temp_text = translator.translate_text(str(texto_modificado), target_lang="ES")

        print(temp_text)

        text_trad.append(temp_text)
    
    return text_trad