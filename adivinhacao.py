import random

def jogo_adivinhacao():
    print("Bem-vindo ao Jogo de Adivinhação!")
    print("Estou pensando em um número entre 1 e 100.")
    
    numero_secreto = random.randint(1, 100)
    tentativas = 0
    acertou = False
    
    while not acertou:
        try:
            chute = int(input("Digite seu palpite: "))
            tentativas += 1
            
            if chute < numero_secreto:
                print("Muito baixo!")
            elif chute > numero_secreto:
                print("Muito alto!")
            else:
                print(f"Parabéns! Você acertou o número {numero_secreto} em {tentativas} tentativas.")
                acertou = True
        except ValueError:
            print("Por favor, insira um número válido.")
    
    print("Fim do jogo!")

# Iniciar o jogo
jogo_adivinhacao()
