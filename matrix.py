__author__ = 'Sonni'

def plus(m, n):
    if len(m) == len(n) and len(m[0]) == len(n[0]):
        result = []
        for x in range(len(m)):
            tmp = []
            for y in range(len(m[0])):
                tmp.append(m[x][y] + n[x][y])
            result.append(tmp)

        return result

    else:
        print "The matrices do not have the same length"
        exit()

def minus(m, n):
    if len(m) == len(n) and len(m[0]) == len(n[0]):
        result = []
        for x in range(len(m)):
            tmp = []
            for y in range(len(m[0])):
                tmp.append(m[x][y] - n[x][y])
            result.append(tmp)

        return result

    else:
        print "The matrices do not have the same length"
        exit()


def multiply(m, n):
    if len(m[0]) == len(n):
        result = []
        for x in range(len(m)):
            tmp = []
            for y in range(len(n[0])):
                tmpCell = []
                for z in range(len(m[0])):
                    tmpCell.append(m[x][z] * n[z][y])

                tmpResult = tmpCell[0]
                for i in range(len(tmpCell) - 1):
                    tmpResult += tmpCell[i + 1]

                tmp.append(tmpResult)
            result.append(tmp)

        return result

    else:
        print "m's column count has to be equal to n's row count"
        exit()

#m = result, a = first matrix, b = second matrix
def formatMatrix(m, a, b, operation):
    for i in range(len(m)):
        print m[i]

    print "\nLatex code:"
    print "_______________________"
    if operation == "*":
        print "Matricerne kan ganges sammen, da matrix A's antal sojler, svarer til matrix B's antal raekker.\\"
        print "\\\\Matrix multiplikation forgaar paa folgende maade: $(AB)_{ij}=\sum\limits_{k=1}^mA_{ik}B_{kj}$"
    if operation == "+":
        print "Matrix addition er trivielt og resultatet er som folgende:\\\\"
    if operation == "-":
        print "Matrix subtraction er trivielt og resultatet er som folgende:\\\\"

    print "\["

    printMatrix(a)
    print operation
    printMatrix(b)
    print "="
    printMatrix(m)

    print "\]"

    print "_______________________"

def printMatrix(m):
    print "\\begin{bmatrix}"

    for x in range(len(m)):
        tmpString = ""
        for y in range(len(m[0])):
            if y == 0:
                tmpString += str(m[x][y])
            else:
                tmpString += " & " + str(m[x][y])
        tmpString += " \\\\"
        print tmpString

    print "\end{bmatrix}"


def takeMatrixInput():
    userInput = raw_input()
    row = []
    result = []
    while (userInput != "e"):

        input = userInput.split(" ")
        for i in range(len(input)):
            row.append(int(input[i]))

        result.append(row)
        row = []
        userInput = raw_input()
    return result


print "Write row by row, each number separated by space. 'e' = next, ENTER = new row: "
m = takeMatrixInput()

print "Enter next matrix: e = next"
n = takeMatrixInput()



op = raw_input("Those operation (+/-/*): ")
print op
if op == "+":
    result = plus(m, n)
elif op == "-":
    result = minus(m, n)
elif op == "*":
    result = multiply(m, n)
else:
    print "No valid operation entered... closing"
    exit()

formatMatrix(result, m, n, op)