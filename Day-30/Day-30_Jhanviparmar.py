#day30
def lowerTringle(matrix, row, col):     
    for i in range(0, row):     
        for j in range(0, col):         
            if (i < j):             
                print("0", end = " ")             
            else:
                print(matrix[i][j],
                       end = " " )         
        print(" ")
m = int(input("Number of rows: "))
n = int(input("Number of columns: "))
matrix = []
print("Enter the elements row-wise-")
for i in range (0, m): #rows
    x = []
    for j in range (0, n): #columns
        x.append(int(input()))
    matrix.append(x)
lowerTringle(matrix, m, n)
