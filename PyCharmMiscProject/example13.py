def calculadora(a,b,operacao):
    if operacao == "+":
        return a + b
    elif operacao == "-":
        return a - b
    elif operacao == "*":
        return a * b
    elif operacao == "/":
        return a / b
    else:
        return "Operação inválida!"

print(calculadora(5,10,"+"))
print(calculadora(5,10,"-"))
print(calculadora(5,10,"*"))
print(calculadora(5,10,"/"))
print(calculadora(5,10,"a"))