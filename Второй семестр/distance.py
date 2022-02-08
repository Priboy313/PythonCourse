import math

def distance(item1, item2):
	if len(item1) == 2 and len(item2) == 2:
		return math.sqrt((item2[0]-item1[0])**2 + (item2[1]-item1[1])**2)
	else:
		return math.sqrt((item2[0]-item1[0])**2 + (item2[1]-item1[1])**2 + (item2[2]-item1[2])**2)
	
	
	
print(distance((-1, 3), (6, 2)))
print(distance((-1, 3, 3), (6, 2, -2)))