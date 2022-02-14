
def get_source_data(src_url:str):
	with open(src_url, "r", encoding="utf-8") as file:
		_src = file.read().split("\n")
		return _src


def get_quotient(src_data:list):
	"""Вычисление частного от деления ID на количество букв в ФИО без учёта пробелов"""
	_src_fio = src_data[0].replace(" ", "")
	return int(src_data[1]) // len(_src_fio)


def get_unicode_list(src_string:str):
	"""Получение списка символов ФИО в кодировке Юникод"""
	_unicode_list:list = []
	_src = src_string.replace(" ", "")
	
	for i in range(0, len(_src)):
		_unicode_list.append(ord(_src[i]))
	
	return _unicode_list


def merge(left, right):
	"""Функция слияния частей массивов для сортировки Слиянием"""
	_sorted_list = []
	l_index = r_index = 0
	l_len, r_len = len(left), len(right)
	
	for i in range(l_len + r_len):
		if l_index < l_len and r_index < r_len:
			if left[l_index] <= right[r_index]:
				_sorted_list.append(left[l_index])
				l_index += 1
			else:
				_sorted_list.append(right[r_index])
				r_index += 1
		elif l_index == l_len:
			_sorted_list.append(right[r_index])
			r_index += 1
		elif r_index == r_len:
			_sorted_list.append(left[l_index])
			l_index += 1
	return _sorted_list


def merge_sort(src_unicode_list:list):
	"""Сортировка слиянием"""
	_list = src_unicode_list.copy()
	
	if len(_list) == 1 or len(_list) == 0:
		return _list
	
	left = merge_sort( _list[:len(_list) // 2])
	right = merge_sort(_list[len(_list) // 2:])
	
	return merge(left, right)


def bubble_sort(src_unicode_list:list):
	"""Сортировка пузырьком"""
	_sorted_list = src_unicode_list.copy()
	
	for i in range(len(_sorted_list)-1):
		for j in range(len(_sorted_list)-1):
			if _sorted_list[j] > _sorted_list[j+1]:
				_sorted_list[j], _sorted_list[j+1] = _sorted_list[j+1], _sorted_list[j]
	
	return _sorted_list


def sort_ascending(src_unicode_list:list):
	"""Сортировка по возрастанию"""
	_sorted_list = bubble_sort(src_unicode_list)
	_quo_parity = "чётное"
	_sorted_type = "по возрастанию"
	return _sorted_list, _quo_parity, _sorted_type


def sort_descending(src_unicode_list:list):
	"""Сортировка по убыванию"""
	_sorted_list = merge_sort(src_unicode_list)
	_quo_parity = "нечётное"
	_sorted_type = "по убыванию"
	return _sorted_list[::-1], _quo_parity, _sorted_type


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
		_sum += int(src_list[i])**2
	
	return round((_sum / len(src_list))**0.5, 3)


def main():
	src_data = get_source_data("source_data.txt")
	quotient = get_quotient(src_data)
	unicode_list = get_unicode_list(src_data[0])
	sorted_list, quo_parity, sorted_type = sort_ascending(unicode_list) if quotient % 2 == 0 else sort_descending(unicode_list)
	average = get_average(unicode_list)
	square = get_square(unicode_list)
	
	with open("result.txt", "w", encoding="utf-8") as file:
		file.write(f"""
1. Исходные данные: {src_data[0]}; ID: {src_data[1]}
2. {quotient}
3. Направление сортировки: {sorted_type}, так как число {quotient} - {quo_parity}
4. Набор данных: {unicode_list}
5. Отсортированный {sorted_type} набор данных: {sorted_list}
6. Среднее арифметическое значение: {average}
7. Среднее квадратическое значение: {square}"""[1:])
	

if __name__=='__main__':
	main()
