size = int(input("Enter size of a matrix:  "))
print("\n")
print("-------------------------------------------------\n")
def printmatrix(matrix):
    for i in range (len(matrix)):
        print(matrix[i])
        
def creatematrix(size):
    matrix=[] 
    for i in range(size):
        temp=[]
        for j in range(size):
            temp.append("X")
        matrix.append(temp)
    return matrix

def checkdiagonal(row,col, colsUsed):
    for i in range(row):
        if abs(i-row)==abs(colsUsed[i]-col):
            return False
    return True
    
def placequeen(n,colsUsed, size,matrix):
    if n>=size:
        return True
    
    for j in range(size):
        if j not in colsUsed:
            if checkdiagonal(n,j,colsUsed):
                matrix[n][j]="Q"
                colsUsed.append(j)
                if placequeen(n+1,colsUsed,size,matrix)==True:
                    return True
                else:
                    matrix[n][colsUsed.pop()]="X"     
    return False

i=0
for i in range(size):
    matrix=creatematrix(size)
    colsUsed=[]
    matrix[0][i]="Q"
    colsUsed.append(i)
    if placequeen(1, colsUsed, size, matrix)==False:
        # print("False")
        pass
    else:
        printmatrix(matrix)
        print("\n")
        print("-------------------------------------------------\n")