#   input: Perusalen

#   output: nelasureP


word = input("Enter Word: ")
def wordr(word):
    wordr = ""   
    for i in range(len(word) - 1, -1, -1):       
        wordr += word[i]  
    return wordr
    
Reveez_word = wordr(word)
# print("word:", Reveez_word )


myString1 = "Educative"
myString2 = ""

myString2 += myString1[-1]
myString2 += myString1[-2]
myString2 += myString1[-3]
myString2 += myString1[-4]
myString2 += myString1[-5]
myString2 += myString1[-6]
myString2 += myString1[-7]
myString2 += myString1[-8]
myString2 += myString1[-9]
print("myString2:", myString2)                    