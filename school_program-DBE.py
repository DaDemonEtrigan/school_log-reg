# School app for saving scores and etc
# dev : Captain_Etrigan
# state : indev
from tkinter import *
import sqlite3 as sql


def logister():
    logreg = Tk()
    logreg.title('Register')

    def submitter():
        mycnct = sql.connect('school_program.db')
        mycu = mycnct.cursor()

        mycu.execute("INSERT INTO students VALUES (:username, :password, :iidentity, :grade)",
                     {
                         'username': username.get(),
                         'password': password.get(),
                         'iidentity': iidentity.get(),
                         'grade': grade.get()
                     })

        mycnct.commit()
        mycnct.close()

        username.delete(0, END)
        password.delete(0, END)
        iidentity.delete(0, END)
        grade.delete(0, END)

    username = Entry(logreg, width=30)
    username.grid(row=0, column=1, padx=20)

    password = Entry(logreg, width=30)
    password.grid(row=1, column=1, padx=20)

    grade = Entry(logreg, width=20)
    grade.grid(row=2, column=1, padx=20)

    iidentity = Entry(logreg, width=30)
    iidentity.grid(row=3, column=1, padx=20)

    Label(logreg, text='Username').grid(row=0, column=0)
    Label(logreg, text='Password').grid(row=1, column=0)
    Label(logreg, text='grade').grid(row=2, column=0)
    Label(logreg, text='ID (custom 5 digit number)').grid(row=3, column=0)
    submitter = Button(logreg, text='Submit your account', command=submitter)
    submitter.grid(row=4, column=0, columnspan=2, pady=10, padx=10, ipadx=100)


def searcher():
    searchpoint = Tk()
    searchpoint.title('Search data')

    def cobtn():
        mycon = sql.connect('school_program.db')
        mycursr = mycon.cursor()

        mycursr.execute("SELECT * FROM students")
        recs = mycursr.fetchall()
        print(recs)

        print_records = ''
        for rec in recs:
            print_records += "Username : " + str(rec[0]) + "\n"
            print_records += "Password : " + str(rec[1]) + "\n"
            print_records += "ID : " + str(rec[2]) + "\n"
            print_records += "Grade : " + str(rec[3]) + "\n"
            print_records += 23 * "=" + "\n"

        Label(searchpoint, text=print_records).grid(row=9, column=0, columnspan=2)

        mycon.commit()
        mycon.close()

    qbtn = Button(searchpoint, text='show all users', command=cobtn)
    qbtn.grid(row=7, column=0, columnspan=2, pady=10, padx=10, ipadx=100)


def editerpoint():
    editSC = Tk()
    editSC.title('Edit data (currently only delete available soon)')
    edit_bar = Entry(editSC, width=20)
    edit_bar.grid(row=1, column=1)
    Label(editSC, text='search a username to edit!').grid(row=1, column=0)


def beta():
    unknown = Tk()
    unknown.title('un$kn*wn?>!')
    pass


root = Tk()
root.title('schools program?')
button1 = Button(root, text="login/register", command=logister, padx=30)
button1.grid(row=0, column=0, pady=1, padx=1, ipadx=20)
button2 = Button(root, text="search point", command=searcher, padx=30)
button2.grid(row=0, column=1, pady=1, padx=1, ipadx=20)
button3 = Button(root, text="editer", command=editerpoint, padx=30)
button3.grid(row=1, column=0, pady=1, padx=1, ipadx=20)
button4 = Button(root, text="un$kn*wn?>!", command=beta, state=DISABLED)
button4.grid(row=1, column=1, pady=1, padx=1, ipadx=20)

root.mainloop()

# <<!--DATA BASE CODE--!>>

myconn = sql.connect('school_program.db')

myc = myconn.cursor()

# <<!--TABLE CREATION--!>>
'''
myc.execute("""CREATE TABLE students (
        username text,
        password text,
        ID integer,
        grade integer
        )""")
'''

myconn.commit()

myconn.close()
