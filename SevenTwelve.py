from math import sqrt
xbar1 = 61.8
xbar2 = 69.0 
s1 = 8.35
s2 = 12.9
n1 = 9640
n2 = 23351
xp = (xbar1-xbar2)
Z = 2.58  
E = Z*sqrt(s1**2/n1+s2**2/n2)

lower = xp - E
upper = xp + E

print("lower:", lower)
print("upper:", upper)

