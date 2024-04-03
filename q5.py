def inverter_string(string):
    # convertendo a string em uma lista de caracteres
    caracteres = list(string)
    print(caracteres)
    
    # obtendo o tamanho da string
    tamanho = len(caracteres)
    
    # invertendo os caracteres usando uma abordagem de troca
    for i in range(tamanho // 2):
        temp = caracteres[i]
        caracteres[i] = caracteres[tamanho - 1 - i]
        caracteres[tamanho - 1 - i] = temp
    
    # convertendo a lista de caracteres de volta para uma string
    string_invertida = ''.join(caracteres)
    
    return string_invertida


string_original = input("Digite uma string para inverter: ")
string_invertida = inverter_string(string_original)
print("String original:", string_original)
print("String invertida:", string_invertida)