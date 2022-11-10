def removeall(z,lis):
    i=0
    for r in lis:
        if z == r:
            del lis[i]
        i+=1
    return lis
print(removeall(2,[2,5,6,3,8,7,9,0,1,5,2]))

        
