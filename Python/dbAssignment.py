
import sqlite3

conn = sqlite3.connect('test.db')

with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_persons( \
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        col_fname TEXT)")
    conn.commit()
conn.close()

fileList = ('information.docx', 'Hello.txt', 'myImage.png',  \
           'myMovie.mpg', 'World.txt', 'data.pdf', 'myPhoto.jpg')


        


conn = sqlite3.connect('test.db')

with conn:
    cur = conn.cursor()
    cur.execute("INSERT INTO tbl_persons(col_fname) VALUES (?)", \
               ('Hello.txt',))
    cur.execute("INSERT INTO tbl_persons(col_fname) VALUES (?)", \
               ('World.txt',))
    cur.execute("INSERT INTO tbl_persons(col_fname) VALUES (?)", \
               ('information.docx',))
    cur.execute("INSERT INTO tbl_persons(col_fname) VALUES (?)", \
               ('myImage.png',))
    cur.execute("INSERT INTO tbl_persons(col_fname) VALUES (?)", \
               ('data.pdf',))
    cur.execute("INSERT INTO tbl_persons(col_fname) VALUES (?)", \
               ('myPhoto.jpg',))
    


                                                                

conn = sqlite3.connect('test.db')

with conn:
    cur = conn.cursor()
    cur.execute("SELECT col_fname FROM tbl_persons")
    newList = []
    for x in fileList:
        if x.endswith('.txt'):
            newList.append(x)

print(newList)


