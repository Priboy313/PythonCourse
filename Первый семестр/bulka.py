import sys

item = sys.argv[1]
item = item.split(",")
item[0] = item[0].capitalize()

result = ""

for x in range(0, len(item) - 2):
	result += item[x] + ", "

result += str(item[len(item) - 2]) + " и " + str(item[len(item) - 1]) + "."

print(result)
