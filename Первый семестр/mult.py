import sys

SCR = sys.argv[1]

for i in range(1, 10):
    result = f"{SCR} x {i} = {int(SCR) * int(i)}"
    print(result)
