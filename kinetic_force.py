import sys

mass = sys.argv[1]
speed = sys.argv[2]

force = (float(mass) * (float(speed) ** 2)) / 2

print(force)
