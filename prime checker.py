user = int(input("Enter No here:"))
i = 0
for r in range(1,user+1):
    if user%r==0:
        i+=1
if i>2:
    print("not prime")
else:
    print("Yes it is prime")
