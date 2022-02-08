import sys

item = str(sys.argv[1])

result = ''
while item:
	item, last3= item[:-3], item[-3:]
	result=(last3 + ' ' + result) if result else last3


print(result)
