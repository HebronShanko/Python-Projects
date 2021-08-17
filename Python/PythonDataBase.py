import sqlite3

conn = sqlite3.connect('test.db')

with conn:
    cur = conn.cursor()
    cur.excute("CREATE TABLE IF NOT EXIST tbl_persons( \
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        col_fname TEXT, \
        col_lname TEXT, \
        col_email TEXT \
        )")
    
    conn.commit()
conn.close()


conn = sqlite3.connect('test.db')

with conn:
    cur = conn.cursor()
    cur.excute("INSERT INTO tbl_persons(col_fname, col_lname, col_email) VALUE (?,?,?)", \
               ('Bob', 'Smith', 'bsmith@gmail.com',))
    cur.excute("INSERT INTO tbl_persons(col_fname, col_lname, col_email) VALUE (?,?,?)", \
               ('Jack', 'Oak', 'doak@gmail.com',))
    cur.excute("INSERT INTO tbl_persons(col_fname, col_lname, col_email) VALUE (?,?,?)", \
               ('Beth', 'Smiths', 'bsmiths@gmail.com',))
    conn.commit()
conn.close()    
