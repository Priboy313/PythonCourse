l1 = [1, 2, 3]
l2 = [4, 5, 6]

l3 = [1, 2, 3]
l4 = [4, 5]

# def mymap(func, *lists) -> list:
# 	_lists = sorted(lists, key=len)
# 	result = []
#
# 	for x in range(0, len(_lists[0])):
# 		result.append(func(_lists[0][x], _lists[1][x]))
#
# 	return result


def mymap(func, *args) -> list:
	match len(args):
		case 2:
			_result = map(func, args[0], args[1])
		case _:
			_result = map(func, args[0])
	
	return list(_result)


print(mymap(lambda x, y: x + y, l2, l1))
print(mymap(lambda x, y: x + y, l3, l4))


