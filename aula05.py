lista = ['gomes', 10, True, 1.60]

lista1 = [1,2,3,4,5,6,7,8,9,10]

#print(lista1[0])
#print(lista1[2:])
# indices negativos sao tratados de maneira, o -1 é considerado o ultimo elemento
print(lista1[-1])

lista_int = [10,5,3,49,8,3,4,9,42,15,16,13,11,20]
print(lista_int)
lista_int.sort()

print(lista_int)
lista_int.sort(reverse=True)

print(lista_int)
print(f'Lista ordenada direto no print: {sorted(lista_int, reverse=True)}')

# remove, pop, del

nomes = ['gomes', 'oliveira', 'joao', 'pedro', 'jose', 'dias', 'ronaldo', 'kauan']