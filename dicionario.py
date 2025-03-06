# Criando um dicionário

dados = {'nome': 'Shiro', 'idade': 24, 'sexo': 'masculino'}

print(dados)

# Acessando dados

print(dados['nome'])
print(dados['idade'])
print(dados['sexo'])

# Adicionando novos dados

dados['email'] = 'shiro@example.com'

print(dados)

# Atualizando dados

dados['idade'] = 25

print(dados)

# Deletando dados

del dados['email']

print(dados)

# Verificando se um dado existe

print('idade' in dados)
print('email' in dados)

# Métodos Keys() Values() items()
chaves = dados.keys()
print('Chaves', chaves)

valores = dados.values()
print('Valores', valores)

items = dados.items()
print('Items', items)