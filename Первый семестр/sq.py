import sys
NUM = str(sys.argv[1]).split(" ")
_result = [0]
for x in NUM:
    _result.append(int(x))

result = []
for x in range(1, len(_result)):
    if _result[x] > _result[x - 1]:
        result.append(1)
    else:
        result.append(0)

result.sort()
if result[0] == 0:
    print(0)
else:
    print(1)