import redis
import time

try:
    creds_provider = redis.UsernamePasswordCredentialProvider("default", "redispw")
    r = redis.Redis(host="localhost", port=32768, credential_provider=creds_provider)
    r.ping()
    print("Conexão bem sucedida")
except:
    print("Erro de conexão")


r.set('conectado', 'true')

r.expire('conectado', 300)

tempo_de_vida = r.ttl('conectado')

while tempo_de_vida >= 0:
    # verifica quanto "tempo de vida" em segundos a chave "conectado" ainda possui
    print("-----------------------------------------------------------------------------")
    print(f"Tempo de vida restante da chave 'conectado': {tempo_de_vida} segundos")
    print("-----------------------------------------------------------------------------")

    # aguarda por 5 segundos
    time.sleep(5)

    # verifica o tempo de vida novamente
    tempo_de_vida -= 5

