# S SREENIVASA SHENOY
# Canara Engineering College
# Mangalore

import sqlite3
import os
os.system("")
from time import sleep

# Connecting into database
def connectDataBase():
    return sqlite3.connect("data.db")
db = connectDataBase()
cursor = connectDataBase().cursor()

# Inserting Data into Database
def Insert(db):
    movie_name = input("Enter Movie: ")
    actor = input("Enter Actor name: ")
    actress = input("Enter actress name: ")
    director = input("Enter director name: ")
    year = input("Enter year of release: ")
    cmd = ("""INSERT INTO database (movie,actor,actress,director,year) VALUES (?,?,?,?,?);""")
    parms = (movie_name, actor, actress, director, year)
    cursor.execute(cmd, parms)
    db.commit()
    print("\nData saved ")

# Removing data from Database
def Remove(db):
    cursor.execute("""DELETE FROM database;""").fetchall()
    db.commit()
    print("Data Deleted !")

# Finding Movies ->Actor
def Actor():
    act = str(input("Enter Actor Name : "))
    c = cursor.execute("""SELECT movie FROM database WHERE actor=(?);""", (act,)).fetchall()
    db.commit()
    for i in c:
        print(i, end='')
    if c == []:
        print("No Actor Found ")

# Finding Movies ->Actress
def Actress():
    act = str(input("Enter Actress Name : "))
    c = cursor.execute("""SELECT movie FROM database WHERE actress=(?);""", (act,)).fetchall()
    db.commit()
    for i in c:
        print(i, end='')
    if c == []:
         print("No Actress Found ")

# Finding Movies ->Director
def Director():
    director = str(input("Enter the director name : "))
    c = cursor.execute("""SELECT movie FROM database WHERE director=(?);""", (director,)).fetchall()
    db.commit()
    for i in c:
        print(i, end='')
    if c == []:
         print("No Dicrectors Found ")

# Finding Movies ->Year
def Year():
    year = str(input("Enter the release year : "))
    c = cursor.execute("""SELECT movie FROM database WHERE year=(?);""", (year,)).fetchall()
    db.commit()
    for i in c:
        print(i, end='')
    if c == []:
         print("No Movies Found ")

# Displaying Database
def Display():
    Movie = []
    Actor = []
    Actress = []
    Director = []
    Year = []
    data = cursor.execute("""SELECT * FROM database; """).fetchall()
    print("Movie" + " | " + "Actor" + " | " + "Actress" + " | " + "Director" + " | " + "Year")
#print data
    for row in data:
        Movie.append(row[0])
        Actor.append(row[1])
        Actress.append(row[2])
        Director.append(row[3])
        Year.append(row[4])
    print("Movie = ", Movie)
    print("Actor = ", Actor)
    print("Actress  = ", Actress)
    print("Director  = ", Director)
    print("Year  = ", Year)

# Create Table
def createTable(db):
    t = cursor.execute("""SELECT * FROM sqlite_master WHERE type='table' and name="database" ; """).fetchall()
    if t == []:
        cursor.execute("""CREATE TABLE IF NOT EXISTS database(movie VARCHAR(50),actor VARCHAR(20), actress VARCHAR(20), director VARCHAR(20),year INT);""")
        print('Table Created !')
        db.commit()
    else:
        print('Table Already Exist ')

# checking Database Connection
def testConnect():
    if connectDataBase() is not None:
        print("Connected ")
        createTable(connectDataBase())
    else:
        print("No Data Base not connected ")

# Clear screen
def clrscr():
    os.system('cls' if os.name == 'nt' else 'clear')

# start
def start():
    while(1):
        clrscr()
        print("\n\n-------------------->Movie DataBase by Sreenivas<-------------------")
        print(" ------------------------------------------------------------------")
        print(" 1. Check DataBase Connected ?")
        print(" 2. Insert data                                      ")
        print(" 3. Display data                                     ")
        print(" 4. Remove data                                      ")
        print(" 5. Movies by Actor                                  ")
        print(" 6. Movies by Actress                                ")
        print(" 7. Movies by Director                               ")
        print(" 8. Movies of year                                   ")
        print(" 9. Exit                                             ")
        print(" ------------------------------------------------------------------")
        choice = input("\nEnter your choice: ")
        print(" ------------------------------------------------------------------")
        if choice == '1':
            clrscr()
            testConnect()
            sleep(1)
        elif choice == '2':
            clrscr()
            Insert(connectDataBase())
            sleep(1)
        elif choice == '3':
            clrscr()
            Display()
            sleep(1)
        elif choice == '4':
            clrscr()
            Remove(connectDataBase())
            sleep(1)
        elif choice == '5':
            clrscr()
            Actor()
            sleep(1)
        elif choice == '6':
            clrscr()
            Actress()
            sleep(1)
        elif choice == '7':
            clrscr()
            Director()
            sleep(1)
        elif choice == '8':
            clrscr()
            Year()
            sleep(1)
        elif choice == '9':
            clrscr()
            print("END")
            sleep(1)
            exit()
            break
        else:
            clrscr()
            print("Invalid Choice!")
            sleep(1)
start()
