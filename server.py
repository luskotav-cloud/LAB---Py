# EXEMPLO SOCKET SERVIDOR
# RM568040 - Lucas Otavio Lacerda Menezes

import socket  # Importa a biblioteca que permite comunicação de rede

# Cria um objeto socket (IPv4, TCP)
servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Define o endereço e a porta que o servidor vai escutar
servidor.bind(("127.0.0.1", 8080))

# Coloca o servidor para escutar (aceitar conexões)
servidor.listen()

print("Servidor ativo e aguardando conexões...")

# Aceita uma conexão (retorna o socket do cliente e o endereço)
cliente_socket, cliente_endereco = servidor.accept()
print(f"Conexão estabelecida com {cliente_endereco}")

# Recebe mensagem do cliente (máx. 1024 bytes)
mensagem = cliente_socket.recv(1024).decode()
print("Mensagem recebida do cliente:", mensagem)

# Envia resposta de volta para o cliente
cliente_socket.send("Mensagem recebida com sucesso!".encode())

# Fecha conexões
cliente_socket.close()
servidor.close()
