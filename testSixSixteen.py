import math
n = 40
mu = 30
std = 9
x = 33
stde = std/math.sqrt(n)
zx = (x - mu)/stde
z = (x - mu)/std
print("n:", n)
print("x:", x)
print("mu:", mu)
print("std:", std)
print("stde:", stde)
print("zx:", zx)
print("z:", z)
