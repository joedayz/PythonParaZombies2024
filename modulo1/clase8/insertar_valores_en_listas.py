a = [1,2,3]
b = [8,9]
print("List a:",a)
print("List b:",b)

print('\nAgregando el 4 a la lista a')
a.append(4)
print("List a:",a)

print('\nAgregando la lista b como sublista en la lista a')
a.append(b)
print("List a:",a)
print("List b:",b)

print('\nCrear una nueva copia de la lista b en lista c')
c = b.copy()
print('List b:',b)
print("List c:",c)

print('\nReferenciar la lista b en la lista d')
d = b
print('List d:',d)

print('\nAgregar todos los miembros de b en la lista c')
c.extend(b)
print('List c:',c)

print('\nInsertar el numero 15 en el indice 1 de la lista b')
b.insert(1, 15)
print('List b:',b)
