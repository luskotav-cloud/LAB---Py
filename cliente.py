# EXEMPLO SOCKET CLIENTE
# RM568040 - Lucas Otavio Lacerda Menezes

import socket  # Biblioteca de rede

# Cria o socket TCP
cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Conecta no servidor local na porta 8080
cliente.connect(("127.0.0.1", 8080))
print("Conectado ao servidor!")

# Envia uma mensagem
mensagem = input("Digite uma mensagem para o servidor: ")
cliente.send(mensagem.encode())

# Recebe a resposta do servidor
resposta = cliente.recv(1024).decode()
print("Servidor respondeu:", resposta)

# Fecha a conexão
cliente.close()
