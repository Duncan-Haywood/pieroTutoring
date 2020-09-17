import math 
import numpy as np
data1 = [115,85,80,90,75,50,30,23,100,110,105,95,105,60,110,120,95,90,60,70,115,85,80,90,75,50,30,23,100,110,105,95,105,60,110,120,95,90,60,70]
data = [1264,	1285,	1257,	1243,	1268,	1316,	1275,	1317,	1275]
mean = np.mean(data1)
var = np.var(data1)
n = len(data1)
std = math.sqrt(var)
print("mean:", mean)
print("std:", std)
