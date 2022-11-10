user = input("Enter you string here:")

lis = user.split()
size = len(lis)
lis2 = {}

for r in lis:
    for i in r:
        if i.isdigit():
            lis2[int(i)]=r
            break

st = ""
for r in range(1,size+1):
    print(lis2[r],end=" ")
