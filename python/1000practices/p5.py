# wind chill.
import math 
v = float(input('Input wind speed in k/h: '))
t = float(input('Input air temperature in degree celsius: '))
wci = 13.12 + .6215*t - 11.37*math.pow(v, .16) + .3965*t*math.pow(v, .16)

print('The wind chill index is: ', int(round(wci, 1))) 