""" Подсчет урона от дробовика """
from math import gcd
COL_DROB = int(input())
CH = []
ZN = []
for i in range(0, COL_DROB):
    CH.append(int(input()))
    ZN.append(int(input()))

MAX_ZN = max(ZN)
NOZ = MAX_ZN
MNOJ = 2
i = 0
FLAG = 1
while FLAG:
    if NOZ % ZN[i] != 0:
        NOZ = MAX_ZN * MNOJ
        MNOJ += 1
        FLAG = 1
    else:
        i += 1
    if i == COL_DROB:
        break
SUM = 0
for i in range(0, COL_DROB):
    SUM += int(NOZ / ZN[i] * CH[i])

ZNACH = gcd(SUM, NOZ)
while ZNACH != 1:
    SUM = int(SUM / ZNACH)
    NOZ = int(NOZ / ZNACH)
    ZNACH = gcd(SUM, NOZ)

print(SUM, "/", NOZ)
