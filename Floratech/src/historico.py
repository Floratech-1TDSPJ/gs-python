historico = []

def adicionar_consulta(cidade):
    historico.append(cidade)

def mostrar_historico():
    if len(historico) == 0:
        print("\nNenhuma consulta realizada.")
        return

    print("\nHistórico de consultas:")

    for indice, cidade in enumerate(historico, start=1):
        print(f"{indice} - {cidade}")