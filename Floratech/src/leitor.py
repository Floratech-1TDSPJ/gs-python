import csv

def carregar_dados(caminho_csv):

    dados = {}

    with open(caminho_csv, mode="r", encoding="utf-8") as arquivo:

        leitor = csv.DictReader(arquivo)

        for linha in leitor:

            cidade = linha["municipio"].strip().upper()

            registro = {
                "id": linha["id"],
                "lat": linha["lat"],
                "lon": linha["lon"],
                "data_hora_gmt": linha["data_hora_gmt"],
                "satelite": linha["satelite"],
                "municipio": linha["municipio"],
                "estado": linha["estado"],
                "pais": linha["pais"],
                "municipio_id": linha["municipio_id"],
                "estado_id": linha["estado_id"],
                "pais_id": linha["pais_id"],
                "numero_dias_sem_chuva": linha["numero_dias_sem_chuva"],
                "precipitacao": linha["precipitacao"],
                "risco_fogo": linha["risco_fogo"],
                "bioma": linha["bioma"],
                "frp": linha["frp"] if linha["frp"] != "" else None
            }

            if cidade not in dados:
                dados[cidade] = []

            dados[cidade].append(registro)

    return dados