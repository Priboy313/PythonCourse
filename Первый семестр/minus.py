SRC = open("numbers.txt").read().split(" ")

_result = []
for x in SRC:
	if int(x) < 0: _result.append(x)

result = 0
for x in _result:
	result += int(x)

print(result)
