import gi
gi.require_version('Notify', '0.7')
from gi.repository import Notify as obj
import pyfiglet
import os,sys
import time
import sqlite3
import time
#this app is simple that takes input messages as text and reminds the user every time using notifications
#every time the system boots or every hour
#uses sqlite to store messages in the same dir
obj.init("Task Reminder")
obj.Notification.new("str").show()

def header():
    print(pyfiglet.figlet_format("TASK REMINDER",font="bubble"))

def about():
    header()
    print("An Reminder Application To remind you about the tasks \neverytime your system boots")

def add_note():
    conn=sqlite3.connect("msg.db")
    cur=conn.cursor()
    mesg=str(input("Enter The Message To Add"))
    cur.execute('INSERT INTO msgs(msg) VALUEs(?)',(mesg,))
    conn.commit()
    conn.close()

def rem_note():
    show_notes()
    inp=str(input("Select Id From the Table"))
    conn=sqlite3.connect("msg.db")
    cur=conn.cursor()
    cur.execute('DELETE from msgs WHERE id=?',(inp,))
    conn.commit()
    conn.close()

def show_notes():
    conn=sqlite3.connect("msg.db")
    cur=conn.cursor()
    print("Id   Message")
    for rows in cur.execute("Select * from msgs"):
        print(rows[0],"  ",rows[1])
    conn.commit()
    conn.close()
def func():
        os.system("clear")
        header()
        print("1.Add Note\n2.Remove Note\n3.View Notes\n4.About\n5.Exit")
        opt=int(input("Enter Option"))
        if opt==1:
            os.system("clear")
            add_note()
        elif opt== 2:
            os.system("clear")
            rem_note()
        elif opt==3:
            os.system("clear")
            show_notes()
        elif opt==4:
            os.system("clear")
            about()
        elif opt==5:
            os.system("clear")
            sys.exit()
        else:
            print("Unknown Value")

if __name__=="__main__":
    while True:
        func()
        time.sleep(1.8)
