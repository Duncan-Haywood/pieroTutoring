
import math
x = 107.1111111
std = 31.24277694
n = 9
c = 0.90
t = 1.859547
E = t*std/math.sqrt(n)
lower = x - E
upper = x + E
E1 = 2.20
n1 = (t*std/E1)**2
print("E:", E)
print("lower:", lower)
print("upper:", upper)
print("n1:", n1)
