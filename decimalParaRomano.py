#Ainda em desenvolvimento...

def conversao(decimal):
   # I = 1
   # V = 5
   # X = 10
   # L = 50
   # C = 100
   # D = 500
   # M = 1000

    romano = decimal
    operador = ""

    operador += (int(romano/1000) * 'M')
    romano = romano - (int((romano/1000))*1000)

    if(romano/1000 >= 0.9 and romano/1000 < 1):
        operador += "CM"
        romano = romano - 900

    elif(romano/500 >= 0.8 and romano/500 < 1):
        operador += "CD"
        romano = romano - 400

    else:
        operador += (int(romano/500) * 'D')
        romano = romano - (int((romano/500))*500)



    if(romano/100 >= 0.9 and romano/100 < 1):
        operador += "XC"
        romano = romano - 90

    else:    
        operador += (int(romano/100) * 'C')
        romano = romano - (int((romano/100))*100)


    if(romano/50 >= 0.8 and romano/50 < 1):
        operador += "XL"
        romano = romano - 40
        
    else:    
        operador += (int(romano/50) * 'L')
        romano = romano - (int((romano/50))*50)

    if(romano/10 >= 0.9 and romano/10 <1):
        operador += "IX"
        romano = romano - 9
     
    else:     
        operador += (int(romano/10) * 'X')
        romano = romano - (int((romano/10))*10)

    if(romano/5 >= 0.8 and romano/5 < 1):
        operador += "IV"
        romano = romano - 4
     
    else:    
        operador += (int(romano/5) * 'V')
        romano = romano - (int((romano/5))*5)

    operador += (int(romano/1) * 'I')
    romano = romano - (int((romano/1))*1)

    print(operador)


def entrada():
    print("Digite um número inteiro positivo dentro do intervalo 0 - 3.999:")
    decimal = int(input())
    if(decimal >=0 and decimal <= 3999):
        conversao(decimal)
    else:
        print("Erro: Tente digitar um número inteiro dentro do intervalo 0 - 3.999\n")
        exit()    

entrada()