""" Вывод делителей числа N """
while True:
    NUM = int(input())
    if NUM < 1000000:
        break
k = 0
for i in range(1, NUM+1):
    if NUM % i == 0:
        k += 1
        print(i, end=' ')
if k == 2:
    print("\nACHTUNG")
