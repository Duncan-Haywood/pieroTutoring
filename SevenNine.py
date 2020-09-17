import math 
x1 = 259.6190
s1 = 12.2331
x2 = 205.8947
s2 = 12.7797
n1 = 21
n2 = 19


df = n1 + n2 -2
sp = math.sqrt(((n1-1)*s1**2+(n2-1)*s2**2)/df)
print("sp:", sp)
