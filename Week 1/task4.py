""" Проверка на вертикаль и горизонталь """
def plus_check(strings, colums):   
    f = 0
    SET_STR = set(strings)
    SET_COL = set(colums)
    if len(strings) != len(SET_STR) or len(colums) != len(SET_COL):
        f = 1
    return f
        

""" Функция на проверку диагоналей """
def diag_check(STRINGS, COLUMS, flag):
    f = 0
    k = 0
    for i in range(0,2):
        ZNACH = COLUMS[i]
        if ZNACH == 1:
            k = 8-STRINGS[i]
            ZNACH = 2
        else:
            while ZNACH != 1:
                ZNACH = ZNACH - 1
                k+=1
        FIN = k                        #k = 1
        for j in range(0, FIN):
            if ZNACH in COLUMS:
                INDEX1 = COLUMS.index(ZNACH)  
                if flag == 1:
                    ZNACH_SR = STRINGS[i] + k  
                else:
                    ZNACH_SR = STRINGS[i] - k    
                if ZNACH_SR in STRINGS:
                    INDEX2 = STRINGS.index(ZNACH_SR)
                    if INDEX1 == INDEX2:
                        f = 1
            ZNACH += 1
            k -= 1
    return f

STRINGS = []
COLUMS = []

for i in range(0,2):
    COLUMS.append(int(input()))
    STRINGS.append(int(input()))

f_plus = plus_check(STRINGS, COLUMS)
f_diag_g = diag_check(STRINGS, COLUMS, 1) 
f_diag_p = diag_check(STRINGS, COLUMS, 2) 

if (f_diag_p or f_plus or f_diag_g) == 1:
    print("YES")
else:
    print("NO")