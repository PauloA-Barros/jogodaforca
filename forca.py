# Jogo da forca
# Declaração de variáveis
from palavraforca import palavra
palavra = palavra()
letras_usuário = []
chances = 3
ganhou = False

# Criar a lógica
while True:    
    # Informações para o jogador
    for letra in palavra:
        if letra.lower() in letras_usuário:
            print(letra, end=" ")
        else:
            print("_", end=" ")
    print(f"Você tem {chances} chances.")
    tentativa = input("Escolha uma letra para advinhar:")
    letras_usuário.append(tentativa.lower())
    if tentativa.lower() not in palavra.lower():
        chances -= 1
    
    # Iforma se o jogador acertou ou não
    ganhou = True
    for letra in palavra:
        if letra.lower() not in letras_usuário:
            ganhou = False 

    # Condição de encerramento do jogo
    if chances == 0 or ganhou:
        break    

# Imprime o resultado se ganhou ou perdeu
if ganhou:
    print(f"Parabéns, você ganhou o jogo. A palavra era {palavra}.")
else:
    print(f"Você perdeu. A palavra era {palavra}.")