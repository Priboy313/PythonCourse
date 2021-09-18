import sys

item = str(sys.argv[1])

result = []

#revers
for x in range(len(item)):
	result.append(item[len(item) - 1 - x])

item = ""

for x in range(len(result)):
	item += result[x]

result = item.split(" ")
item = ""

for x in range(len(result)):
	item += result[len(result) - 1 - x] + " "
item.strip(" ")

print(item)
