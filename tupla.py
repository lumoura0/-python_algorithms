# Tuplas são imutáveis
# Criando uma tupla de exemplo
minha_tupla = (1, 2, 3, 4, 5)
tupla_nomes = ('Shiro', 'Luna', 'Riku')

print('Tupla de números:', minha_tupla)
print('Tupla de nomes:', tupla_nomes)

# Acessando valores em uma tupla

print('Primeiro elemento da tupla:', minha_tupla[0])
print('Segundo elemento da tupla:', minha_tupla[1])
print('Terceiro elemento da tupla:', minha_tupla[2])

# Tentativa de alterar um valor de uma tupla    

minha_tupla[0] = 10

# Tuplas são imutáveis, logo esta tentativa irá gerar um erro