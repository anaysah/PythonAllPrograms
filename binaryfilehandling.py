import pickle
f = open("bi.txt","wb+")
pickle.dump(3,f)
pickle.dump("dhdjd3",f)
pickle.dump(["dhdjd3",34,67],f)
f.seek(0)
while True:
    try:
        print(pickle.load(f))
    except:
        break
f.close()

