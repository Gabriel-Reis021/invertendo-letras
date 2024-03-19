def inverter_string(string):
    # Inicializa uma string vazia para armazenar a string invertida
    string_invertida = ""

    # Itera sobre a string de trás para frente
    for i in range(len(string) - 1, -1, -1):
        # Adiciona cada caractere à string invertida
        string_invertida += string[i]

    return string_invertida

# String de exemplo
minha_string = "Hello, world!"

# Chama a função para inverter a string
string_invertida = inverter_string(minha_string)

# Imprime a string original e a string invertida
print("String original:", minha_string)
print("String invertida:", string_invertida)
