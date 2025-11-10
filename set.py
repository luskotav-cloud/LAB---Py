# EXEMPLO DE USO DO set()
# RM568040 - Lucas Otavio Lacerda Menezes

# Lista com IDs que tentaram acessar o sistema
tentativas = [101, 102, 103, 101, 105, 102, 107, 103]

print("Tentativas originais:", tentativas)

# Transforma a lista em conjunto (remove duplicatas)
usuarios_unicos = set(tentativas)

print("IDs únicos:", usuarios_unicos)

# Adiciona novo ID
usuarios_unicos.add(110)
print("Após adicionar 110:", usuarios_unicos)

# Remove um ID
usuarios_unicos.discard(102)
print("Após remover 102:", usuarios_unicos)

# Outro conjunto: IDs com acesso liberado
acesso_liberado = {101, 105, 107, 110}

# Mostra quem tem acesso (interseção entre os dois conjuntos)
acessos_validos = usuarios_unicos.intersection(acesso_liberado)
print("Usuários com acesso liberado:", acessos_validos)
