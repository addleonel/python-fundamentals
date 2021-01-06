
# Matrix Operations


def matrixAddition(m1, m2):
    result = []
    values = []
    value = 0
    if len(m1) == len(m2) and len(m1[0]) == len(m2[0]): 
        for i in range(len(m1)):
            for j in range(len(m1[0])):
                value = m1[i][j]+m2[i][j]
                values.append(value)
                value = 0
            result.append(values)
            values = []
        return result
    return "The matrices don't have correct dimensions"



def matrixSubtraction(m1, m2):
    result = []
    values = []
    value = 0
    if len(m1) == len(m2) and len(m1[0]) == len(m2[0]): 
        for i in range(len(m1)):
            for j in range(len(m1[0])):
                value = m1[i][j]-m2[i][j]
                values.append(value)
                value = 0
            result.append(values)
            values = []
        return result
    return "The matrices don't have correct dimensions"

def matrixMultiplication(m1, m2):
    result = []
    values = []
    value = 0
    if len(m1[0]) == len(m2):
        for i in range(len(m1)):
            for j in range(len(m2[0])):
                for k in range(len(m1[0])):
                    value += m1[i][k]*m2[k][j]
                values.append(value)
                value = 0
            result.append(values)
            values = []
        return result
    return "The matrices don't have correct dimensions"
    
                        


def printLine():
    print("-"*50)

if __name__ == '__main__':
    
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

    print(matrixAddition(matrix_1, matrix_2)) 
    printLine()
    print(matrixSubtraction(matrix_1, matrix_2))
    printLine()
    m1 = [
        [1, 0, 2, 3],
        [4, 5, 1, 2],
        [1, 0, 1, 2],
    ]

    m2 = [
        [0, 0, 2, 3],
        [4, 5, 1, 6],
        [1, 1, 2, 7],
        [3, 0, 1, 9],
    ]
    print(matrixMultiplication(m1, m2))
        

    


