import math 
n = 500

x = 291

p = x / n 

q = 1 - p



alpha = 1 - 0.99

alphaHalf = alpha / 2
z  = 2.576
E = z*math.sqrt(p*q/n)
lower = p - E
upper = p + E


print("E:", E)
print("lower:", lower)
print("upper:", upper)



