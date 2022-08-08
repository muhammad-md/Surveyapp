import matplotlib.pyplot as plt
import numpy as np
import mysql.connector
import pandas.io.sql as sql
from getpass import getpass
from mysql.connector import connect, Error
from pymysql import *



connection = connect(host="localhost",database = "SURVEY_DATA",user="root",password="55+DAta#3",)
print(connection)

cursor = connection.cursor()

hall = ['LectureHallOne', 'LectureHallTwo']

l1 = []
l2 = []
l3 = []
l4 = []


level1h = """SELECT lecturehall FROM RESPONSE WHERE level = 1"""
cursor.execute(level1h)
msg9 = cursor.fetchall()
counth1 = 0
counth2 = 0
for i in msg9:
    if i == ('LectureHallOne',):
        counth1 = counth1 + 1
    elif i == ('LectureHallTwo',):
        counth2 = counth2 + 1

l1.append(counth1)
l1.append(counth2)

level2h = """SELECT lecturehall FROM RESPONSE WHERE level = 2"""
cursor.execute(level2h)
msg2 = cursor.fetchall()
counth2 = 0
counth22 = 0
for i in msg2:
    if i == ('LectureHallOne',):
        counth2 = counth2 + 1
    elif i == ('LectureHallTwo',):
        counth22 = counth22 + 1

l2.append(counth1)
l2.append(counth22)

level3h = """SELECT lecturehall FROM RESPONSE WHERE level = 3"""
cursor.execute(level3h)
msg3 = cursor.fetchall()
counth3 = 0
counth33 = 0
for i in msg3:
    if i == ('LectureHallOne',):
        counth3 = counth3 + 1
    elif i == ('LectureHallTwo',):
        counth33 = counth33 + 1

l3.append(counth3)
l3.append(counth33)

level4h = """SELECT lecturehall FROM RESPONSE WHERE level = 4"""
cursor.execute(level4h)
msg4 = cursor.fetchall()
counth4 = 0
counth44 = 0
for i in msg4:
    if i == ('LectureHallOne',):
        counth4 = counth4 + 1
    elif i == ('LectureHallTwo',):
        counth44 = counth44 + 1

l4.append(counth4)
l4.append(counth44)

print(l1)
print(l2)
print(l3)
print(l4)

l11 = np.array(l1)
l22 = np.array(l2)
l33 = np.array(l3)
l44 = np.array(l4)


w = 0.4

plt.bar(hall, l11, w, label="Level 1")
plt.bar(hall, l22, w, bottom=l11, label="Level 2")
plt.bar(hall, l33, w, bottom=l11+l22, label="Level 3")
plt.bar(hall, l44, w, bottom=l11+l22+l33, label="Level 4")

plt.legend()
plt.show()
