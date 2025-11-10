import requests, json

url = 'https://api.github.com/users/luskotav-cloud'

github = requests.get(url)
dados = github.json()
usuario = {}

usuario['Usuario'] = dados['login']
usuario['Nome'] = dados['name']
usuario['Local'] = dados['location']
usuario['Repositórios'] = dados['public_repos']
usuario['Url'] = dados['url']

with open('dados.json', 'w', encoding='utf-8') as arquivo:
    json.dump(dados, arquivo, indent=4, ensure_ascii=False)

print(type(dados), type(usuario), type(github))
print(usuario)