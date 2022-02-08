def pot_en(m, v1):
	v2 = 2 #m/c
	E = -((m*v2**2)/2 - ((m*v1**2)/2))
	return E
print(round(pot_en(1,4)))