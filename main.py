import mysql.connector as sqlc
import sys
import time

user =  input("Enter user : ")
p_word = input("Type password to database : ")
host = "localhost" #input("Enter host : ")
book_details = "book_details" #input("Enter name of Table containing details of book : ")

mydb = sqlc.connect(user= user, password= p_word, host = host)
my_curser = mydb.cursor()
my_curser.execute("show databases")
db = my_curser.fetchall()
print ("Thses are the pre-existing databases : ")
for i in db :
   print(i)

def db_idt():
    db_ch = input("Do you want to use one of them ? (y/n) :")
    global db_name
    match db_ch:
        case 'y' :
            db_name = input("Enter the databse name : ")
        case 'Y' :
            db_name = input("Enter the databse name : ")
        case 'n':
            db_name = input("Enter new databse name : ")
            my_curser.execute("create database " +db_name)
            my_curser.execute("use " +db_name)
            my_curser.execute("create table book_details(b_id varchar(6) not null primary key , b_name varchar(50) , publication varchar(20),ISBN varchar(20) , genre varchar(15), writer varchar(30) , no_b_left int(10), price int(5))")
            mydb.commit()
        case 'n':
            db_name = input("Enter new databse name : ")
            my_curser.execute("create database " +db_name)
            my_curser.execute("use " +db_name)
            my_curser.execute("create table book_details(b_id varchar(6) not null primary key , b_name varchar(50) , publication varchar(20),ISBN varchar(20) , genre varchar(15), writer varchar(30) , no_b_left int(10), price int(5))")
            mydb.commit()
        case other:
            print('''
            Use programme wisely...!
            Enter 'Y' OR 'N'
            ''' )
            time.sleep(2)
            E = input("Hit enter to Continue. ")
            db_idt()
db_idt()


my_curser.execute("use " +db_name)
print(db_name + " database using now.")

def main ():
    print ('''
                ***** MAIN MENU *****
    ------------------------------------------------
    1. Mark a book as sold
    ------------------------------------------------
    2. Show all books details available
    ------------------------------------------------
    3. Search book details by it's Book ID
    ------------------------------------------------
    4. Search book details by it's name 
    ------------------------------------------------
    5. Search book details by it's ISBN
    ------------------------------------------------
    6. Show all books of a publication
    ------------------------------------------------
    7. Show all books of a writer
    ------------------------------------------------
    8. Show all books of a genre
    ------------------------------------------------
    9. Show all books in a price range
    ------------------------------------------------
    10. Show all books which are left a few in stock
    ------------------------------------------------
    11. EXIT
    
    ''')
    ch = input ("Enter no. according to your execution : ")
    match ch:
        case '2':
            mark_sold()
        case '2':
            all_b_details()
        case '3':
            search_by_b_id()
        case '4':
            search_by_b_name()
        case '5':
            search_by_ISBN()
        case '6':
            search_by_publ()
        case '7':
            search_by_writer()
        case '8':
            search_by_genre()
        case '9':
            search_in_price_range()
        case '10':
            shorted_book()
        case '11':
            exit()
        case other:
            print("Use the programme wisely, dont't be stupid..!")
            main()

def mark_sold():
    b_id = input("Enter Book ID of the book : ")
    n = int(input("Enter the number of book sold : "))
    my_curser.execute('update '+book_details+ 'set no_b_left = no_b_left - '+n+' where b_id = "'+b_id+'"')
    rec = my_curser.fetchall()
    print(rec)
    time.sleep(1.5)
    print("\n")
    y_n = input("Want to mark another book as sold : ")
    if y_n == y or Y:
        

    E = input("Press Enter to naviagte to MAIN MENU.")
    print("\n")
    main()

def all_b_details():
    my_curser.execute("select * from " +book_details)
    rec = my_curser.fetchall()
    for i in rec:
        print(i)
        # print("\n")
    time.sleep(1.5)
    print("\n")
    E = input("Press Enter to naviagte to MAIN MENU.")
    print("\n")
    main()

def search_by_b_id():
    b_id = input("Enter Book ID for the book : ")
    my_curser.execute('select * from ' +book_details+ ' where b_id = " ' + b_id + '"' )
    rec = my_curser.fetchall()
    for i in rec:
        print(i)
        # print("\n")
    time.sleep(1.5)
    print("\n")
    E = input("Press Enter to naviagte to MAIN MENU.")
    print("\n")
    main()

def search_by_b_name():
    b_id = input("Enter Book Name : ")
    my_curser.execute('select * from ' +book_details+ ' where b_name = " ' + b_id + '"' )
    rec = my_curser.fetchall()
    for i in rec:
        print(i)
        # print("\n")
    time.sleep(1.5)
    print("\n")
    E = input("Press Enter to naviagte to MAIN MENU.")
    print("\n")
    main()

def search_by_ISBN():
    b_id = input("Enter ISBN of the book : ")
    my_curser.execute('select * from ' +book_details+ ' where ISBN = " ' + b_id + '"' )
    rec = my_curser.fetchall()
    for i in rec:
        print(i)
        # print("\n")
    time.sleep(1.5)
    print("\n")
    E = input("Press Enter to naviagte to MAIN MENU.")
    print("\n")
    main()

def search_by_publ():
    b_id = input("Enter publication of the book : ")
    my_curser.execute('select * from ' +book_details+ ' where publication = " ' + b_id + '"' )
    rec = my_curser.fetchall()
    for i in rec:
        print(i)
        # print("\n")
    time.sleep(1.5)
    print("\n")
    E = input("Press Enter to naviagte to MAIN MENU.")
    print("\n")
    main()

def search_by_writer():
    b_id = input("Enter Writer of the book : ")
    my_curser.execute('select * from ' +book_details+ ' where writer = " ' + b_id + '"' )
    rec = my_curser.fetchall()
    for i in rec:
        print(i)
        # print("\n")
    time.sleep(1.5)
    print("\n")
    E = input("Press Enter to naviagte to MAIN MENU.")
    print("\n")
    main()

def search_by_genre():
    b_id = input("Enter genre : ")
    my_curser.execute('select * from ' +book_details+ ' where genre = " ' + b_id + '"' )
    rec = my_curser.fetchall()
    for i in rec:
        print(i)
        # print("\n")
    time.sleep(1.5)
    print("\n")
    E = input("Press Enter to naviagte to MAIN MENU.")
    print("\n")
    main()

def search_in_price_range():
    u_lim = int (input("Enter upper limit for search : "))
    l_lim = int (input("Enter lower limit for search : "))
    my_curser.execute('select * from ' +book_details+ ' where price > ' + l_lim + ' and price < '+u_lim )
    rec = my_curser.fetchall()
    for i in rec:
        print(i)
        # print("\n")
    time.sleep(1.5)
    print("\n")
    E = input("Press Enter to naviagte to MAIN MENU.")
    print("\n")
    main()

def shorted_book():
    l_lim = int (input("Enter lower limit no. for a book in stock : "))
    my_curser.execute('select * from ' +book_details+ ' where no_b_left < ' +l_lim )
    rec = my_curser.fetchall()
    for i in rec:
        print(i)
        # print("\n")
    time.sleep(1.5)
    print("\n")
    E = input("Press Enter to naviagte to MAIN MENU.")
    print("\n")
    main()

def exit():
    mydb.commit()
    mydb.close()
    print("\n")
    print("************* Programme ENDED..! *************")
    time.sleep(1.8)
    sys.exit()

main()