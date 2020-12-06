p = int(input("enter the number of rows:"))
q = int(input("enter the number of columns:"))

print("enter the elements for matrix1:")
matrix1 = [[int(input()) for i in range (q)] for j in range (p)]
print("matrix1:")
for i  in range (p):
    for j in range(q):
        print(format(matrix1[i][j],"<4"),end ="")
    print()

result = [[0  for i in range (p)] for j in range (q)]
for j in range(q):
    for i in range(p):
        result[i][j]= matrix1[j][i]

for i in int(q):
    for j in int(P):
        print(format(result[i][j],"<4"),end="")
    print()
              
