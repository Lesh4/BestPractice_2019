""" Топ букв в строке """
import string
TOP = {}
WORDS = str(input())
WORDS = WORDS.translate(str.maketrans('', '', string.punctuation))
LETTERS = WORDS.replace(" ", "").lower()
for LETTER in LETTERS:
    if LETTER not in TOP.keys():
        TOP[LETTER] = 1
    else:
        TOP[LETTER] += 1
LIST_VAL = list(TOP.items())
LIST_VAL.sort(key=lambda i: i[1], reverse=True)

for i in range(0, len(LIST_VAL)-1):
    for j in range(0, len(LIST_VAL)-1-i):
        if LIST_VAL[j][1] == LIST_VAL[j+1][1]:
            if LIST_VAL[j][0] > LIST_VAL[j+1][0]:
                VAR = LIST_VAL[j]
                LIST_VAL[j] = LIST_VAL[j+1]
                LIST_VAL[j+1] = VAR
for i in LIST_VAL:
    print(i[0], ':', i[1])
