def contarVogais(texto):
    vogais = "aeiouAEIOU"
    contador = 0

    for letra in texto :
        if letra in vogais:
            contador += 1
    return contador

frase = input("Digite uma frase:")

print("Quantidade de vogais:", contarVogais((frase)))