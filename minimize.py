n = int(input())
lst = list(map(int, input().split()))
count = 0
while  True:
    odd = False
    for i in range(n):
        if lst[i]%2 == 0:
            lst[i] = lst[i]//2
        else: 
            odd = True
            break
    if odd == False:
        count+=1
    else: break
     

print(count)