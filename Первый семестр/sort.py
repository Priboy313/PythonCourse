import sys

item = str(sys.argv[1])
notresult = []
result = []

for x in range(len(item)):
	notresult.append(item[x:x+1])

notresult.sort()

for x in range(len(notresult)):
	if notresult[x] != notresult[x-1]:
		result.append(notresult[x])

item = ""

for x in range(len(result)):
	item += result[x]

print(item)
