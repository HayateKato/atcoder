n = int(input())
d = list()
for i in range(n):
    d.append(int(input()))
d.sort(reverse=True)

current_mochi = d[0]
cnt = 1
for i in range(1,len(d)):
    if d[i] < current_mochi:
        cnt += 1
        current_mochi = d[i]

print(cnt)

