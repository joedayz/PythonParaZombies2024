a = 1
inputCount = 0

sum =0

while a!=0:
          a = int(input("Ingrese un numero: "))
          sum += a 
          inputCount += 1

if inputCount > 1:
          print("El promedio de los numeros ingresados es: ", sum / (inputCount - 1))          