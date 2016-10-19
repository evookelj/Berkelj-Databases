import sqlite3
import csv
from numpy import mean

f = "discobandit.db"

db = sqlite3.connect(f)
c = db.cursor()

def getGrades(student):
    q = "SELECT mark FROM students,courses WHERE students.id = courses.id and name=?"
    sel = c.execute(q, (student,))
    grades = []
    for record in sel:
        grades.append(record[0])
    return grades

def getAvg(student):
     return mean(getGrades(student))

def getAverages():
    q = "SELECT name, id FROM students"
    sel = c.execute(q)
    students = []
    for record in sel:
        students.append(record)
    for student in students:
        print "%s's (id: %d) average: \t%f"%(student[0],student[1],getAvg(student[0]))

getAverages()
