# 5

# salida
# *
# **
# ***
# ****
# *****

n = int(input("Ingrese un número: "))
# for i in range(1, n + 1):
#     print("*" * i)  #  * * 2 = **    * * 3 = ***
    
    


for x in range(n):   # 0 1 2 3 4
     for y in range(x + 1):
         print("*", end="")
     print()    
    
