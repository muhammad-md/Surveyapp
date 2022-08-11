import matplotlib.animation as animation
from matplotlib import style
import matplotlib.pyplot as plt
import mysql.connector
from mysql.connector import connect, Error
import numpy as np

#style.use('fivethirtyeight')
fig = plt.figure()
ax = fig.add_subplot(1,1,1)

#Function to make the chart live
def animate(i):
    connection = connect(host="xxxxxxxxx",database = "SURVEY_DATA",user="xxxx",password="xxxxxxxxx",)
    print(connection)
    cursor = connection.cursor()

    lecturehall = ['LectureHallOne', 'LectureHallTwo']
    level1 = []
    level2 = []
    level3 = []
    level4 = []

    levelonehall = """SELECT lecturehall FROM RESPONSE WHERE level = 1"""
    cursor.execute(levelonehall)
    halloutputl1 = cursor.fetchall()
    l1count1 = 0
    l1count2 = 0
    for hall in halloutputl1:
        if hall == ('LectureHallOne',):
            l1count1 = l1count1 + 1
        elif hall == ('LectureHallTwo',):
            l1count2 = l1count2 + 1

    level1.append(l1count1)
    level1.append(l1count2)

    leveltwohall = """SELECT lecturehall FROM RESPONSE WHERE level = 2"""
    cursor.execute(leveltwohall)
    halloutputl2 = cursor.fetchall()
    l2count1 = 0
    l2count2 = 0
    for hall in halloutputl2:
        if hall == ('LectureHallOne',):
            l2count1 = l2count1 + 1
        elif hall == ('LectureHallTwo',):
            l2count2 = l2count2 + 1

    level2.append(l2count1)
    level2.append(l2count2)

    levelthreehall = """SELECT lecturehall FROM RESPONSE WHERE level = 3"""
    cursor.execute(levelthreehall)
    halloutputl3 = cursor.fetchall()
    l3count1 = 0
    l3count2 = 0
    for hall in halloutputl3:
        if hall == ('LectureHallOne',):
            l3count1 = l3count1 + 1
        elif hall == ('LectureHallTwo',):
            l3count2 = l3count2 + 1

    level3.append(l3count1)
    level3.append(l3count2)

    levelfourhall = """SELECT lecturehall FROM RESPONSE WHERE level = 4"""
    cursor.execute(levelfourhall)
    halloutputl4 = cursor.fetchall()
    l4count1 = 0
    l4count2 = 0
    for hall in halloutputl4:
        if hall == ('LectureHallOne',):
            l4count1 = l4count1 + 1
        elif hall == ('LectureHallTwo',):
            l4count2 = l4count2 + 1

    level4.append(l4count1)
    level4.append(l4count2)

    print(level1)
    print(level2)
    print(level3)
    print(level4)

    levelone = np.array(level1)
    leveltwo = np.array(level2)
    levelthree = np.array(level3)
    levelfour = np.array(level4)

    ax.clear()
    plt.bar(lecturehall, levelone, 0.4, label='Level 1')
    plt.bar(lecturehall, leveltwo, 0.4, bottom=levelone, label='Level 2')
    plt.bar(lecturehall, levelthree, 0.4, bottom=levelone+leveltwo, label='Level 3')
    plt.bar(lecturehall, levelfour, 0.4, bottom=levelone+leveltwo+levelthree, label='Level 4')
    plt.legend()

ani = animation.FuncAnimation(fig, animate, interval=1000)
plt.show()
