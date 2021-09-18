import sys

result = 0

for x in range(1, 6):
	if int(sys.argv[x]) > result:
		result = int(sys.argv[x])

print(result)
