n = int(input())
lis=[]
for r in range(n):
    value = input().split(" ")
    extra = list(map(int,value))
    lis.append(extra)

for r in lis:
    x , y= r[1], r[0]
    maxi = max(r)
    mini = min(r)
    if (maxi == x and maxi%2==0) or (maxi == y and maxi%2!=0):
        baseno = (maxi-1)**2
        baseno+= mini
    elif (maxi == x and maxi%2!=0) or (maxi == y and maxi%2==0):
        baseno = (maxi**2)+1
        baseno-= mini
    print(baseno)

