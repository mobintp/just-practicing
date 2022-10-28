# volume and area of a cylinder.
pi = 22 / 7
height = float(input('Height of cylinder: '))
radius = float(input('Radius of cylinder: '))
volume = pi * height * radius ** 2
surArea = 2 * pi * radius * height + 2 * pi * radius ** 2
print('Volume is: ', volume, '\n', 'surface Area is: ', surArea)
