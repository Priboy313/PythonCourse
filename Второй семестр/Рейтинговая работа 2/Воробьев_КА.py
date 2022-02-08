
def get_source_data(src_url:str):
	with open(src_url, "r", encoding="utf-8") as file:
		src = file.read().split("\n")
		return src


def get_quotient(src_data:list):
	_src_fio = src_data[0].replace(" ", "")
	return int(src_data[1]) // len(_src_fio)


def get_unicode_list(src_string:str):
	_unicode_list:list = []
	_src = src_string.replace(" ", "")
	
	for i in range(0, len(_src)):
		_unicode_list.append(ord(_src[i]))
	
	return _unicode_list


def sort_ascending(src_unicode_list:list):
	"""Сортировка по возрастанию"""
	_sorted_list = []
	_quo_parity = "чётное"
	_sorted_type = "по возрастанию"
	return _sorted_list, _quo_parity, _sorted_type


def sort_descending(src_unicode_list:list):
	"""Сортировка по убыванию"""
	_sorted_list = []
	_quo_parity = "нечётное"
	_sorted_type = "по убыванию"
	return _sorted_list, _quo_parity, _sorted_type


def get_average(src_list:list):
	"""Среднее арифметическое"""
	_sum = 0
	
	for i in range(0, len(src_list)):
		_sum += int(src_list[i])
	
	return round(_sum / len(src_list), 3)


def get_square(src_list:list):
	"""Среднее квадратическое"""
	_sum = 0
	
	for i in range(0, len(src_list)):
		_sum += src_list[i]**2
	
	return round((_sum / len(src_list))**0.5, 3)


def main():
	src_data = get_source_data("source_data.txt")
	quotient = get_quotient(src_data)
	unicode_list = get_unicode_list(src_data[0])
	sorted_list, quo_parity, sorted_type = sort_ascending(unicode_list) if quotient % 2 == 0 else sort_descending(unicode_list)
	average = get_average(unicode_list)
	square = get_square(unicode_list)
	
	with open("result.txt", "w", encoding="utf-8") as file:
		file.write(
f"""1. Исходные данные: {src_data[0]}; ID: {src_data[1]}
2. {quotient}
3. Направление сортировки: {sorted_type}, так как число {quotient} - {quo_parity}
4. Набор данных: {unicode_list}
5. Отсортированный {sorted_type} набор данных {sorted_list}
6. Среднее арифметическое значение: {average}
7. Среднее квадратическое значение: {square}""")
	
	# print(f"\n{src_data = }\n{quotient = }\n{unicode_list = }\n{sorted_list = }\n{quo_parity = }\n{sorted_type = }")


if __name__=='__main__':
	main()
