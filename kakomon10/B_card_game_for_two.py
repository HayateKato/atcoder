n = int(input())
a = [int(x) for x in input().split()]

a.sort(reverse=True)
alice = bob = 0
for i in range(len(a)):
    if i % 2 == 0:
        alice += a[i]
    else:
        bob += a[i]

print(alice - bob)