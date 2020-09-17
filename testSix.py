import math
n = 132
p = 0.37
mu = n*p
q = (1-p)
std = math.sqrt(n*p*q)
x = 45
z = (x-mu)/std
xL = x - 0.5      
zL = (xL-mu)/std
xR = x + 0.5      
zR = (xR-mu)/std
deltaZ = zR-zL
print("mu:", mu)
print("std:", std)
print("x:", x)
print("z:", z)
print("xL:", xL)
print("zL:", zL)
print("xR:", xR)
print("zR:", zR)
print("deltaZ:", deltaZ)
