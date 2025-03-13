def valida_Idade(idade):
    if(idade < 0 or idade > 120):
        print("A idade digitada não existe.\n")
        exit()

def valida_Sexo(sexo):

    if sexo not in ["Masculino", "Feminino"]:
        print("Sexo inexistente.\nTente (Masculino ou Feminino).\n")
        exit()         

def M_18(idade, sexo):
    if(sexo == "Masculino" and idade < 18):
        print("Masculino, com menos de 18 anos.")
        return True
    return False    

def F_50k40(idade, sexo, salario):
    if(sexo == "Feminino" and idade > 40 and salario > 50000):
        print("Feminino, com salário acima de R$ 50.000,00 e com idade acima de 40 anos.")        
        return True
    return False    

def MF_2030(idade, sexo):
    if((sexo == "Feminino" or sexo == "Masculino") and idade >= 20 and idade <= 30):
        print("Masculino ou feminino e idade entre 20 e 30 anos.")        
        return True
    return False    

def verifica_criterios(idade, sexo, salario):
    if(not M_18(idade, sexo) and  not F_50k40(idade, sexo, salario) and not MF_2030(idade, sexo)):
        print("Não se encaixa em nenhuma das possibilidades do sistema.")




print("Digite sua idade: ")
idade = int(input())
valida_Idade(idade)

print("Digite seu sexo (Masculino ou Feminino): ")
sexo = input()
valida_Sexo(sexo)

print("Digite seu salário: ")
salario = float(input())

print("Pessoa: [Idade: " + str(idade) + " ano(s) -  Sexo: " + str(sexo) + " - Salário: " + str(salario) + "]")

verifica_criterios(idade, sexo, salario)