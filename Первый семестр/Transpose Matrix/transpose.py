FILE = open("matrix.txt", encoding="utf8")
Matrix = FILE.read().strip("\n ").split("\n")
FILE.close()
trans_Matrix = []

for x in range(len(Matrix)):
    Matrix[x] = Matrix[x].split(" ")

trans_Matrix = [[0 for j in range(len(Matrix))] for i in range(len(Matrix[0]))]

for i in range(len(Matrix)):
    for j in range(len(Matrix[0])):
        trans_Matrix[j][i] = Matrix[i][j]


trans_FILE = open("transpose_matrix.txt", "w")
for x in range(len(trans_Matrix)):
    _result = ""
    for y in range(len(trans_Matrix[0])):
        _result += str(trans_Matrix[x][y]) + " "

    trans_FILE.write(str(_result.strip() + "\n"))