""" Королевы бьют друг друга """
def plus_check(strings, colums):
    """ Проверка на вертикаль и горизонталь """
    f_func = 0
    set_str = set(strings)
    set_col = set(colums)
    if len(strings) != len(set_str) or len(colums) != len(set_col):
        f_func = 1
    return f_func

def diag_check(strings, colums, flag):
    """ Функция на проверку диагоналей """
    f_func = 0
    k = 0
    for i in range(0, 8):
        znach = colums[i]
        if znach == 1:
            k = 8-strings[i]
            znach = 2
        else:
            while znach != 1:
                znach = znach - 1
                k += 1
        fin = k
        for j in range(0, fin):
            if znach in colums:
                index1 = colums.index(znach)
                if flag == 1:
                    znach_sr = strings[i] + k
                else:
                    znach_sr = strings[i] - k
                if znach_sr in strings:
                    index2 = strings.index(znach_sr)
                    if index1 == index2:
                        f_func = 1
            znach += 1
            k -= 1
    return f_func

STRINGS = []
COLUMS = []

for l in range(0, 8):
    COORD = input().split()
    COLUMS.append(int(COORD[0]))
    STRINGS.append(int(COORD[1]))

F_PLUS = plus_check(STRINGS, COLUMS)
F_DIAD_G = diag_check(STRINGS, COLUMS, 1)
F_DIAG_P = diag_check(STRINGS, COLUMS, 2)

if (F_DIAG_P or F_PLUS or F_DIAD_G) == 1:
    print("YES")
else:
    print("NO")
