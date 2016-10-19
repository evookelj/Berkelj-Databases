import sqlite3
import csv
from numpy import mean

def getGrades(student_id):
    query = "SELECT mark FROM students,courses WHERE students.id = courses.id and students.id=?"
    sel = cursor.execute(query, (student_id,))
    grades = []
    for record in sel:
        grades.append(record[0])
    return grades

def getAvg(student_id):
     return mean(getGrades(student_id))

def getAverages():
    sel = cursor.execute("SELECT name, id FROM students")
    students = []
    for record in sel:
        students.append(record)
    for (name, id) in students:
        print "%s's (id: %d) average: \t%f"%(name, id, getAvg(id))

if __name__ == '__main__':
    db = sqlite3.connect("discobandit.db")
    cursor = db.cursor()
    getAverages()
