import pymysql
roll_no=int(input("Enter roll no. = "))
name=input("Enter the name = ")
branch=input("Enter branch = ")

#connect to mysql
cn=pymysql.connect(host="localhost",port=3306,user="root",passwd="",db="payal",autocommit=True)

#create cursor
cur=cn.cursor()

#create sql command
sql1="update studentdata set branch='IT' where roll_no=1001"
sql2="delete from studentdata where roll_no=1004"

print(sql2)
try:
    #send the data to the table
    cur.execute(sql2)

    #check response
    n=cur.rowcount
    if(n==1):
        print("Data saved")
    else:
        print("Data not saved")

except pymysql.err.IntegrityError:
    print("the "+str(roll_no)+" is alredy registered")