import sys
import os

# Adiciona a pasta src ao caminho
sys.path.append(
    os.path.join(
        os.path.dirname(__file__),
        "Floratech",
        "src"
    )
)
from login import (inicializar_arquivo, cadastrar_usuario, fazer_login, mostrar_titulo)
from leitor import carregar_dados
from menu import mostrar_menu
from historico import adicionar_consulta, mostrar_historico
from risco import classificar_risco
from relatorio import gerar_relatorio

# Caminho do CSV
caminho_csv = os.path.join(
    os.path.dirname(__file__),
    "Floratech",
    "dados",
    "cidades.csv"
)

# Carrega dados
dados = carregar_dados(caminho_csv)
inicializar_arquivo()

# Login
def calcular_risco_medio(registros):

    soma = 0

    for r in registros:
        soma += float(r["risco_fogo"])

    return soma / len(registros)


def filtrar_por_bioma(dados, bioma):

    filtrado = {}

    for cidade, registros in dados.items():

        if registros[0]["bioma"].upper() == bioma.upper():
            filtrado[cidade] = registros

    return filtrado
usuario_logado = None
while usuario_logado is None:
    mostrar_titulo()
    print("\n1 - Fazer Login")
    print("2 - Cadastrar Usuário")
    print("3 - Sair")
    opcao_inicio = input("\nEscolha uma opção: ")
    if opcao_inicio == "1":
        usuario = fazer_login()
        if usuario:
            usuario_logado = usuario
            print(f"\nBem-vindo, {usuario_logado}!")
        else:
            print("\nEmail ou senha incorretos. Tente novamente.")
    elif opcao_inicio == "2":
        cadastrar_usuario()
    elif opcao_inicio == "3":
        print("\nAté logo!")
        sys.exit()
    else:
        print("\nOpção inválida. Tente novamente.")
# Loop
while True:

    mostrar_menu()

    opcao = input("\nEscolha uma opção: ")

    # Cnsulta
    if opcao == "1":

        busca = input("\nDigite parte do nome da cidade: ").strip().upper()

        resultados = []

        for cidade in sorted(dados.keys()):

            if busca in cidade:
                resultados.append(cidade)

        if len(resultados) == 0:

            print("\nNenhuma cidade encontrada.")

        else:

            print("\nCIDADES ENCONTRADAS:\n")

            for indice, cidade in enumerate(resultados, start=1):
                print(f"{indice} - {cidade}")

            try:

                escolha = int(input("\nEscolha o número da cidade: "))

                if escolha < 1 or escolha > len(resultados):

                    print("\nNúmero inválido.")

                else:

                    cidade_escolhida = resultados[escolha - 1]

                    adicionar_consulta(cidade_escolhida)

                    registros = dados[cidade_escolhida]
                    ultimo = registros[-1]

                    nivel_risco = classificar_risco(
                        ultimo["risco_fogo"]
                    )

                    print("\n" + "=" * 50)
                    print(f"Cidade: {cidade_escolhida}")
                    print(f"Estado: {ultimo['estado']}")
                    print(f"Bioma: {ultimo['bioma']}")
                    print(f"Latitude: {ultimo['lat']}")
                    print(f"Longitude: {ultimo['lon']}")
                    print(f"Satélite: {ultimo['satelite']}")
                    print(f"Dias sem chuva: {ultimo['numero_dias_sem_chuva']}")
                    print(f"Risco de fogo: {ultimo['risco_fogo']}")
                    print(f"Classificação: {nivel_risco}")
                    print(f"FRP: {ultimo.get('frp', 'N/A')}")
                    print(f"Precipitação: {ultimo['precipitacao']}")
                    print(f"Último registro: {ultimo['data_hora_gmt']}")
                    print("=" * 50)

            except ValueError:
                print("\nDigite apenas números.")


    # Historico
    elif opcao == "2":

        print("\nHISTÓRICO DE CONSULTAS")
        print("-" * 40)

        mostrar_historico()

    # Estatísticas
    elif opcao == "3":

        maior_risco = 0
        cidade_maior_risco = ""

        for cidade, registros in dados.items():

            risco = float(registros[-1]["risco_fogo"])

            if risco > maior_risco:
                maior_risco = risco
                cidade_maior_risco = cidade

        print("\nESTATÍSTICAS")
        print("-" * 40)
        print(f"Total de cidades: {len(dados)}")
        print(f"Maior risco: {maior_risco}")
        print(f"Cidade mais crítica: {cidade_maior_risco}")
   

    # Sair
    elif opcao == "6":

        print(f"\nAté logo, {usuario_logado}!")
        break

    # Relatorio
    elif opcao == "4":

        cidade = input("\nDigite a cidade: ").strip().upper()

        if cidade in dados:
            gerar_relatorio(cidade, dados[cidade])
        else:
            print("\nCidade não encontrada.")

    # Ranking Geral
    elif opcao == "8":

        ranking = []

        for cidade, registros in dados.items():

            media = calcular_risco_medio(registros)

            ranking.append((cidade, media))

        ranking.sort(key=lambda x: x[1], reverse=True)

        print("\nTOP 10 CIDADES MAIS PERIGOSAS")
        print("-" * 40)

        for i, (cidade, media) in enumerate(ranking[:10], start=1):
            print(f"{i} - {cidade} | risco médio: {media:.2f}")
   
    # Comparacao entre biomas
    elif opcao == "5":

        bioma1 = input("\nDigite o primeiro bioma: ").strip()
        bioma2 = input("Digite o segundo bioma: ").strip()

        dados1 = filtrar_por_bioma(dados, bioma1)
        dados2 = filtrar_por_bioma(dados, bioma2)

        if len(dados1) == 0 or len(dados2) == 0:

            print("\nNenhum dado encontrado.")

        else:

            media1 = sum(calcular_risco_medio(r) for r in dados1.values()) / len(dados1)
            media2 = sum(calcular_risco_medio(r) for r in dados2.values()) / len(dados2)

            print("\nCOMPARAÇÃO ENTRE BIOMAS")
            print("-" * 40)
            print(f"{bioma1.upper()}: {media1:.2f}")
            print(f"{bioma2.upper()}: {media2:.2f}")

    else:

        print("\nOpção inválida.") 
        