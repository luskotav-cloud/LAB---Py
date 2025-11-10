# EX5 - RM568040 - Lucas Otavio Lacerda Menezes
nomes = ["ana", "bruno", "carla", "diego", "lucas"]
novo = input("Digite outro nome para adicionar: ")
nomes.append(novo)
nomes_unicos = list(set(nomes))
print("Lista final (sem duplicatas):", nomes_unicos)


# EX6 - RM568040 - Lucas Otavio Lacerda Menezes
usuario = {}
usuario["nome"] = input("Nome: ")
usuario["idade"] = int(input("Idade: "))
usuario["status"] = input("Status (ativo/inativo): ")

print(f"\nUsuário cadastrado:")
for chave, valor in usuario.items():
    print(f"{chave}: {valor}")