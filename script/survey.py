import tkinter as tk
import tkinter.font as tkFont
from tkinter import *
from tkinter import messagebox
from mysql.connector import connect

#connecting mysql database
connection = connect(host="xxxxxxxxx",database = "xxxxxxxxx",user="xxxx",password="xxxxxxxxx")
print(connection)

#for executing sql operations
cursor = connection.cursor()

#setting the window
window = Tk()
window.title("SURVEY FORM")
window.configure(width=600, height=900)
fontStyle1 = tkFont.Font(family="Candara", size=13)
fontStyle2 = tkFont.Font(family="Candara", size=22)

#list to save the current user name
namelist = []

class mainwindow:
    def __init__(self, master):
        self.master = master

        self.label = tk.Label(self.master, text="This survey is carried out to know the lecture hall that is mostly used between \n LectureHallOne and LectureHallTwo. This survey would also be \n used to find out the level of students that uses it the most", font=fontStyle1)
        self.label.place(relx = 0.5, rely = 0.05, anchor = CENTER)

        self.button = tk.Button(self.master, text="Submit", font=fontStyle1, command=lambda: [getvariables(), self.clearpage()])
        self.button.place(relx = 0.5, rely = 0.70, anchor=CENTER)
        
        self.label1 = tk.Label(self.master, text='Name: ', font=fontStyle1)
        self.label1.place(relx = 0.2, rely = 0.20, anchor=CENTER)
        #Create an Entry box to enter name
        self.entry1= tk.Entry(self.master)
        self.entry1.place(relx = 0.5, rely = 0.20, anchor=CENTER, width=150,height=40)

        self.label2 = tk.Label(self.master, text='Day: ', font=fontStyle1)
        self.label2.place(relx = 0.2, rely = 0.30, anchor=CENTER)
        self.menu2= StringVar(self.master)
        self.menu2.set("Select Day")
        #Create a dropdown Menu
        self.drop2= tk.OptionMenu(self.master, self.menu2, "Monday", "Tuesday","Wednesday","Thursday","Friday")
        self.drop2.place(relx = 0.5, rely = 0.30, anchor=CENTER, width=150,height=40)
        
        self.label3 = tk.Label(self.master, text='Level: ', font=fontStyle1)
        self.label3.place(relx = 0.2, rely = 0.40, anchor=CENTER)
        self.menu3= StringVar(self.master)
        self.menu3.set("Select Level")
        #Create a dropdown Menu
        self.drop3= tk.OptionMenu(self.master, self.menu3, 1, 2,3,4)
        self.drop3.place(relx = 0.5, rely = 0.40, anchor=CENTER, width=150,height=40)

        self.label4 = tk.Label(self.master, text='Department: ', font=fontStyle1)
        self.label4.place(relx = 0.2, rely = 0.50, anchor=CENTER)
        self.menu4= StringVar(self.master)
        self.menu4.set("Select Department")
        #Create a dropdown Menu
        self.drop4= tk.OptionMenu(self.master, self.menu4, "Statistics", "Computer","Mathematics","IT")
        self.drop4.place(relx = 0.5, rely = 0.50, anchor=CENTER, width=150,height=40)

        self.label5 = tk.Label(self.master, text='LectureHall: ', font=fontStyle1)
        self.label5.place(relx = 0.2, rely = 0.60, anchor=CENTER)
        self.menu5= StringVar(self.master)
        self.menu5.set("Select LectureHall")
        #Create a dropdown Menu
        self.drop5= tk.OptionMenu(self.master, self.menu5, "LectureHallOne", "LectureHallTwo")
        self.drop5.place(relx = 0.5, rely = 0.60, anchor=CENTER, width=150,height=40)
        
        def getvariables():
            name = (self.entry1.get())
            namelist.append(name)
            day = self.menu2.get()
            level = int(self.menu3.get())
            department = self.menu4.get()
            lecturehall = self.menu5.get()

            username = """SELECT name FROM response WHERE name = %s"""
            value = (name,)
            cursor.execute(username, value)
            usernameoutput = cursor.fetchall()
            #print(usernameoutput)

            userdept = """SELECT department FROM response WHERE name = %s"""
            value = (name,)
            cursor.execute(userdept, value)
            userdeptoutput = cursor.fetchall()
            if len(userdeptoutput) > 0:
                for dept in userdeptoutput:
                    dept = dept
            else:
                dept = "none"
            #print(userdeptoutput)

            userlevel = """SELECT level FROM response WHERE name = %s"""
            value = (name,)
            cursor.execute(userlevel, value)
            userleveloutput = cursor.fetchall()
            if len(userleveloutput) > 0:
                for lev in userleveloutput:               #lev means level
                    lev = lev
            else:
                lev = "none"
            #print(userleveloutput)
            
            #check if the current user has already participated by checking his/her name, department and level. 
            #if present in the database, then he cannot submit again, if not found in the database
            #if not present in the database, then add the user inputs to the database 
            if dept == (department,) and lev == (level,) and len(usernameoutput) >= 1:
                messagebox.showinfo("", "Thank you %s ! You have Already participated in this survey" %(name))
                #print("THIS USER ALREADY EXISTS")
            else:
                cursor.execute("INSERT INTO RESPONSE (name, day, level, department, lecturehall) VALUES ('%s', '%s', '%s', '%s', '%s')" % (name, day, level, department, lecturehall))
                connection.commit()
        
    #function to clear the page(make it empty) and shows a message to trh user
    def clearpage(self):
        self.button.destroy()
        self.label.destroy()
        self.label1.destroy()
        self.label2.destroy()
        self.label3.destroy()
        self.label4.destroy()
        self.label5.destroy()
        self.entry1.destroy()
        self.drop2.destroy()
        self.drop3.destroy()
        self.drop4.destroy()
        self.drop5.destroy()

        name = namelist[0].upper()
        label6 = tk.Label(self.master, text="THANK YOU \n %s  !" %(name), font=fontStyle2)
        label6.place(relx = 0.5, rely= 0.5, anchor=CENTER) 

#make window unexpandable(fixed)
window.resizable(False,False)
#set default window as mainwindow and run
mainwindow(window)
window.mainloop()
