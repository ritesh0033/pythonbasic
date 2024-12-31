# databae connection
import sqlite3
def init_db():
    conn = sqlite3.connect('user.db')
    c = conn.cursor()
    c.execute('CREATE TABLE IF NOT EXISTS employee (id INTEGER PRIMARY KEY AUTOINCREMENT,name TEXT,age INTEGER, email TEXT)')
    conn.commit()
    c.close()
    conn.close()
    
 #create a users
def create_user(): 
    name  = input("enter the name:")
    age = input ("enter the age:")  
    email = input("enter the email")
    conn = sqlite3.connect('user.db')
    c = conn.cursor()
    c.executemany("INSERT INTO employee(name,age,email)VALUES(?,?,?)",name,age,email)
    conn.commit()
    c.close()
    conn.close()  

# read the users
def read_users():
     conn = sqlite3.connect('user.db')
     c = conn.cursor()
     c.execute("SELECT * FROM employee" )
     employee = c.fetchall()
     
     
