#
n = int(input("enter here n"))
lis = []
for r in range(n):
    value = input()
    lis.append(value)

obje = {}
mainlist = []
maximun = 0
for data in lis:
    newlis = data.split(" ")
    if newlis[0] not in obje:
        obje[newlis[0]] = int(newlis[1])
        mainlist.append(data)
    else:
        obje[newlis[0]] += int(newlis[1])
        mainlist.append(data)

    lastlist = obje.values()
    m = max(lastlist)
    if m > maximun:
        mainlist.remove(data)
        mainlist.insert(0,data)
            
    maximun = m
  
print("ans",mainlist[0])


