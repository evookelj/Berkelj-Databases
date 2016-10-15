import sqlite3   #enable control of an sqlite database
import csv       #facilitates CSV I/O

f="discobandit.db"

db = sqlite3.connect(f) #open if f exists, otherwise create
c = db.cursor()    #facilitate db ops

#==========PEEP CREATION===========
csvPeeps = csv.DictReader(open("peeps.csv"))
q = "CREATE TABLE students (name TEXT, id INTEGER)"
c.execute(q)
for peep in csvPeeps:
    q = "INSERT INTO students VALUES (\"%s\", %d)" % (peep['name'],int(peep['id']))
    c.execute(q)

#==========COURSES CREATION===========
csvCourses = csv.DictReader(open("courses.csv"))
q = "CREATE TABLE courses (code TEXT, id INTEGER, mark INTEGER)"
c.execute(q)
for course in csvCourses:
    q = "INSERT INTO courses VALUES (\"%s\", %d, %d)" % (course['code'],int(course['mark']),int(course['id']))
    c.execute(q)

db.commit() #save changes
db.close()  #close database
