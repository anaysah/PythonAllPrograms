import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  password="ajay9212",
  user="root",
  database="test"
)
mycursor = mydb.cursor()
print("first choose what you want to do login or sing up")
def whattodo():
    global user
    user = input("enter here:")
    if user!="login" and user!="signup":
        print("pls enter only signup or login ")
        whattodo()

whattodo()
def userinfo():
    global name, password
    name = input("enter here your name:")
    password = input("enter here your password:")
    if name=="" or password=="":
        userinfo()

userinfo()

if user=="signup":
    mycursor.execute(f"insert into student (name,password) values('{name}','{password}')")
    print("you signed up sucessfully")


if user=="login":
    while True :
        mycursor.execute(f"select * from student where name='{name}'")
        result = mycursor.fetchall()
        if result==[]:
            print("pls enter user name again")
            userinfo()
            continue
        elif password==result[0][2]:
            print("you logged in")
            break 
        else:
            print("password is wrong")
            password = input("enter here your password:")
            continue
    
mydb.commit()




