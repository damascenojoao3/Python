import random #Para números aleatórios
import os #Para poder limpar a tela 

def limpar_tela():
    os.system('cls') #Limpa a tela

while True: #Loop principal para rodar o jogo
    numero_aleatorio = random.randint(1,15)

    numero_user = int(input("Insira um número entre 1 e 15: "))

    if numero_user == numero_aleatorio:
        print(f"Acertou! Seu número foi {numero_user} e o número gerado foi {numero_aleatorio}.")
    else:
        print(f"Errou... Seu número foi {numero_user} e o número gerado foi {numero_aleatorio}.")

    print("Deseja jogar novamente? Digite '1' ou 'sim' para continuar (ou enter para sair): ")
    continuar = input("").strip().lower()
    limpar_tela() #Tela limpa depois de escolher uma das opções

    if continuar not in ["1", "sim"]:
            print("Obrigado por jogar! Até a próxima.")
            break #Fecha o programa