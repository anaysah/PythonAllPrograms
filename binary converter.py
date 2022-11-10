user= int(input("enter input"))
bi = ""
while user>0:
    x=user%2
    bi+=str(x)
    user//=2
print(bi[::-1])
input()
