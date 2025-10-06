s = input()
conutl =0
countr =0
ans = []
temp = ""
for ch in s:
    temp+=ch
    if ch =='L':
        conutl =  conutl+1
    else:
        countr = countr+1
    if conutl == countr:
        ans.append(temp)
        temp = ""
        conutl =0
        countr =0
print(len(ans))
for i in ans:
    print(i)
