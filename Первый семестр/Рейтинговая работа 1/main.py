def y(x:int):
	a = 0
	b = 0
	
	if x < -7:
		a = (76*(x**6) + 50*(x**2) + 21)**8 - 38*(x**8)
		b = (15*(x**3) - (x**3))**7 + (16*(x**2) + 12)**4
		
	elif -7 <= x < -1:
		a = ((37*(x**4) + 80*(x**2) + 92)**5)**0.5 - 55*(x**5)
		b = (59*(x**2))**5 + (25*(x**2) - 38)**6
		
	elif x >= -1:
		a = (5*(x**5) + 78*(x**2) + 75)**6 - 11*(x**5)
		b = (7*(x**6) - (x**3))**5 + ((38*x - 79)**3)**0.5
	
	return a / b


def main():
	with open("source_data.txt", encoding="utf8") as file:
		src = file.read().strip("\n ").split("\n")
		
		for item in range(len(src)):
			src[item] = src[item].replace("x=", "")
	
	result = {}
	for x in src:
		result[x] = y(int(x))
	
	with open("result.txt", "w", encoding="utf8") as file:
		for key, item in result.items():
			if type(item) == complex:
				file.write(f"При x = {key} значение y = {round(item.real, 3) + round(item.imag, 3) * 1j}\n")
			else:
				if "e" in str(item):
					file.write(f"При x = {key} значение y = " + "{:.3e}".format(item) + "\n")
				else:
					file.write(f"При x = {key} значение y = {round(item, 3)}\n")


if __name__ == '__main__':
	main()