# -*- coding: utf-8 -*-
# dev : BloodHunter
from tkinter import *
import sqlite3 as sql



def logister():
    def submit():
        username.delete(0, END)
        password.delete(0, END)
        identity.delete(0, END)
    logreg = Tk()
    logreg.title('login/register')
    username = Entry(logreg, width=30).grid(row=0, column=1, padx=20)
    password = Entry(logreg, width=30).grid(row=1, column=1, padx=20)
    identity = Entry(logreg, width=30).grid(row=2, column=1, padx=20)
    Label(logreg, text='Username').grid(row=0, column=0)
    Label(logreg, text='Password').grid(row=1, column=0)
    Label(logreg, text='ID (custom 5 digit number)').grid(row=2, column=0)
    submitter = Button(logreg, text='submit your account', command=submit).grid(row=3, column=0, columnspan=2, pady=10, padx=10, ipadx=100)


def searcher():
    searchpoint = Tk()
    searchpoint.title('search data')
    search_bar = Entry(searchpoint, width=30).grid(row=0, column=0, padx=21, pady=21, ipadx=54)
    search_button = Button(searchpoint, width=20, text='search!').grid(row=1, column=0, padx=21, pady=21, ipadx=54)

def editerpoint():
    editSC = Tk()
    editSC.title('Edit data')
    edit_bar = Entry(editSC, width=20)
    Label(editSC, text='search a username to edit!')



def beta():
    unknwon = Tk()
    unknwon.title('un$kn*wn?>!')
    pass


root = Tk()
root.title('schools program?')
Button(root, text="login/register", command=logister, padx=30).grid(row=0, column=0, pady=1, padx=1, ipadx=20)
Button(root, text="search point", command=searcher, padx=30).grid(row=0, column=1, pady=1, padx=1, ipadx=20)
Button(root, text="editer", command=editerpoint, padx=30).grid(row=1, column=0, pady=1, padx=1, ipadx=20)
Button(root, text="un$kn*wn?>!", command=beta, state=DISABLED).grid(row=1, column=1, pady=1, padx=1, ipadx=20)

root.mainloop()

# <<!--DATA BASE CODE--!>>

myconn = sql.connect('school_program.db')

myc = myconn.cursor()

# <<!--TABLE CREATION--!>>
'''
myc.execute("""CREATE TABLE students (
        username text,
        password text,
        ID integer
        )""")
'''

myconn.commit()

myconn.close()
