# Palindrome

# "level" 

# input:  level

# output: Si es palindrome

# input:  leve

# output: No es palindrome

# word = input("Enter word: ")
# def palindrome(word):
#     word = word.lower()  
#     return word == word[::-1]  
# if  palindrome(word):
#     print(f"'{word}' it's a palinbrome.")
# else:
#     print(f"'{word}' it is not a palinbrome.")
    
    
string = "level"


if (string[0]==string[-1] and string[1]==string[-2]):
          print("Si es palindrome")
else:     
          print("No es palindrome")