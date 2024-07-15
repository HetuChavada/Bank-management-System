import mysql.connector

conn =mysql.connector.connect(host="localhost", user="root", password="" , autocommit=True)
my_cursor=conn.cursor()
my_cursor.execute("create database if not exists bank_database")
my_cursor.execute("use bank_database")
my_cursor.execute("create table if not exists login(acc_no int primary key auto_increment, name varchar(30), city varchar(20), mobile_no varchar(10), balance int(6))")


print("1.Admin Panel \n 2.User panel ")
choicemenu = int(input("Enter your choice :"))

if choicemenu==1:
    my_cursor.execute("insert into login values('MANAGER','mngr@123)")
    my_cursor.execute("insert into login values('HEAD','hod@123)")

elif choicemenu==2:
     my_cursor.execute("insert into login values('','bank@123)")
   #  my_cursor.execute("insert into login values('HEAD','bank@)")


else:
    print("Try Again")

#create tables 
my_cursor.execute(
    "create table if not exists bank_account(acc_no int primary key auto_increment, name varchar(30), city varchar(20), mobile_no varchar(10), balance int(6))")

my_cursor.execute(
    "create table if not exists transaction(acc_no int, amount int(6),ttype varchar(10),foreign key (acc_no) references bank_account(acc_no))")

print("---------------------------Welcome to the world bank------------------------------")

while True:
    print("1.create Account \n 2.Deposit Money \n 3.Withdraw Money \n 4.View Account details \n 5.close account \n 6.exit"  )
    ch = int(input("Enter Your choice :"))

    #create new account

    if ch==1:
        name = input("Enter your name :")
        city = input("Enter city name :")
        mn = input("Enter mobile number :")
        balance = 0
        sql = "insert into bank_account(name,city,mobile_no,balance) values (%s, %s, %s, %s)"
        val = (name,city,mn,balance)
        my_cursor.execute(sql,val)
        my_cursor.execute("select * from bank_account where name=' " +name + " ' ")
        print("Account created successfully !")

        for i in my_cursor:
            print(i)

    #deposit money 

    elif ch==2:
        accno = input("Enter Account Number :")
        dp = int(input("Enter Amount to be deposited :"))
        ttype = "Deposit"
        my_cursor.execute("insert into transaction values(' " + accno + " ', '" + str(dp) + " ', ' " + ttype + " ')")
        my_cursor.execute("update bank_account set balance=balance+'" + str(dp) + " ' where acc_no=' " + accno + " ' ")
        print("Rs."  , dp , " has been deposited successfully in Account :" , accno)

    elif ch==3:
        accno = input("Enter Account Number :")
        wd = int(input("Enter Amount to be withdrawn :"))
        select_Query = "select balance from bank_account where acc_no = ' " + accno + " ' "
        my_cursor.execute(select_Query)
        bal = my_cursor.fetchone()[0]

        if wd < bal:
            ttype = "withdraw"
            my_cursor.execute("insert into transaction values(' " + accno + " ', '" + str(wd) + " ', ' " +ttype + " ')")
            my_cursor.execute("update bank_account set balance=balance-'" +str(wd) + " ' where acc_no=' " +accno + " ' ")
            print("Rs."  , wd , " has been withdrawn successfully in Account :" , accno)

        else:
            print("Insufficient Balance !")

    elif ch==4:
        accno = input("Enter Account Number :")
        my_cursor.execute("select * from bank_account where acc_no=' "+ accno + " ' ")
        for i in my_cursor:
            print(i)

    elif ch==5:
        nm = input("Enter your name :")
        delete_Query = "delete from bank_account where name = ' " + nm + " ' "
        
        my_cursor.execute(delete_Query)
      
        print("Account Deleted Successfully..!")

    else:
        break

