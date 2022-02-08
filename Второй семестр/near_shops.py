from math import *

def near_shops(startxy:tuple, radius, shops:list):
	_result = []
	
	for i in range(0, len(shops)):
		shop = shops[i]
		dist = sqrt((shop[1][0]-startxy[0])**2 + (shop[1][1]-startxy[1])**2)
		
		if dist <= radius:
			_result.append((shop[0], dist))
	
	result = sorted(_result, key=lambda x: x[1])
	
	return result


# _shops = [
#     ("Магазин 1", (1, 1)),
#     ("Магазин 2", (-1, 0)),
#     ("Магазин 3", (2, -1)),
#     ("Магазин 4", (2, 4)),
#     ("Магазин 5", (2, 0)),
# ]
#
# print(near_shops(startxy=(2,3), radius=3,shops=_shops))