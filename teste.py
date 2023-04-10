import redis


try:
    creds_provider = redis.UsernamePasswordCredentialProvider("default", "redispw")
    r = redis.Redis(host="localhost", port=32768, credential_provider=creds_provider)
    r.ping()
    print("Conexão bem sucedida")
except:
    print("Erro de conexão")


def compra():
    print("Você selecionou:\nCOMPRA DE INGRESSOS")
    print("-------------------------\n")
    nome = str(input("Digite seu nome: "))
    chegada = r.incr("contador")
    r.rpush("fila", f"Posição: {chegada}, Nome: {nome}")
    posicao = r.llen("fila")
    print("-------------------------")
    print(f"{nome}, sua posição na fila é {chegada}")
    print("-------------------------\n")


def fila():
    print("Você selecionou:\nVER FILA")
    print("-------------------------\n")
    fila = r.lrange("fila", 0, -1)
    for item in fila:
        print(item.decode())
    print("-------------------------\n")


def proximo():
    print("Você selecionou:\nATENDER O PRÓXIMO CLIENTE")
    print("-------------------------\n")
    remover = r.lpop("fila")
    print(f"O cliente atendido foi {remover.decode()}")
    print("-------------------------\n")


while True:

    print("Bem vindo! O que deseja fazer?")
    print("[1] Comprar ingressos")
    print("[2] Mostrar fila")
    print("[3] Atender o próximo cliente")
    print("[4] Sair")
    op = int(input("Qual a opção desejada?: "))
    print("-------------------------\n")


    if op == 1:
        compra()

    if op == 2:
        fila()

    if op == 3:
        proximo()

    if op == 4:
        print("Você selecionou:\nSAIR")
        print("-------------------------\n")
        print("Obrigado. Volte sempre!")
        print("-------------------------\n")
        break