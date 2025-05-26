import os  #Biblioteca para limpar a tela
import random  #Biblioteca para números aleatórios

#Função para limpar a tela do terminal (compatível com Windows e Unix/Linux)
def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

print("Bubble Sort")

#Função que implementa o algoritmo de ordenação Bubble Sort
def bubblesort(vetor):
    comparacoes = 0  #Contador de comparações entre elementos
    trocas = 0       #Contador de trocas realizadas
    tam = len(vetor)  #Obtém o tamanho do vetor (não utiliza ELE)

    #Loop externo: controla quantas vezes o vetor será percorrido
    for i in range(tam):
        #Loop interno: percorre os elementos ainda não ordenados
        for j in range(0, tam - i - 1):
            comparacoes += 1  #Conta uma comparação
            #Se o elemento atual for maior que o próximo, troca os dois
            if vetor[j] > vetor[j + 1]:
                vetor[j], vetor[j + 1] = vetor[j + 1], vetor[j]  #Troca de valores
                trocas += 1  #Conta uma troca

    #Exibe o número total de comparações e trocas realizadas
    print(f"Total de comparações: {comparacoes}\nTotal de trocas: {trocas}")

#Função principal que coordena a execução do programa
def main():
    while True:  #Loop para permitir que o usuário repita o processo quantas vezes quiser
        #Gera uma lista com 100 números inteiros aleatórios de 1 a 100
        numeros = [random.randint(1, 100) for _ in range(100)]
        print(f"Vetor desordenado: {numeros}")  #Mostra o vetor antes da ordenação

        bubblesort(numeros)  #Chama a função de ordenação

        print(f"Vetor ordenado com Bubble Sort: {numeros}")  #Mostra o vetor ordenado

        #Pergunta ao usuário se deseja repetir o processo
        continuar = input("Deseja tentar novamente? (s/n ou sim/não)\n").strip().lower()
        if continuar not in ["s", "sim"]:  #Se a resposta não for afirmativa, sai do loop
            break
        limpar_tela()  #Limpa a tela para a próxima execução

#Inicia o programa chamando a função principal
main()
