import pymysql
roll_no=int(input("enter the roll no"))
name=input("enter the name")
branch=input("enter the branch")


#connect to  mysql
cn=pymysql.connect(host="localhost",port=3306,user="root",passwd="",db="payal",autocommit=True)
#ceate cursor
cur=cn.cursor()
#create sql command
sql="update studentdata set name='D' where roll_no=1002"
print(sql)


#send data to table
cur.execute(sql)
#check response
n=cur.rowcount
if(n==1):
    print("Data saved")
else:
    print("data not saved")
