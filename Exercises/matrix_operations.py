def matrixSum():
    # in this function I'm going to sum two matrix
    print("SUM")
    matrix_1 =[
        [2,1,2],
        [2,3,1],
        [1,0,2],
    ]
    matrix_2 = [
        [1,0,2],
        [1,4,2],
        [1,3,2],
    ]
    for i in range(3):
        for j in range(3):
            matrix_result = matrix_1[i][j]+matrix_2[i][j]
            print(matrix_result,end =" ") #For line print
        print()



def matrixRest():
    print("REST")
    matrix_1 = [
        [1,2,3],
        [1,0,3],
        [1,2,0],
    ]
    matrix_2 =[
        [1,2,3],
        [1,0,2],
        [1,0,3],
    ]
    for i in range(3):
        for j in range(3):
            matrix_result = matrix_1[i][j]-matrix_2[i][j]
            print(matrix_result, end =" ")
        print()

def matrixMultiply():
    print("MULTIPLY")
    matrix_1 = [
        [1,2,3],
        [1,0,3],
        [1,2,0],
    ]
    matrix_2 =[
        [1,2,3],
        [1,0,2],
        [1,0,3],
    ]
    result =[
        [0,0,0],
        [0,0,0],
        [0,0,0]
    ]
    
    for i in range(3):
        for j in range(3):
            for k in range(3):
                matrix_sum = matrix_1[i][k]*matrix_2[k][j]
                result[i][j] += matrix_sum
    for num in result:
        print(num)
def printLine():
    print("------------------------")
# matrix sum
matrixSum() 
printLine()
matrixRest()
printLine()
matrixMultiply()
    

    


