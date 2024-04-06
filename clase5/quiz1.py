#  v = ['a','e','i','o','u','w','h','y']

# Como salida quiero la reversa:  ['y','h','w','u','o','i','e','a']


v = ["a","e","i","o","u","w","h","y"]
print("La lista original es: ", v)

t = v[0]
v[0] = v[-1]
v[-1] = t

t = v[1]
v[1] = v[-2]
v[-2] = t

t=v[2]
v[2] = v[-3]
v[-3] = t
 
t=v[3]
v[3] = v[-4]
v[-4] = t

print("La lista original es: ", v)