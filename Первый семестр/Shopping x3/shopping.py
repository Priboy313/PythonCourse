FFILE = open("shopping_list_1.txt", encoding="utf8").read().strip("\n ").split("\n")
SFILE = open("shopping_list_2.txt", encoding="utf8").read().strip("\n ").split("\n")
TFILE = open("shopping_list_3.txt", encoding="utf8").read().strip("\n ").split("\n")
_result = []

def AddList(first, second, thid):
	for x in range(len(first)):
		_result.append(first[x])

	for x in range(len(second)):
		_result.append(second[x])

	for x in range(len(thid)):
		_result.append(thid[x])

	_result.sort()
AddList(FFILE, SFILE, TFILE)

result = []
for y in range(len(_result)):
	if _result[y] != _result[y-1]:
		result.append(_result[y] + "\n")

#================= Запись.
FINAL_FILE = open("shopping_list.txt", "w", encoding="utf8")
for y in range(len(result)):
	FINAL_FILE.write(result[y] + "")
