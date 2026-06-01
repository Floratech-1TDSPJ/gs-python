import csv
import os

ARQUIVO_USARIOS = os.path.join(
    os.path.dirname(__file__),
    "..",
    "..",
    "usuario",
    "usuarios.csv"
)
def inicializar_arquivo():
    os.makedirs(os.path.dirname(ARQUIVO_USARIOS), exist_ok=True)
    if not os.path.exists(ARQUIVO_USARIOS):
        with open(ARQUIVO_USARIOS, mode='w', newline='', encoding='utf-8') as arquivo:
            writer = csv.writer(arquivo)
            writer.writerow(['nome', 'email', 'senha'])
def mostrar_titulo():
  
    print("====================================")
    print("               Floratech            ")
    print("====================================")


def cadastrar_usuario():
    while True:
        mostrar_titulo()
        print("\nCadastro de Usuário")
        nome = input("Digite seu nome: ").strip()
        email = input("Digite seu email: ").strip()
        senha = input("Digite sua senha: ").strip()
        confirmacao = input("Confirme sua senha: ").strip()
        
        if senha != confirmacao:
            print("\nAs senhas não coincidem. Tente novamente.")
            continue

        with open(ARQUIVO_USARIOS, mode='a', newline='', encoding='utf-8') as arquivo:
            writer = csv.writer(arquivo)
            writer.writerow([nome, email, senha])

        print("\nUsuário cadastrado com sucesso!")
        input("Pressione Enter para continuar...")
        return
def fazer_login():
    mostrar_titulo()
    print("\nLogin de Usuário")
    email = input("Digite seu email: ").strip()
    senha = input("Digite sua senha: ").strip()
    with open(ARQUIVO_USARIOS, mode='r', newline='', encoding='utf-8') as arquivo:
        leitor = csv.DictReader(arquivo)
        for usuario in leitor:
            if( usuario['email'] == email and usuario['senha'] == senha ):
                return usuario['nome']
            return None