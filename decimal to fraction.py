user = input()
ind = user.index(".")
length = len(user)
n = (length - ind) - 1
up = int(user[:ind] + user[ind + 1:])
do = int("1" + ("0" * n))
if up >= do:
    maxi = up
else:
    maxi = do
r = 2
while r != maxi:
    if up % r == 0 and do % r == 0:
        up = up // r
        do = do // r
    else:
        r += 1
print(f"{up}/{do}")
