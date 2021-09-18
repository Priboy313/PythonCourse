import sys

ITEM = str(sys.argv[1])
ITEM = ITEM.strip(" ")

ITEM = ITEM.split(" ")

result = []

for x in range(0, len(ITEM)):
	if ITEM[x].isalnum():
		result.append(ITEM[x])


print(len(result))
