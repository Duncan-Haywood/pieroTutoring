
import math
r1 = 296
n1 = 364
r2 = 34
n2 = 562
p1 = r1/n1
p2 = r2/n2
q1 = 1 - p1
q2 = 1 - p2
pp = p1-p2

c = 0.95
alpha = 1-c
alphahalf = alpha/2
zalphahalf = 1.96
sep = math.sqrt((p1*q1/n1)+(p2*q2/n2))

E = zalphahalf*sep


lower = pp - E
upper = pp + E

print("pp:", pp)
print("p1:", p1)
print("p2:", p2)
print("zalphahalf:", zalphahalf)
print("sep:", sep)
print("E:", E)
print("lower:", lower)
print("upper:", upper)

