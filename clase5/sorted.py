lista = [5, 2, 7, 9, 1]

len1 = len(lista) - 1

print("Longitud de la lista: ", len(lista))

#ordena de mayor a menor
for i in range(len(lista)):
    for j in range(0, len1 - i):
        if lista[j] < lista[j+1]:
            t = lista[j]
            lista[j] = lista[j+1]
            lista[j+1] = t
            
print("Lista ordenada de mayor a menor: ", lista)

#ordena de menor a mayor
for i in range(len(lista)):
    for j in range(0, len1 - i):
        if lista[j] > lista[j+1]:
            t = lista[j]
            lista[j] = lista[j+1]
            lista[j+1] = t
            
print("Lista ordenada de mayor a menor: ", lista)