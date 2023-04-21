import mysql.connector as sqluser
con=sqluser.connect(host='localhost',user='root',passwd='root')

cur=con.cursor()
cur.execute('create database tn')
cur.execute('use tn')

cur.execute('create table employee(EID INT PRIMARY KEY, ENAME VARCHAR(20), PWD VARCHAR(20), DOJ VARCHAR(10), JOB VARCHAR(15), SAL INT)')

print("Employee data")
print()
print("1. Login")
print("2. Register New User")
print()

ans = int(input("Choose option(1, 2, or any other number to exit)):"))

while ans == 1 or ans == 2:
    print()
    if ans == 2:
        try:
            cur.reset()
            cur.execute("select max(EID) from employee")
            data = cur.fetchone()
            EID = str(data[0] + 1)
        except:
            EID = 1001
        print("Your EID is",EID)
        ENAME = input("Enter name:")
        PWD = input("Create new password:")
        DOJ = input("Date of Joining (YYYY-MM-DD):")
        JOB = input("Enter job:")
        SAL = int(input("Enter salary:"))
        insert = "INSERT INTO employee (EID,ENAME,PWD,DOJ,JOB,SAL) VALUES (%s,'%s','%s','%s','%s',%s)"%(EID,ENAME,PWD,DOJ,JOB,SAL)
        cur.execute(insert)
        con.commit()
        print("Account created!")
        print()
    elif ans == 1:
        cur.reset()
        EID = int(input("Enter EID:"))
        print()
        sel = "select EID from employee where EID = %s"%(EID)
        cur.execute(sel)
        data = cur.fetchall()
        if cur.rowcount == 0:
            print("EID not found!")
            print()
        else:
            cur.reset()
            sel2 = "select * from employee where EID = %s"%(EID)
            cur.execute(sel2)
            data = cur.fetchall()
            for row in data:
                print("EID:",row[0])
                print("ENAME:",row[1])
                print("PWD:",row[2])
                print("DOJ:",row[3])
                print("JOB:",row[4])
                print("SAL:",row[5])
            print()
                
    ans = int(input("Choose option(1, 2, or any other number to exit)):"))

print()
database=sqluser.connect(host='localhost',user='root',passwd='root')

mycur=database.cursor()
mycur.execute('use tn')
mycur.execute('create table airport(Destination varchar(15), Flight varchar(15),Time time primary key,Price integer)')


st='''insert into airport(Destination,Flight,Time,Price) values
    ('Chennai','Indigo(997)','1:05:00',4312),
    ('Delhi','Air India(320)','3:48:00',3299),
    ('Lucknow','Air India(333)','5:55:00',4612),
    ('Goa','Go-Air(4045)','9:51:00',4713),
    ('Kochi','Vistara(644)','11:59:00',3755),
    ('Kolkata','Go-Air(002)','12:06:00',3121),
    ('Jaipur','Go-Air(123)','15:23:00',3817),
    ('Mumbai','Indigo(654)','17:23:00',4214),
    ('Oman','Emirates(345)','19:08:00',15712),
    ('Bikaner','Indigo(412)','20:05:00',5832),
    ('Chandigarh','Indigo(656)','22:55:00',4532)'''

mycur.execute(st)
database.commit()
    


print ("WELCOME TO OUR AIRPORT".center(70))
print ("="*60)
print()
print ("Flight ticket booking".center(70))
print()
print ("="*60)
print()
print()
print ("Enter any key to book tickets")
enter = input()
print()


from tabulate import tabulate

database=sqluser.connect(host='localhost',user='root',passwd='root',database='tn')
cursor=database.cursor()
cursor.execute('Select * from airport')
data=cursor.fetchall()
info=[]

for i in data:
    info.append([i[0],i[1],i[2],i[3]])

print(tabulate(info))

print()

print("Enter flight details:")
a=int(input("Enter number of passengers: "))
b=str(input("Enter names of passengers: "))
c=str(input("Enter age of passengers(seperated by commas): "))
d=str(input("Enter destination: "))
e=str(input("Enter date and time[DD/MM/YY format]: "))
f=str(input("Enter name of flight: "))
print(input("Press any key to book the ticket :"))
print("Click on link to complete payments _____")
input("Enter any key to print tickets: ")
print()
print("-"*60)
print("TICKET".center(70))
print()
print("Number of passengers is:")
print(a)
print("\nNames of passengers are:")
print(b)
print("\nAge of passengers are:")
print(c)
print("\nFlight destination is:")
print(d)
print("\nDate and time of flight are:")
print(e)
print("\nFlight name is:")
print(f)
print()
print()
print("Kindly carry a printout of this image".center(70))
print("-"*60)
        