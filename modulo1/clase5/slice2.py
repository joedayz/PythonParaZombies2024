letters = ['a','b','c','d','e','f','g','h','i']
print("List of letters: ")
print(letters)
 
print('Slice "[2:7]" from index 2 till before index 7')
print(letters[2:7])
print('Slice "[2:-4]" from index 2 till before index -4')
print(letters[2:-4])
print('Slice "[-4:-1]" from index -4 till before index -1')
print(letters[-4:-1])
print('Slice "[-6:8]" from index -6 till before index 8')
print(letters[-6:8])
 
print('Slice "[7:2]" from index 7 till before index 2')
print('no element in this wrongly ordered index values')
print(letters[7:2])
print('Slice "[-2:-4]" from index -2 till before index -4')
print('no element in this wrongly ordered index values')
print(letters[-2:-4])