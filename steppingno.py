def stepping(user):
    user = str(user)
    length = len(user)
    sp = 0
    i = 0
    for r in range(length - 1):
        sp = int(user[r]) - int(user[r + 1])
        if sp == 1 or sp == -1:
            i += 1
    if i == length - 1:
        return True
    else:
        return False

print(stepping(int(input("enterhere:"))))
