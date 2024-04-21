# input   [[10, 20, 30], [40, 50, 60]]

# sum row 1: 60
# sum row 2: 150



#output

# Matrix: [[1, 2, 3], [4, 5, 6]]
# sum of row1: 6
# sum of row2: 15


#  a[0][0] + b[0][0] = 1 + 10 = 11

# a = [ [1,2,3], [4, 5, 6] ]

# sumRow1 = a[0][0] + a[0][1] + a[0][2]
# sumRow2 = a[1][0] + a[1][1] + a[1][2]

# print("Matrix:", a)
# print("sum of row1:", sumRow1)
# print("sum of row2:", sumRow2)


a = [ [10,20,30],[40,50,60] ]



sumRow1 = 0
sumRow2 = 0

for i in range(len(a[0])):
    sumRow1 += a[0][i]
for i in range(len(a[1])):
    sumRow2 += a[1][i]    
        
print("Matrix:", a)
print("sum of row1:", sumRow1)
print("sum of row2:", sumRow2)