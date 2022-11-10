def isEmpty():
    if  st==[]:
        return True
    else:
        return False

def Push(item):
    st.append(item)

def Pop():
    if isEmpty():
        print("the stack is empty")
    else:
        print("the deleted item is",st.pop())

def Display():
    if isEmpty():
        print("the Stack is empty")
    else:
        l = len(st)-1
        for r in range(l,-1,-1):
            print(st[r])


st = []
top = 0
while True:
    print("1. Push")
    print("2. Pop")
    print("3. Display")
    print("0. Exit")
    op = int(input("enter here:"))
    if op==1:
        value = input("enter any no")
        Push(value)
    elif op==2:
        Pop()
    elif op==3:
        Display()
    elif op==0:
        break
    else:
        print("you entered input wrong no")
