import matplotlib.animation as animation
from matplotlib import style
import matplotlib.pyplot as plt
from mysql.connector import connect
import numpy as np

fig = plt.figure()
#creating a subplot 
ax = fig.add_subplot(1,1,1)

#Function to make the chart live
def animate(i):
    #database connection
    connection = connect(host="xxxxxxxxx",database = "xxxxxxxxx",user="xxxx",password="xxxxxxxxx")
    #cursor for executing sql operations
    cursor = connection.cursor()

    lecturehall = ['LectureHallOne', 'LectureHallTwo']
    level1 = [0, 0]
    level2 = [0, 0]
    level3 = [0, 0]
    level4 = [0, 0]
    
    #getting the number of peoples that are in level one from the database
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

    #check if l1count1 and l1count2 are greater than 0 to insert them in thier position in the list        
    if l1count1 != 0 and l1count2 != 0:
        level1[0] = l1count1
        level1[1] = l1count2
    elif l1count1 != 0 and l1count2 == 0:
        level1[0] = l1count1
    elif l1count1 == 0 and l1count2 != 0:
        level1[1] = l1count2

    #getting the number of peoples that are in level two from the database
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
    
    #check if l2count1 and l2count2 are greater than 0 to insert them in thier position in the list   
    if l2count1 != 0 and l2count2 != 0:
        level2[0] = l2count1
        level2[1] = l2count2
    elif l2count1 != 0 and l2count2 == 0:
        level2[0] = l2count1
    elif l2count1 == 0 and l2count2 != 0:
        level2[1] = l2count2

    #getting the number of peoples that are in level three from the database
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
    
    #check if l3count1 and l3count2 are greater than 0 to insert them in thier position in the list   
    if l3count1 != 0 and l3count2 != 0:
        level3[0] = l3count1
        level3[1] = l3count2
    elif l3count1 != 0 and l3count2 == 0:
        level3[0] = l3count1
    elif l3count1 == 0 and l3count2 != 0:
        level3[1] = l3count2
    
    #getting the number of peoples that are in level four from the database
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
    
    #check if l4count1 and l4count2 are greater than 0 to insert them in thier position in the list   
    if l4count1 != 0 and l4count2 != 0:
        level4[0] = l4count1
        level4[1] = l4count2
    elif l4count1 != 0 and l4count2 == 0:
        level4[0] = l4count1
    elif l4count1 == 0 and l4count2 != 0:
        level4[1] = l4count2

    print(level1)
    print(level2)
    print(level3)
    print(level4)

    #transform the lists to arrays
    level1 = np.array(level1)
    level2 = np.array(level2)
    level3 = np.array(level3)
    level4 = np.array(level4)

    ax.clear()
    plt.bar(lecturehall, level1, 0.4, label='Level 1')
    plt.bar(lecturehall, level2, 0.4, bottom=level1, label='Level 2')
    plt.bar(lecturehall, level3, 0.4, bottom=level1+level2, label='Level 3')
    plt.bar(lecturehall, level4, 0.4, bottom=level1+level2+level3, label='Level 4')
    plt.legend()

ani = animation.FuncAnimation(fig, animate, interval=1000)
plt.show()
