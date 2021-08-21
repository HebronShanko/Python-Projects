import os
from tkinter import *
import tkinter as tk
import sqlite3


import phonebook_main
import phonebook_gui



def center_window(self, w, h):
    screen_width = self.master.winfo_screenwidth()
    screen_height = self.master.winfo_screenheight()

    x = int((screen_width/2) - (w/2))
    x = int((screen_height/2) - (h/2))
    centerGeo = self.master.geometry('{}x{}+{}'.format(w, h, x, y))
    return centerGeo


def ask_quit(self):
    if messagebox.askokcancel1("Exit program", "Okay to exit application?"):

        self.master.destroy()
        os._exit(0)



    
def create_db(self):
    conn = sqlite3.connect('phonebook.db')
    with conn:
        cur = conn.cursor()
        cur.execute("CREATE TABLE if not exists tbl_phonebook( \
            ID INTEGER PRIMARY KEY AUTOINCREMENT, \
            col_fname TEXT, \
            col_lname TEXT, \
            col_fullname TEXT, \
            col_phone TEXT, \
            col_email TEXT, \
            );")

        conn.commit()
    conn.close()
    first_run(self)

def first_run(self):
    data = ('John', 'Doe', 'John Doe', '111-111-1111', 'jdoe@gmail.com')
    conn = sqlite3.connect('phonebook.db')
    with conn:
        cur = conn.cursor()
        cur,count = count_records(cur)
        if count < 1:
            cur.execute("""INSERT INTO tbl_phonebook (col_fname, col_lname, col_fullname, col_phone, col_email) VALUES (?,?,?,?,?)""",(data))
            conn.commit()
    conn.close()


def count_records(cur):
    count = ""
    cur.execute("""SELECT COUNT(*) FROM tbl_phonebook""")
    count = cur.fetchone()[0]
    return cur,count

def onSelect(self,event):
    varList = event.widget
    select = varList.curselection()[0]
    value = varList.get(select)
    conn = sqliste3.connect('phonebook.db')
    with conn:
        cursor = conn.cursor()
        cursor.execute("""SELECT col_fname, col_lname,col_phone,col_email FROM tbl_phonebook WHERE col_fullname = (?)""", [value])
        varBody = cursor.fetchall()

        for data in varBody:
            self.txt_fname.delete(0,END)
            self.txt_fname.insert(0,data[0])
            self.txt_lname.delete(0,END)
            self.txt_lname.insert(0,data[1])
            self.txt_phone.delete(0,END)
            self.txt_phone.insert(0,data[2])
            self.txt_email.delete(0,END)
            self.txt_email.insert(0,data[3])


def addToList(self):
    var_fname = self.txt_fname.get()
    var_lname = self.txt_lname.get()

    var_fname = var_fname.strip()
    var_lname = var_lname.strip()
    var_fname = var_fname.title()
    var_lname = var_lname.title()
    var_fullname = ("{} {}".format(var_fname,var_lname))
    print("var_fullname: {}".format(var_fullname))
    var_phone = self.txt_phone.get().strip()
    var_email = self.txt_email.get().strip()
    if not "@" or not "." in var_email:
        print("incorrect email format!!!")
    if (len(var_fname) >0) and (len(var_lname) >0) and (len(var_phone) >0) and (len(var_email) >0):
            conn = sqlite3.connect('phonebook.db')
            with conn:
                cursor = conn.cursor()

                cursor.execute("""SELECT COUNT(col_fullname) FROM tbl_phonebook WHERE col_fullname = '{}'""".format(var_fullname))
                cursor.execute.fetchone()[0]
                chkName = count
                if chkName == 0:
                    print("chkName: {}".format(chkName))
                    cursor.execute("""INSERT INTO tbl_phonebook (col_fname,col_lname,col_fullname,col_phone, col_email) VALUE (?,?,?,?,?)"""
                    self.lstList.insert(END, var_fullname)
                    onClear(self)
                else:
                    messagebox.showerror("Name Error","'{}' already exist in the database! Please choose a different name.".format(var_fullname))
                    onClear(self)
            conn.commit()
            conn.close()
        else:
            messagebox.showerror("Missing Text Error","Please ensure that there is data in all four feilds.")


def onDelete(self):
    var_select = self.lstList.get(self.lstList.curselection())
    conn - sqlite3.connect('phonebook.db')
    with conn:
        cur = conn.cursor()

        cur.execute("""SELECT COUNT(*) FROM tbl_phonebook""")
        count = cur.fetchone()[0]
        if count > 1:
            confirm = messagebox.askokcancel1("Delete Confirmation", "All information associated with, ({}) \nwill be permenatly deleted from the databasse. \n\nProceed with the deletion request?".format(var_select))
            if confirm:
                conn = sqlite3.connect('phonebook.db')
                with conn:
                    cursor = conn.cursor()
                    cursor.execute("""DELETE FROM tbl_phone WHERE col_fullname = '()'""".format(var.select))
                    
