user = [3, 5, 2, 9, 1, 6, 7]
length = len(user)
dic = {}
lis = []
for r in user:
    i = 0
    for z in user:
        if r > z:
            i += 1
    dic[i] = r
for k in range(length):
    lis.append(dic[k])
print(lis)
