def remake(user):
    for r in user:
        for z in range(len(user)):
            if user.index(r) == z:
                continue
            elif r==user[z]:
                del user[z]
    return user
print( remake([2,3,5,6,7,2,3,3]) )

