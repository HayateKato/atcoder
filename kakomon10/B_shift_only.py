n = int(input())
a = [int(i) for i in input().split()]

ans = 0
flag = True
while flag:
    for i in range(n):
        if a[i] % 2 == 0:
            a[i] //= 2
        else:
            flag = False
            print(ans)
            break
    ans += 1