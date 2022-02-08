import sys
SRC = str(sys.argv[1]).lower()
src = []
for x in range(len(SRC)):
	src.append(SRC[x])
def Pal(num):
	center = num / 2
	src_left = src[:int(center)]
	src_right = src[int(center):] if (len(src) % 2) == 0 else src[int(center) + 1:]
	revers = []
	for i in range(len(src_right)):
		revers.append(src_right[len(src_right) - 1 - i])
	return 1 if src_left == revers else 0
print(Pal(len(src)))
