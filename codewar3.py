def decending_order(num):
    st = list(str(num))
    length = len(st)
    maximum = 0
    mainlis= []

    for i in range(length):
        maximum = max(st)
        st.remove(maximum)
        mainlis.append(maximum)
    
    no = ""
    for r in mainlis:
        no+=r
    return int(no)

print(decending_order(42145))


