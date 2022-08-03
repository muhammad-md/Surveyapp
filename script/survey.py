import tkinter
import tkinter as tk
import tkinter.font as tkFont
from tkinter import *
from tkinter.ttk import *
from tkinter import filedialog as fd
from tkinter import messagebox
from tkinter.messagebox import showinfo


#setting the window
root = Tk()
root.title("SURVEY FORM")
root.configure(width=600, height=900)
fontStyle = tkFont.Font(family="Lucida Grande", size=13)
fontStyle1 = tkFont.Font(family="Lucida Grande", size=14)

namelist = list()
class mainwindow:
    def __init__(self, master):
        self.master = master

        self.label = tk.Label(self.master, text="This survey is carried out to know the lecture hall that is mostly used between \n (LectureHallOne and LectureHallTwo), the days that it is mostly used, the \n department that uses it the most and the Level of students that uses it the most", font=fontStyle)
        self.label.place(relx = 0.5, rely = 0.05, anchor = CENTER)

        self.btn1 = tk.Button(self.master, text="Submit", font=fontStyle1, command=lambda: [getvariables(), self.clearpagee()])
        self.btn1.place(relx = 0.5, rely = 0.70, anchor=CENTER)

        
        self.label1 = tk.Label(self.master, text='Name: ', font=fontStyle1)
        self.label1.place(relx = 0.2, rely = 0.20, anchor=CENTER)
        #Create an Entry box
        self.entry1= tk.Entry(self.master)
        self.entry1.place(relx = 0.5, rely = 0.20, anchor=CENTER, width=150,height=40)


        self.label2 = tk.Label(self.master, text='Day: ', font=fontStyle1)
        self.label2.place(relx = 0.2, rely = 0.30, anchor=CENTER)
        menu2= StringVar(self.master)
        menu2.set("Select Day")
        #Create a dropdown Menu
        self.drop2= tk.OptionMenu(self.master, menu2, "Monday", "Tuesday","Wednesday","Thursday","Friday")
        self.drop2.place(relx = 0.5, rely = 0.30, anchor=CENTER, width=150,height=40)

        
        self.label3 = tk.Label(self.master, text='Level: ', font=fontStyle1)
        self.label3.place(relx = 0.2, rely = 0.40, anchor=CENTER)
        menu3= StringVar(self.master)
        menu3.set("Select Level")
        #Create a dropdown Menu
        self.drop3= tk.OptionMenu(self.master, menu3, "1", "2","3","4")
        self.drop3.place(relx = 0.5, rely = 0.40, anchor=CENTER, width=150,height=40)


        self.label4 = tk.Label(self.master, text='Department: ', font=fontStyle1)
        self.label4.place(relx = 0.2, rely = 0.50, anchor=CENTER)
        menu4= StringVar(self.master)
        menu4.set("Select Department")
        #Create a dropdown Menu
        self.drop4= tk.OptionMenu(self.master, menu4, "Statistics", "Computer","Mathematics","IT")
        self.drop4.place(relx = 0.5, rely = 0.50, anchor=CENTER, width=150,height=40)


        self.label5 = tk.Label(self.master, text='LectureHall: ', font=fontStyle1)
        self.label5.place(relx = 0.2, rely = 0.60, anchor=CENTER)
        menu5= StringVar(self.master)
        menu5.set("Select LectureHall")
        #Create a dropdown Menu
        self.drop5= tk.OptionMenu(self.master, menu5, "LectureHallOne", "LectureHallTwo")
        self.drop5.place(relx = 0.5, rely = 0.60, anchor=CENTER, width=150,height=40)
        
        def getvariables():
            name = self.entry1.get()
            namelist.append(name)
            day = menu2.get()
            level = menu3.get()
            department = menu4.get()
            lecturehall = menu5.get()
            print(name)
            print(day)
            print(level)
            print(department)
            print(lecturehall)


    def clearpagee(self):
        self.btn1.destroy()
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

        fontStyle2 = tkFont.Font(family="Lucida Grande", size=20)
        for p in namelist:
            name = p.upper()
    
        self.label = tk.Label(self.master, text="THANK YOU \n %s  !" %(name), font=fontStyle2)
        self.label.place(relx = 0.5, rely= 0.5, anchor=CENTER) 


#set default window as mainwindow and run
mainwindow(root)
root.mainloop()
