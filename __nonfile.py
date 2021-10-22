alph = ("A", "B", "C", "D", "E", "F", "G", "K", "L")

result = ["A"]

_stroke:str

for x in range(0, len(alph) - 1):
	_stroke = alph[x + 1] + result[x] * 2
	result.append(_stroke)
	print(_stroke)

print(f"===\n{result[8][126:133]}")
