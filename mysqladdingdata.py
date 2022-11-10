import mysql.connector
mydb = mysql.connector.connect(host="localhost",user="root",database="SIKKIM")
how,n = int(input("Enter how many ROWS you want to add:")),1
mycursor = mydb.cursor()
def data():
    global year,Population,SexRatio,GrowthRate,lis
    year = int(input("Enter Year here:"))
    Population = int(input("Enter Population here:"))
    SexRatio = int(input("Enter SexRatio here:"))
    GrowthRate = float(input("Enter GrowthRate here:"))
    lis = [year,Population,SexRatio,GrowthRate]
while n<=how:
    data()
    if len(lis)==4 and len(str(lis[0]))==4:
        mycursor.execute(
            f"INSERT INTO census_population(Years,Population,Sex_Ratio,GrothRate) VALUES({year},{Population},{SexRatio},{GrowthRate})")
        print("added succesfully now add next rows if any")
        n+=1
    else:
        print("some details are wrong pls enter them again")
        data()
mydb.commit()
