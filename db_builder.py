import sqlite3   #enable control of an sqlite database
import csv       #facilitates CSV I/O

f="discobandit.db"

db = sqlite3.connect(f) #open if f exists, otherwise create
c = db.cursor()    #facilitate db ops

#==========PEEP CREATION===========
dPeeps = csv.DictReader(open("peeps.csv"))
try:
    c.execute("CREATE TABLE students (name TEXT, id INTEGER)")
    for peep in dPeeps:
        query_template = "INSERT INTO students VALUES (?, ?)"
        values = (peep['name'], int(peep['id']))
        c.execute(query_template, values)
    print "TABLE students successfully populated with contents of 'peeps.csv'"
except:
    print "Error: TABLE 'students' already exists. Cannot re-create. Delete %s and re-run this file to recreate table.\n" % (f)

#==========COURSES CREATION===========
dCourses = csv.DictReader(open("courses.csv"))
try:
    c.execute("CREATE TABLE courses (code TEXT, id INTEGER, mark INTEGER)")
    for course in dCourses:
        query_template = "INSERT INTO courses VALUES (?, ?, ?)"
        values = (course['code'], int(course['id']), int(course['mark']))
        c.execute(query_template, values)
    print "TABLE courses successfully populated with contents of 'courses.csv'"

except:
    print "Error: TABLE 'courses' already exists. Cannot re-create. Delete %s and re-run this file to recreate table.\n" % (f)

db.commit() #save changes
db.close()  #close database
