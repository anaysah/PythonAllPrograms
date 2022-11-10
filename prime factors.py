user = int(input())
i = 2
lis = []
while True:
    if user == 1:
        break
    elif user % i == 0:
        user = user // i
        lis.append(i)
    elif user % i != 0:
        i += 1
print(lis)