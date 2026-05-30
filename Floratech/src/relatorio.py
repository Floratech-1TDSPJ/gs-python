import os

def gerar_relatorio(cidade, registros):

    if len(registros) == 0:
        print("Sem dados para gerar relatório.")
        return

    total_focos = len(registros)

    soma_risco = 0
    soma_frp = 0
    cont_frp = 0

    for r in registros:
        soma_risco += float(r["risco_fogo"])

        if r["frp"] not in [None, "", " "]:
            soma_frp += float(r["frp"])
            cont_frp += 1

    media_risco = soma_risco / total_focos
    media_frp = soma_frp / cont_frp if cont_frp > 0 else 0

    # 📁 garante pasta relatorios
    pasta = os.path.join(os.path.dirname(__file__), "..", "relatorios")
    os.makedirs(pasta, exist_ok=True)

    nome_arquivo = os.path.join(pasta, f"relatorio_{cidade}.txt")

    with open(nome_arquivo, "w", encoding="utf-8") as f:

        f.write("RELATÓRIO DE QUEIMADAS\n")
        f.write(f"Cidade: {cidade}\n")
        f.write(f"Total de focos: {total_focos}\n")
        f.write(f"Média de risco: {media_risco:.2f}\n")
        f.write(f"Média de FRP: {media_frp:.2f}\n")
        f.write("Satélite principal: GOES-19\n")

    print(f"\nRelatório gerado em: {nome_arquivo}")