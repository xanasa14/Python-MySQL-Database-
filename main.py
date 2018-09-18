import mysql.connector

while (True):
    try:
        print ("0 is for creating a Database")
        print ("1 is creating a primary key in our Database")
        print ("2 is to add more atributes to a table")
        print ("3 is for instering data into our Database")
        print ("4 is to show all the data in the tablas from the database")
        option = input("What would you like to do? ")
        option = int(option)
    except:
        print("There is a mistake. Try again")
        # Creating a database
    if option == 0:
        print ("We are creating a database")
        mydb = mysql.connector.connect(host="localhost",
                                       user="root",
                                       passwd="")
        mycursor = mydb.cursor()
        val = input ("What's the name of the database you want to create?")
        sql = "CREATE DATABASE "
        command = sql + val
        mycursor.execute(command)

    elif option == 1:
        print("We are creating a primary key in a table")
        correct_Database = input("In which database you would like to save the primary key in a table? ")
        mydb = mysql.connector.connect(host="localhost",
                                       user="root",
                                       passwd="",
                                       database= correct_Database)
        mycursor = mydb.cursor()
        atr1 = input("Whats the first atribute? ")
        atr2 = input("What the second atribute?")
        atr3 = input("Whats the third attibute/")
        command = "CREATE TABLE IF NOT EXISTS SoccerPlayers (id INT AUTO_INCREMENT PRIMARY KEY, " + atr1 + " VARCHAR(255), " + atr2 + " VARCHAR(255), " + atr3 + " VARCHAR(255))"
        mycursor.execute(command)
    elif option == 2:
        print("We are adding one more atribute to a table")
        correct_Database = input("In which database you would like to save the primary key in a table? ")
        mydb = mysql.connector.connect(host="localhost",
                                       user="root",
                                       passwd="",
                                       database= correct_Database)
        mycursor = mydb.cursor()
        table = input("In What table is the new atribute going to be added" )
        new_atr = input("Whats the new atribute to be added ?")
        command = "ALTER TABLE "+ table + " ADD COLUMN " + new_atr +" VARCHAR(15)"
        mycursor.execute(command)
    elif option == 3:
        print("We are inserting data into our table")
        correct_Database = input("In which database you would like to insert data? ")
        mydb = mysql.connector.connect(host="localhost",
                                       user="root",
                                       passwd="",
                                       database= correct_Database)

        mycursor = mydb.cursor()
        table = input("Whats the name of the table?")
        command = "SHOW COLUMNS FROM "+ correct_Database +"."+table
        mycursor.execute(command)
        counter = 0
        lista = []
        atributes = []
        str1 = ""
        str2 = ""
        str3 = ""
        for x in mycursor:
            if x[0]!= "id":
                print(x[0], end= "       ")
                counter += 1
                atributes.append(x[0])
        print ("     ")

        for i in range (len (atributes)):
            if i == len(atributes)-1:
                str1 += atributes[i]
            else:
                str1 += atributes[i] + ", "
        print (str1)
        for i in range(counter):
            tmp = input("Whats the value for it?")
            lista.append(tmp)
        tup1 = ('%s',) * counter
        tuplist = tuple(lista)
        tup = str(tup1)
        val = str(tuplist)
        command = "INSERT INTO " + table + " (" + str1 + ") VALUES "+ val
        sql = command
        mycursor.execute(sql)
        mydb.commit()

    elif option == 4:
        print("We are extracting data from our table")
        correct_Database = input("In what database you would like to see all the data from?")
        mydb = mysql.connector.connect(host="localhost",
                                       user="root",
                                       passwd="",
                                       database= correct_Database)

        mycursor = mydb.cursor()
        table = input("Whats the name of the table?")
        command = "SELECT * FROM "+ correct_Database +"."+table
        mycursor.execute(command)
        myresult = mycursor.fetchall()
        print (myresult)
