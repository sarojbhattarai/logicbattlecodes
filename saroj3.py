import sys
import math
a = int(input("enter number of test cases"))
for i in range(0,a):
    x = input().split()
    a = int (x[0])
    b = int (x[1])
    c = int (x[2])
    d = a ** b
g = 0
for i in range (0,100000):
    g = i * c
    for k in range(0,a):
        if (((d-g) == 0) or ((d-g)<=c)):
            print(i*c)
            break
