FILE = open("matrix.txt", encoding="utf8").read()
file = str(FILE).strip("\n ").split("\n")

matrix = []
for col in file:
	matrix.append(col.split(" "))

result = 0
for x in range(len(matrix)):
	result += int(matrix[x][x])

print(result)
