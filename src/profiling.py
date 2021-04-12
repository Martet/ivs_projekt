from mathLib import *
import sys

numbers = sys.stdin.read().split()

N = 0
normSum = 0.0
powSum = 0.0
for x in numbers:
    try:
        x = float(x)
    except:
        continue
    normSum = ADD(normSum, x)
    powSum = ADD(powSum, POW(x, 2))
    N = ADD(N, 1)

if N == 0:
    print(0)
    exit()

average = DIV(normSum, N)
s = SQRT(DIV(SUB(powSum, MUL(N, POW(average, 2))), SUB(N, 1)))

print(s)
