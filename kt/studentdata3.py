import pymysql

roll_no=int(input("Enter the roll no. = "))
name=input("Enter the name = ")
branch=input("Enter the branch = ")

#connect to mysql
cn=pymysql.connect(host="localhost",port=3306,user="root",passwd="",db="payal",autocommit=True)

#create cursor
cur=cn.cursor()

#create sql command
sql="insert into studentdata values("+str(roll_no)+",'"+name+"','"+branch+"')"
print(sql)

#send data to table
cur.execute(sql)

#check response
n=cur.rowcount
if(n==1):
    print("Data saved")
else:
    print("Data not saved")