
def input_matrix(rows, cols):
    matrix = []
    print(f"введіть елементи матриць {rows}x{cols}:")
    for i in range(rows):
        row = list(map(int, input(f"строка {i+1}: ").split()))
        matrix.append(row)
    return matrix

def dodavannya_matric(A, B):
    return [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]

def vidnimannya_matric(A, B):
    return [[A[i][j] - B[i][j] for j in range(len(A[0]))] for i in range(len(A))]

def mnogennya_matric_na_chislo(A, num):
    return [[A[i][j] * num for j in range(len(A[0]))] for i in range(len(A))]

def mnogennya_matric(A, B):
    res= [[0] * len(B[0]) for _ in range(len(A))]
    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                res[i][j] += A[i][k] * B[k][j]
    return res

def druk_res(matrix):
    print("Результат:")
    for row in matrix:
     print("   "  .join(map(str, row)))

def main():
    
    print("оберіть операцію:\n1. додавання\n2. віднімання\n3. множення на число\n4. множення матриць")
    num_oper = int(input("введіть номер операції: "))
    
    if  num_oper in (1, 2, 4):
        rows = int(input("введіть кість строк матриці: "))
        cols = int(input("введіть кількість стовпців матриці: "))
        print("введення першої матриці:")
        A = input_matrix(rows, cols)
        print("введення другої матриці:")
        B = input_matrix(rows, cols)
        
        if num_oper == 1:
            res = dodavannya_matric(A, B)
        elif num_oper == 2:
            res = vidnimannya_matric(A, B)
        elif num_oper == 4:
            res = mnogennya_matric(A, B)
    elif num_oper == 3:
        rows = int(input("ввелдіть кількість строк матриці: "))
        cols = int(input("введіть кількість стовбців матриці: "))
        A = input_matrix(rows, cols)
        num = int(input("введіть число для множення: "))
        res = mnogennya_matric_na_chislo(A, num)
  
    druk_res(res)

if __name__ == "__main__":
    main()
