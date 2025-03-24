def entrada_abastecimento(quantidade, distancia):
    for i in range(0,4):
        print("Digite a quantidade de combustível abastecida no posto " + str(i+1) + " em Litros: ") #usei o str(i+1) apenas pra ficar visualmente melhor
        quantidade[i] = float(input())
        print("Digite a distância percorrida com o combustível do posto " + str(i+1) + " em Km: ") #usei o str(i+1) apenas pra ficar visualmente melhor
        distancia[i] = float(input())  

def MENU():
    print("--------------------------------MENU--------------------------------\n1-Média de consumo(Km/L) na semana\n2-Média de consumo(Km/L) no mês\n3-Quantidade total de Km rodados no mês\n4-Quantidade total de combustível consumido no mês\n5-Posto com maior rendimento\n6-Encerrar Programa\nDigite a opção desejada: ")


def media_semanal(quantidade, distancia):
    print("----------------------------MÉDIA SEMANAL---------------------------\n")
    for i in range(0,4):
        print("Semana " + str(i+1) + ": " + str(distancia[i]/quantidade[i]) + " Km/L\n") #usei o str(i+1) apenas pra ficar visualmente melhor

def media_mensal(quantidade, distancia):
    print("----------------------------MÉDIA MENSAL----------------------------\n")
    print("Média mensal: " + str(sum(distancia)/sum(quantidade)) + " Km/L\n")

def total_distancia(distancia):
    print("--------------------------DISTÂNCIA MENSAL--------------------------\n")
    print("Total de " + str(sum(distancia)) + " km rodados no mês.\n")

def total_quantidade(quantidade):
    print("--------------------------QUANTIDADE MENSAL-------------------------\n")
    print("Total de " + str(sum(quantidade)) + " litros abastecidos no mês.\n")    

def melhor_rendimento(quantidade, distancia):
    rendimento_semanal = 0
    postoId = 0
    print("----------------------------MELHOR POSTO----------------------------\n")
    for i in range(0,4):
        if(distancia[i]/quantidade[i] > rendimento_semanal):
            rendimento_semanal = distancia[i]/quantidade[i]
            postoId = i
    print("O posto " + str(postoId + 1) + " apresentou maior rendimento: \n\nMédia Semanal: " + str(rendimento_semanal) + " Km/L\n") #usei o str(postoId + 1) apenas pra ficar visualmente melhor



quantidade = [0]*4
distancia = [0]*4  
entrada_abastecimento(quantidade, distancia) 

while True:
    MENU()
    opcao = int(input())

    if(opcao == 1):
        media_semanal(quantidade, distancia)

    elif(opcao == 2):
        media_mensal(quantidade, distancia)

    elif(opcao == 3):
        total_distancia(distancia)

    elif(opcao == 4):
        total_quantidade(quantidade)

    elif(opcao == 5):
        melhor_rendimento(quantidade, distancia)

    elif(opcao == 6):
        break

    else:
        print("Erro: Opção digitada não existe.\n")
        
