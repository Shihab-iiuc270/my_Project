
n = int(input())
lst = list(map(int, input().split()))

counter = {}
for i in lst:
    if i in counter:
        counter[i] += 1
    else:
        counter[i] = 1

total = 0
for x,cnt in counter.items():
    if cnt < x:
        total += cnt
    elif cnt > x:
        total += cnt -x
print(total)
