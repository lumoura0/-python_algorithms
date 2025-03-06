# Loop For
# lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# for i in lista:
#     print(i)

print('For utilizando tupla')
tupla = (1, 2, 3, 4, 5, 6, 7, 8)
for elemento in tupla:
    print(elemento)

pessoa = {"nome": "shiro", "tipo": "gato"}

for chave, valor in pessoa.items():
    print(f'{chave}: {valor}')

# numero = [1, 2, 3, 4, 5, 6, 7, 8]
# for numero in range(5):
#     print(numero)

lista = [1, 2, 3, 4, 5]

# for i in range(0, len(lista)):
#     print("Indice", i)

# enumerate()

for index, numero in enumerate(lista):
    print(f'Indice {index}: {numero}')
