# Recebendo a entrada como uma linha de texto
texto = input()

# Verificando o comprimento do texto
if len(texto) <= 140:
    print("TWEET")
else:
    print("MUTE")