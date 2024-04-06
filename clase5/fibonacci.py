# [ 0 , 1, 1, 2, 3, 5, 8, 13, 21 , 34]  Sequence of Fibonacci numbers

# el programa debe decirte si es fibonacci o no

fib = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181]

count = 2
flag = 1

while count < len(fib) and flag == 1:
          if fib[count] != fib[count-1] + fib[count-2]:
                    flag = 0
          count+=1

if flag == 0:
          print("No es un número de Fibonacci")
else:     
          print("Es un número de Fibonacci")
          
# lista de listas          