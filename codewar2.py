lis = [3,9,1,0,4,7]
length = len(lis)
for r in range(length//2):
    if r<lis[(length-1)-r]:
        lis[r],lis[length-1] = lis[length-1],lis[r]


print(lis)