a = [ [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
 [10, 11, 12, 13, 14, 15, 16, 17, 18, 19],
 [20, 21, 22, 23, 24, 25, 26, 27, 28, 29],
 [30, 31, 32, 33, 34, 35, 36, 37, 38, 39],
 [40, 41, 42, 43, 44, 45, 46, 47, 48, 49]]


# Display in the matrix form:

# row 0 ==>  0      1         2         3         4         5         6         7         8         9
# row 1 ==> 10      11        12        13        14        15        16        17        18        19
# row 2 ==> 20 21 22 23 24 25 26 27 28 29
# row 3 ==> 30 31 32 33 34 35 36 37 38 39
# row 4 ==> 40 41 42 43 44 45 46 47 48 49

# Columns sums are = [ 100, 105, 110, 115, 120, 125, 130, 135, 140, 145]

print("Display in the matrix form:")

rows, cols = 5, 10

for i in range(rows):
    print("row ", i, " ==> ", end = ' ')      
    for j in range(cols):
        print(a[i][j], end = "\t")
    print()      
# como hariamos la suma de columnas?

colsum = [0]*cols  # [0,0,0,0,0,0,0,0,0,0]

for j in range(cols):
    for i in range(rows):
        colsum[j] += a[i][j]


print("\nColumns sums are = ", colsum)