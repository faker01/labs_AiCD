def division(n1, n2):
    while n1 % n2 == 0:
        n1 //= n2
    return n1


n = int(input())

for i in range(1, n + 1):
    if division(division(division(i, 7), 5), 3) == 1:
        print(i)
