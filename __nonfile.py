alph = ['А', 'а', 'Б', 'б', 'В', 'в', 'Г', 'г', 'Д', 'д',
		'Е', 'е', 'Ё', 'ё', 'Ж', 'ж', 'З', 'з', 'И', 'и',
		'Й', 'й', 'К', 'к', 'Л', 'л', 'М', 'м', 'Н', 'н',
		'О', 'о', 'П', 'п', 'Р', 'р', 'С', 'с', 'Т', 'т',
		'У', 'у', 'Ф', 'ф', 'Х', 'х', 'Ц', 'ц', 'Ч', 'ч',
		'Ш', 'ш', 'Щ', 'щ', 'Ъ', 'ъ', 'Ы', 'ы', 'Ь', 'ь',
		'Э', 'э', 'Ю', 'ю', 'Я', 'я', '.', ' ', '!', '?']


OFFSET = 5


def set_mode():
	_inp = input("Code (1) or Decode (2)?\n")
	
	match _inp:
		case "1" | "Code":
			_inp = "Code"
		case "2" | "Decode":
			_inp = "Decode"
		case _:
			quit()
	
	return _inp

def main():
	_mode = set_mode()
	
	match _mode:
		case "Code":
			
	
	
	print(len(alph))



if __name__ == "__main__":
	main()


