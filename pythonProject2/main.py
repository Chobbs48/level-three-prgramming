from tabulate import tabulate
import csv
import sqlite3

connect = sqlite3.connect('school_management_system.db')

c = connect.cursor()

c.execute("DROP TABLE IF EXISTS 'Courses';")
c.execute("DROP TABLE IF EXISTS 'Classrooms';")
c.execute('DROP TABLE IF EXISTS "Teachers";')
c.execute("DROP TABLE IF EXISTS 'Students';")
c.execute('DROP TABLE IF EXISTS "Enrollments";')

c.execute("""
CREATE TABLE Courses(
    ID INTEGER NOT NULL PRIMARY KEY,
    Name TEXT NOT NULL,
    Description TEXT NOT NULL,
    Credits INT NOT NULL,
    Classroom_ID INT NOT NULL,
    Teacher_ID INT NOT NULL,
    FOREIGN KEY (Classroom_ID) REFERENCES Classrooms(ID),
    FOREIGN KEY (Teacher_ID) REFERENCES Teachers(ID)
);
""")

c.execute("""
CREATE TABLE Enrollments(
    ID INTEGER NOT NULL PRIMARY KEY,
    Student_ID INT NOT NULL,
    Course_ID INT NOT NULL,
    Enrollment_Date TEXT NOT NULL,
    FOREIGN KEY (Student_ID) REFERENCES Students(ID),
    FOREIGN KEY (Course_ID) REFERENCES Courses(ID)
);
""")

c.execute("""
CREATE TABLE Teachers(
    ID INTEGER NOT NULL PRIMARY KEY,
    First_name TEXT NOT NULL,
    Last_name TEXT NOT NULL,
    Department TEXT NOT NULL,
    Email TEXT NOT NULL
);
""")
c.execute("""
CREATE TABLE Students(
    ID INTEGER NOT NULL PRIMARY KEY,
    First_name TEXT NOT NULL,
    Last_name TEXT NOT NULL,
    Date_Birth TEXT NOT NULL,
    Email TEXT NOT NULL
);
""")
c.execute("""
CREATE TABLE Classrooms(
    ID INTEGER NOT NULL PRIMARY KEY,
    Room_Number INT NOT NULL,
    Capacity INT NOT NULL,
    Building_Name TEXT NOT NULL
);
""")
list_of_teachers = []
with open('Teachers.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        c.execute("INSERT INTO Teachers (ID, First_name, Last_name, Department, Email) VALUES (?, ?, ?,?,?);",
                  (row[0], row[1], row[2], row[3],row[4]))

list_of_students = []
with open('Students.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        c.execute("INSERT INTO Students (ID, First_Name, Last_Name, Date_Birth, Email) VALUES (?,?, ?, ?,?);",
                  (row[0], row[1], row[2], row[3], row[4]))

list_of_classrooms = []
with open('Classrooms.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        c.execute("INSERT INTO Classrooms (ID, Room_Number, Capacity, Building_Name) VALUES (?, ?, ?,?);",
                  (row[0], row[1], row[2], row[3]))


list_of_courses = []
with open('Courses.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        c.execute("INSERT INTO Courses (ID, Name, Description, Credits, Classroom_ID, Teacher_ID) VALUES (?, ?, ?,?,?,?);",
                  (row[0], row[1], row[2], row[3],row[4],row[5]))

list_of_enrollments = []
with open('Enrollments.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        c.execute("INSERT INTO Enrollments (ID, Student_ID, Course_ID, Enrollment_Date) VALUES (?, ?, ?,?);",
                  (row[0], row[1], row[2], row[3]))

def main():
    def security():
        print("please enter your username and password")
        user = input("username: ")
        password = input("password: ")
        if user == "admin" and password == "password":
            print("welcome")
            menu()
        else:
            print("wrong username or password")
            security()
    security()

    def Exit():
        security()
    Exit()

    def menu():
        print('Add Student-1 , Add Teacher-2 , Add Classroom-3, Add Course-4, Enrol Student-5, Search Course-6, Search Students via Teacher-7, Exit-8 ')
        choice = input("what would you like to do? ")
        if choice =="1":
            AddStudent()

        elif choice =="2":
            Add_Teacher()

        elif choice =="3":
           Add_Classroom()

        elif choice == "4":
            Add_Course()

        elif choice == "5":
            Enrol_Student()

        elif choice == "6":
            Search_Course()

        elif choice == "7":
            Search_Teachers_Students()

        elif choice == "8":
            Exit()

        else:
            print("invalid choice")
            menu()

    def AddStudent():
        book_title = input("enter book title: ")
        book_genre = input("enter book genre: ")
        authy_n = input("is book from a pre existing author? y or n: ")
        if authy_n == 'y':
            while True:
                auth_id = input("enter author ID: ")

                c.execute("""
                                SELECT * FROM authors
                                WHERE ID = ?;
                                """, (auth_id,))
                a = c.fetchall()

                if a == []:
                    print('invalid ID')
                    edit()

                else:
                    print('Book Added')
                    borrow_ID = ''
                    c.execute("""
                                    INSERT INTO books 
                                    (title, genre, auth_id, borrow_id)
                                    VALUES (?, ?, ?, ?);
                                    """, (book_title, book_genre, auth_id, borrow_ID))
                    menu()

        elif authy_n == 'n':
            print('enter author details')
            auth_first_name = input("enter author first name: ")
            auth_last_name = input("enter author last name: ")
            auth_birth_date = input("enter author birth date: ")
            c.execute("""
                            INSERT INTO authors 
                            (first_name, last_name, birth_date)
                            VALUES (?, ?, ?);
                            """, (auth_first_name, auth_last_name, auth_birth_date))
            c.execute("""
                            SELECT ID FROM authors
                            WHERE first_name = ? AND last_name = ? AND birth_date = ?;""",
                      (auth_first_name, auth_last_name, auth_birth_date))
            auth_id = c.fetchall()
            auth_id = auth_id[0][0]
            borrow_id = ''
            c.execute("""
                            INSERT INTO books (title, genre, auth_id,borrow_id)
                            VALUES (?, ?, ?,?);
                            """, (book_title, book_genre, auth_id, borrow_id))
            print('Book Added')
            menu()

        else:
            print('invalid choice')
            edit()

    def Add_Teacher():


    def Add_Classroom():


    def Add_Course():


    def Enrol_Student():


    def Search_Course():


    def Search_Teachers_Students():

main()