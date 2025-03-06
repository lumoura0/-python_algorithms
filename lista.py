# Coleção de elementos ordenados e mutaveis
lista = [1,2,3,4,5]

# Adicionando um elemento ao final da lista

lista.append(6)

print(lista)

# Adicionando um elemento em um indice especifico

lista.insert(2, 7)

print(lista)

print(lista[1: 5])
print(lista[::-1])
print(lista[:5])

# Remover um elemento

lista.remove(7)

print(lista)

# Remover um elemento pelo indice

del lista[2]

print(lista)

# Verificar se um elemento está na lista

print(4 in lista)

indice = lista.index(6)
print('indice do elemento 6: ',indice)

lista.pop(3)
print(lista)

lista.sort()
print(lista)