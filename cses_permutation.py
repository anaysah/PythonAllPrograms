def permu(n):
    lis1 = []
    lis2 = []
    if n==2 or n==3:
        return "NO SOLUTION"
    for r in range(1,n+1):
        if r%2!=0:
            lis1.append(str(r))
        elif r%2==0:
            lis2.append(str(r))
    return " ".join(lis2+lis1)

print(permu(int(input())))