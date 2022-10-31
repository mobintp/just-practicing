# area of Regular polygon.
from math import tan, pi

nSides = int(input('Number of sides: '))
sLength = float(input('Length of sides: '))

pArea = nSides * (sLength ** 2) / (4 * tan(pi / nSides))
print('The area of polygon is: ', pArea)
