import sqlite3   #enable control of an sqlite database
import csv       #facilitates CSV I/O

f="discobandit.db"

db = sqlite3.connect(f) #open if f exists, otherwise create
c = db.cursor()    #facilitate db ops

#==========PEEP CREATION===========
dPeeps = csv.DictReader(open("peeps.csv"))
try:
    q = "CREATE TABLE students (name TEXT, id INTEGER)"
    c.execute(q)
    for peep in dPeeps:
        q = "INSERT INTO students VALUES (\"%s\", %d)" % (peep['name'],int(peep['id']))
        c.execute(q)
    print "TABLE students successfully populated with contents of 'peeps.csv'"
except:
    print "Error: TABLE 'students' already exists. Cannot re-create. Delete %s and re-run this file to recreate table.\n" % (f)

#==========COURSES CREATION===========
dCourses = csv.DictReader(open("courses.csv"))
try:
    q = "CREATE TABLE courses (code TEXT, id INTEGER, mark INTEGER)"
    c.execute(q)
    for course in dCourses:
        q = "INSERT INTO courses VALUES (\"%s\", %d, %d)" % (course['code'],int(course['mark']),int(course['id']))
        c.execute(q)
    print "TABLE courses successfully populated with contents of 'courses.csv'"

except:
    print "Error: TABLE 'courses' already exists. Cannot re-create. Delete %s and re-run this file to recreate table.\n" % (f)

db.commit() #save changes
db.close()  #close database
