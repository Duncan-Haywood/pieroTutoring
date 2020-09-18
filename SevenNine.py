
import math 
x1 = 259.6190
s1 = 12.2331
x2 = 205.8947
s2 = 12.7797
n1 = 21
n2 = 19
xp = x1-x2

c = 0.99
alpha = 0.01

df = n1 + n2 -2
sp = math.sqrt(((n1-1)*s1**2+(n2-1)*s2**2)/df)
t = 2.7116

E = t*sp*math.sqrt((1/n1)+(1/n2))

lower = xp - E
upper = xp + E

print("xp:", xp)
print("df:", df)
print("sp:", sp)
print("t:", t)
print("E:", E)
print("lower:", lower)
print("upper:", upper)

