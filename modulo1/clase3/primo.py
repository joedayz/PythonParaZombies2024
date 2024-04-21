# hacer un programa que te diga si un numero es primo o no en python

# input: 7

# output: 7 es primo

# input: 8

# output: 8 no es primo

num = int(input("Ingrese un numero: "))

countFactor = 0

for i in range(1, num + 1):
    if num % i == 0:
        countFactor += 1
        
if(countFactor == 2):
    print(f"{num} es primo")
else:
          print(f"{num} no es primo")  