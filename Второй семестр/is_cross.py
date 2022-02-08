from math import *

def is_cross(cir1:list, cir2:list):
	dist = sqrt((cir2[0]-cir1[0])**2+(cir2[1]-cir1[1])**2)

	if cir1[2] + cir2[2] >= dist:
		return True
	else: return False



print(is_cross([5, 0, 1], [0, 0, 3]))