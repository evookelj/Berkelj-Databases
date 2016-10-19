import sqlite3
import csv
from numpy import mean

def getGrades(student):
    query = "SELECT mark FROM students,courses WHERE students.id = courses.id and name=?"
    sel = cursor.execute(query, (student,))
    grades = []
    for record in sel:
        grades.append(record[0])
    return grades

def getAvg(student):
     return mean(getGrades(student))

def getAverages():
    sel = cursor.execute("SELECT name, id FROM students")
    students = []
    for record in sel:
        students.append(record)
    for student in students:
        print "%s's (id: %d) average: \t%f"%(student[0], student[1], getAvg(student[0]))

if __name__ == '__main__':
    db = sqlite3.connect("discobandit.db")
    cursor = db.cursor()
    getAverages()
