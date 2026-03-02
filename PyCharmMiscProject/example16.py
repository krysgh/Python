def validarSenha(senha):
    temMaiuscula = any(c.isupper() for c in senha)
    temNumero = any(c.isdigit() for c in senha)
    tamanhoOk = len(senha) >= 8

    if tamanhoOk and temNumero and temMaiuscula:
        return "Senha forte"
    else:
        return "Senha fraca"


print(validarSenha(("paodeqUeijo123")))