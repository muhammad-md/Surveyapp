from multiprocessing import connection
import tkinter as tk
import tkinter.font as tkFont
from tkinter import *
from tkinter.ttk import *
from tkinter import filedialog as fd
from tkinter import messagebox
from tkinter.messagebox import showinfo
from getpass import getpass
from mysql.connector import connect, Error
from pymysql import *


#connecting mysql database
connection = connect(host="xxxxxxxxx",database = "SURVEY_DATA",user="xxxx",password="xxxxxxxxx",)
print(connection)

#for executing sql operations
cursor = connection.cursor()


#setting the window
window = Tk()
window.title("SURVEY FORM")
window.configure(width=600, height=900)
fontStyle = tkFont.Font(family="Candara", size=13)
fontStyle1 = tkFont.Font(family="Candara", size=14)


class mainwindow:
    def __init__(self, master):
        self.master = master

        label = tk.Label(self.master, text="This survey is carried out to know the lecture hall that is mostly used between \n LectureHallOne and LectureHallTwo. This survey would also be \n used to find out the level of students that uses it the most", font=fontStyle)
        label.place(relx = 0.5, rely = 0.05, anchor = CENTER)

        button = tk.Button(self.master, text="Submit", font=fontStyle1, command=lambda: [getvariables(), clearpage()])
        button.place(relx = 0.5, rely = 0.70, anchor=CENTER)

        
        label1 = tk.Label(self.master, text='Name: ', font=fontStyle1)
        label1.place(relx = 0.2, rely = 0.20, anchor=CENTER)
        #Create an Entry box
        entry1= tk.Entry(self.master)
        entry1.place(relx = 0.5, rely = 0.20, anchor=CENTER, width=150,height=40)


        label2 = tk.Label(self.master, text='Day: ', font=fontStyle1)
        label2.place(relx = 0.2, rely = 0.30, anchor=CENTER)
        menu2= StringVar(self.master)
        menu2.set("Select Day")
        #Create a dropdown Menu
        drop2= tk.OptionMenu(self.master, menu2, "Monday", "Tuesday","Wednesday","Thursday","Friday")
        drop2.place(relx = 0.5, rely = 0.30, anchor=CENTER, width=150,height=40)

        
        label3 = tk.Label(self.master, text='Level: ', font=fontStyle1)
        label3.place(relx = 0.2, rely = 0.40, anchor=CENTER)
        menu3= StringVar(self.master)
        menu3.set("Select Level")
        #Create a dropdown Menu
        drop3= tk.OptionMenu(self.master, menu3, 1, 2,3,4)
        drop3.place(relx = 0.5, rely = 0.40, anchor=CENTER, width=150,height=40)


        label4 = tk.Label(self.master, text='Department: ', font=fontStyle1)
        label4.place(relx = 0.2, rely = 0.50, anchor=CENTER)
        menu4= StringVar(self.master)
        menu4.set("Select Department")
        #Create a dropdown Menu
        drop4= tk.OptionMenu(self.master, menu4, "Statistics", "Computer","Mathematics","IT")
        drop4.place(relx = 0.5, rely = 0.50, anchor=CENTER, width=150,height=40)


        label5 = tk.Label(self.master, text='LectureHall: ', font=fontStyle1)
        label5.place(relx = 0.2, rely = 0.60, anchor=CENTER)
        menu5= StringVar(self.master)
        menu5.set("Select LectureHall")
        #Create a dropdown Menu
        drop5= tk.OptionMenu(self.master, menu5, "LectureHallOne", "LectureHallTwo")
        drop5.place(relx = 0.5, rely = 0.60, anchor=CENTER, width=150,height=40)
        
        namelist = list()   #list to save the user name
        def getvariables():
            name = str(entry1.get())
            namelist.append(name)
            day = menu2.get()
            level = int(menu3.get())
            department = menu4.get()
            lecturehall = menu5.get()
  


            username = """SELECT name FROM response WHERE name = %s"""
            value = (name,)
            cursor.execute(username, value)
            usernameoutput = cursor.fetchall()
            print(usernameoutput)

            userdept = """SELECT department FROM response WHERE name = %s"""
            value = (name,)
            cursor.execute(userdept, value)
            userdeptoutput = cursor.fetchall()
            if len(userdeptoutput) > 0:
                for dept in userdeptoutput:
                    dept = dept
            else:
                dept = "none"
            print(userdeptoutput)

            userlevel = """SELECT level FROM response WHERE name = %s"""
            value = (name,)
            cursor.execute(userlevel, value)
            userleveloutput = cursor.fetchall()
            if len(userleveloutput) > 0:
                for lev in userleveloutput:
                    lev = lev
            else:
                lev = "none"
            print(userleveloutput)

             
            if dept == (department,) and lev == (level,) and len(usernameoutput) >= 1:
                messagebox.showinfo("", "Thank you %s ! You have Already participated in this survey" %(name))
                print("THIS USER ALREADY EXISTS")
            else:
                cursor.execute("INSERT INTO RESPONSE (name, day, level, department, lecturehall) VALUES ('%s', '%s', '%s', '%s', '%s')" % (name, day, level, department, lecturehall))
                connection.commit()
                print("DOOOOOOOOOOOOOOOOOOOOOOOOO")

        def clearpage():
            button.destroy()
            label.destroy()
            label1.destroy()
            label2.destroy()
            label3.destroy()
            label4.destroy()
            label5.destroy()
            entry1.destroy()
            drop2.destroy()
            drop3.destroy()
            drop4.destroy()
            drop5.destroy()

            fontStyle2 = tkFont.Font(family="Candara", size=22)
            for name in namelist:
                name = name.upper()
        
            label6 = tk.Label(self.master, text="THANK YOU \n %s  !" %(name), font=fontStyle2)
            label6.place(relx = 0.5, rely= 0.5, anchor=CENTER) 

#make window unexpandable(fixed)
window.resizable(False,False)
#set default window as mainwindow and run
mainwindow(window)
window.mainloop()
