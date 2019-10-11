""" Программа, которая проверяет, является ли скобочная последовательность правильной """
from collections import deque
DICT_SEQ = {'{':'}', '(':')', '[':']'}
SEQUENCE = []
N = int(input())
for i in range(N):
    STRING = deque(str(input()))
    SEQUENCE.append(STRING)
for STEK in SEQUENCE:
    if len(STEK) % 2 != 0:
        print('no')
    else:
        f = 0
        while len(STEK) != 0:
            for KEY in DICT_SEQ:
                if len(STEK) == 0:
                    break
                if STEK[0] == KEY:
                    if STEK[len(STEK)-1] == DICT_SEQ[KEY]:
                        STEK.pop()
                        STEK.popleft()
                        f = 1
                    else:
                        f = 0
                        break
            if f == 0:
                break
    if f:
        print("yes")
    else:
        print("no")
