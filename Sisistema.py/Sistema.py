
import json

arquivo_reserva = 'reservas.json'

# Carrega as reservas do arquivo, tratando arquivo vazio ou inexistente
try:
    with open(arquivo_reserva, 'r') as f:
        conteudo = f.read()
        if conteudo.strip() == "":
            reservas = {}
        else:
            reservas = json.loads(conteudo)
except FileNotFoundError:
    reservas = {}
    with open(arquivo_reserva, 'w') as f:
        json.dump(reservas, f)

def salvar_reservas():
    with open(arquivo_reserva, 'w') as f:
        json.dump(reservas, f, indent=4)

def comprar_passagem():
    nome = input("Nome do passageiro: ")
    destino = input("Destino do passageiro: ")
    codigo = f"{nome[:3].upper()}{destino[:3].upper()}{len(reservas)+1}"

    reservas[codigo] = {
        'nome': nome,
        'destino': destino,
        'codigo': codigo,
        'checkin': False
    }

    salvar_reservas()
    print(f"Reserva realizada com sucesso! Seu código de reserva é: {codigo}")

def fazer_checkin():
    codigo = input("Digite o código da sua reserva: ")
    if codigo in reservas:
        if reservas[codigo]["checkin"]:
            print("Check-in já realizado.")
        else:
            reservas[codigo]["checkin"] = True
            salvar_reservas()
            print("Check-in realizado com sucesso!")
    else:
        print("Código de reserva não encontrado.")

def consultar_reservas():
    codigo = input("Digite o código da sua reserva: ")
    if codigo in reservas:
        r = reservas[codigo]
        status = "sim" if r['checkin'] else "não"
        print(f"Nome: {r['nome']}, Destino: {r['destino']}, Check-in: {status}")
    else:
        print("Código de reserva não encontrado.")

def menu():
    print("\n=== SISTEMA DE RESERVA DE PASSAGENS AÉREAS ===")
    print("1. Comprar passagem")
    print("2. Fazer check-in")
    print("3. Consultar reservas")
    print("4. Sair")

while True:
    menu()
    opcao = input("Selecione uma opção: ")
    if opcao == '1':
        comprar_passagem()
    elif opcao == '2':
        fazer_checkin()
    elif opcao == '3':
        consultar_reservas()
    elif opcao == '4':
        print("Saindo do sistema...")
        break
    else:
        print("Opção inválida, tente novamente.")