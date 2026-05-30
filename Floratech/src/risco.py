def classificar_risco(valor):

    valor = float(valor)

    if valor <= 0.30:
        return "BAIXO"

    elif valor <= 0.60:
        return "MÉDIO"

    elif valor <= 0.80:
        return "ALTO"

    else:
        return "EXTREMO"