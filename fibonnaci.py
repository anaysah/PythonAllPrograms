lis = [0,1]
n = 10
for r in range(n-2):
    m = lis[r]+lis[r+1]
    lis.append(m)

print(lis)
