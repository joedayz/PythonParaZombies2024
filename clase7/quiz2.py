# ['2','55','888','9','30','45']

# busca '888'

# output : el 888 si esta en la lista

# busca: 777

#output: ese numero no esta en la lista

def searchStr(lista, n):
          lp = len(lista)
          i =0
          found = 0
          for i in range(lp):
                    if (lista[i] == n):
                              print("\n\n",n,"is found at index",i)
                              found=1
                              
          if found == 0:
                    print ("\n\n",n,"is not found in the list")          
          
          
lista = ['2','55','888','9','30','45']
key = '7'
searchStr(lista,key)


          