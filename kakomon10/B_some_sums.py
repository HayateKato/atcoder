n,a,b = [int(x) for x in input().split()]

ans = 0
for i in range(1,n+1):
    tmp = i
    dig = list()
    while tmp > 0:
        dig.append(tmp % 10)
        tmp //= 10
    
    dig_sum = 0
    for k in dig:
       dig_sum += k
    if a <= dig_sum <= b:
        ans += i
     
print(ans)
