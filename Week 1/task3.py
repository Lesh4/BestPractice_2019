""" Необычные шахматы от BPS """
while True:
    COL_1 = int(input())
    STR_1 = int(input())
    COL_2 = int(input())
    STR_2 = int(input())
    if COL_1 > 0 and STR_1 > 0 and COL_2 > 0 and STR_2 > 0:
        break
if ((COL_1 + 2 == COL_2 and STR_1 + 5 == STR_2) or (COL_1 + 5 == COL_2 and STR_1 + 2 == STR_2)):
    print("YESSSS!")
elif ((COL_2 + 2 == COL_1 and STR_2 + 5 == STR_1) or (COL_2 + 5 == COL_1 and STR_2 + 2 == STR_1)):
    print("YESSSS!")
else:
    print("No no")
