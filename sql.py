import sqlite3





conn = sqlite3.connect('database.db')
c = conn.cursor()
users = [
    ('Bob',25,'bob@gmail.com'),
    ('charlie',35,'charlie@gmail.com'),
    ('xyz',40,'xyz@gmail.com'),
    ('abc',67,'abc@gmail.com')

]
c.executemany('INSERT INTO users(name,age,email) VALUES(?,?,?)',users)
#c.execute("UPDATE users SET age = 31 WHERE name = 'Bob'")
#c.execute("UPDATE users SET age = 36 WHERE name = 'charlie'")
#c.execute("DELETE FROM USERS WHERE id ='6'")
#c. execute("SELECT * FROM USERS")
rows = c.fetchall()
for row in rows:
    print(row)


c.execute("SELECT * FROM USERS WHERE AGE > 30")
filtered_rows =c.fetchall()
for row in filtered_rows:
    print(row)    

conn.commit()