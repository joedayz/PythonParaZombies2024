
# El programa te pide que ingreses los numeros que quieras y luego te imprime el promedio de los numeros ingresados.
# input
# 4, 10, 20, 15, 12 

# output
# average is 12.2

values = int(input("Cuantas notas vas a ingresar"))
sumaOfValues = 0

          
for i in range (1, values+1):
          v =int(input("Ingrese la nota: "))
          sumaOfValues += v
          
print("El promedio es: ", sumaOfValues/values)