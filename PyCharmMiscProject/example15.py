def cadastrar():
    print("cadastrando...")

def listar():
    print("listando...")

def sair():
    print("saindo...")

def menu(opcao):
    opcoes = {
        1:cadastrar,
        2:listar,
        3:sair
    }

    funcao = opcoes.get(opcao)

    if funcao:
        funcao()
    else:
        print("Opção inválida!")

op = int(input("Opção desejada (1 - Cadastrar, 2- Listar, 3- Sair"))
menu(op)