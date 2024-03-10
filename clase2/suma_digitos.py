sum = 0
number = int(input("Ingrese un número positivo de 4 digitos: "))  #1234  5678

# la suma de 1234 es 10 , 5678 es 26

if (number>0 and number<9999):
          sum += number%10  #3
          number = number//10  #12
          if(number>0):
                    sum += number%10  # 2
                    number = number//10  # 1
          if(number>0):
                    sum += number%10 #1
                    number = number//10 #0
          if(number>0):
                    sum += number%10 
                    number = number//10        
          print("La suma de los digitos es: ", sum)
else:
          print("El número ingresado no es válido")                    