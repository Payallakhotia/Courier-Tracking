import pymysql

#connect to my sql
cn=pymysql.connect(host="localhost",port=3306,user="root",passwd="",db="payal",autocommit=True)
#create cursor
cur=cn.cursor()
#create sql command
sql="delete from studentdata where roll_no=1002"
print(sql)

#send data rto table
cur.execute(sql)
#check response
n=cur.rowcount
if(n==1):
    print("data saved")
else:
    print("Data not saved")