def square_digits(num):
    st = str(num)
    newst = ""
    for r in st:
        newst+= str(int(r)**2)
    return newst

print(square_digits("6789"))