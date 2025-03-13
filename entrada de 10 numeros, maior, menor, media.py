def validar_entrada(vetor):
    for i in range(0,10):
       print("Digite um número inteiro positivo para a[" + str(i) + "]: ")
       vetor[i] = int(input())
       
       if(vetor[i] < 0):
          print("Número negativo digitado.\nTente apenas números positivos.")
          exit()

    
    

a = [0]*10
validar_entrada(a)
print("Menor elemento: " + str(min(a)))
print("Maior elemento: " + str(max(a)))
print("Média dos elementos: " + str(sum(a)/len(a)))