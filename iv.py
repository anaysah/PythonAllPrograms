s1 = input("enter first string")
s2 = input("enter second string")
# s1 = "my&friend&Paul has heavy hats! &"
# s2 = "my friend John has many many friends &"

s1dic = {}
s2dic = {}

for r in s1:
    if r==" " or r.isupper():
        pass
    elif r in s1dic:
        s1dic[r]+=1
    else:
        s1dic[r]=1

for r in s2:
    if r==" " or r.isupper():
        pass
    elif r in s2dic:
        s2dic[r]+=1
    else:
        s2dic[r]=1

st=""

for r in s1dic:
    if not r.lower():
        continue
    elif r in s2dic and s1dic[r]>s2dic[r]:
        st+=str(s1dic[r])+":"+r*s1dic[r]+"/"
    elif r in s2dic and s1dic[r]<s2dic[r]:
        st+=str(s2dic[r])+":"+r*s2dic[r]+"/"
    elif r in s2dic and s1dic[r]==s2dic[r] and s1dic[r]!=1:
        st+="=:"+r*s2dic[r]+"/"
    
    
print(st)