# EX9 - RM568040 - Lucas Otavio Lacerda Menezes
import requests
resposta = requests.get("https://www.openai.com")

print("Status da conexão:", resposta.status_code)
if resposta.status_code == 200:
    print("Conexão bem-sucedida!")
else:
    print("Erro ao acessar o site.")
