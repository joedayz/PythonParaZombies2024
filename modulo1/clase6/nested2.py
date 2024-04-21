a = [ [1,2,3,4], [5, 6, 7, 8], [9, 10, 11, 12] ]
b =  [ [1, 2, 3, 4],
      [5, 6, 7, 8],
      [9, 10, 11, 12]]

c = [ [0,0,0,0], [0,0,0,0], [0,0,0,0] ]

print(a)
print(b)

rows, cols = 3, 4

for i in range(rows):
    for j in range(cols):
        c[i][j] = a[i][j] + b[i][j]
        
print(c)