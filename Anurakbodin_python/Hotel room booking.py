"""
import sqlite3
conn = sqlite3.connect(r"D:\\Anurakbodin_python\\guitest.db")
c = conn.cursor()
c.execute ('''CREATE TABLE user (No integer PRIMARY KEY AUTOINCREMENT,
    username varchar(30) NOT NULL,
    password varchar(30) NOT NULL)''')
c.execute ('''CREATE TABLE room (No integer PRIMARY KEY AUTOINCREMENT,
    category varchar(30) NOT NULL,
    cost integer(10) NOT NULL,
    availability varchar(30) NOT NULL,
    first_name varchar(30) NOT NULL,
    last_name varchar(30) NOT NULL,
    tel varchar(10) NOT NULL,
    first_day integer(10) NOT NULL,
    last_day integer(10) NOT NULL,
    day integer(10) NOT NULL,
    total integer(30) NOT NULL)''')
conn.commit()
conn.close()

def insertTousers (username,password) :
    try :
        conn = sqlite3.connect(r"D:\\Anurakbodin_python\\guitest.db")
        c = conn.cursor()

        sql = '''INSERT INTO user (username,password) VALUES (?,?)'''
        data = (username,password)
        c.execute(sql,data)
        conn.commit()
        c.close()
    except sqlite3.Error as e:
        print('Failed to insert : ',e)
    finally :
        if conn :
            conn.close()
insertTousers("anurak","1234")
insertTousers("temakorn","5678")

def insertTousers (category,cost,availability,first_name,last_name,tel,first_day,last_day,day,total) :
    try :
        conn = sqlite3.connect(r"D:\\Anurakbodin_python\\guitest.db")
        c = conn.cursor()

        sql = '''INSERT INTO room (category,cost,availability,first_name,last_name,tel,first_day,last_day,day,total) VALUES (?,?,?,?,?,?,?,?,?,?)'''
        data = (category,cost,availability,first_name,last_name,tel,first_day,last_day,day,total)
        c.execute(sql,data)
        conn.commit()
        c.close()
    except sqlite3.Error as e:
        print('Failed to insert : ',e)
    finally :

        if conn :
            conn.close()
insertTousers("normal","500","Free","-","-","-","0","0","0","0")
insertTousers("normal","500","Busy","ทอง","แท่ง","0896587632","4","6","2","1000")
insertTousers("normal","500","Free","-","-","-","0","0","0","0")
insertTousers("normal","500","Free","-","-","-","0","0","0","0")
insertTousers("normal","500","Busy","ยิ่ง","ยง","0984562886","25","26","1","500")
insertTousers("special","1000","Busy","สมาน","แผล","0895478899","17","19","3","3000")
insertTousers("special","1000","Busy","ภาณุ","ชิต","0985569912","13","14","1","1000")
insertTousers("special","1000","Free","-","-","-","0","0","0","0")
insertTousers("special","1000","Free","-","-","-","0","0","0","0")
insertTousers("special","1000","Free","-","-","-","0","0","0","0")
"""

from tkinter import ttk
from tkinter import *
from tkinter import messagebox
import tkinter as tk
import sqlite3 as db
import sqlite3
import datetime
import time
import os
from datetime import datetime
window = Tk()
window.title("Hotel Booking Room")
window.option_add("*Font", " JasmineUPC 25")
window.minsize (width=1280 , height=720)
window.iconbitmap('D:\Anurakbodin_python\ico\hotel.ico')

def login():
    win_screen = tk.Frame(window, bg= '#cccc99', bd=5)
    win_screen.place(relx=0.5, rely=0.252, relwidth=0.6, relheight=0.74, anchor='n')
    def check_login():
        user_name = str(user.get())
        if len(user_name) > 0 :
            pass_word = str(pass_w.get())
            nologin = 0
            conn = sqlite3.connect(r"D:\\Anurakbodin_python\\guitest.db")
            c = conn.cursor()
            data = (user_name,pass_word)
            c.execute('select No FROM user WHERE username =? and password =?',data)
            result = c.fetchall()
            for x in result:
                nologin = x[0] #ให้ตัวแปรมีค่าเท่ากับตัวที่อยู่ในตาราง ตามเงื่อนไข
            conn.commit()
            conn.close()
            if nologin > 0 :
                messagebox.showinfo("Completed","Login Completed.")
                login_com()
            else :
                messagebox.showinfo("Incorrect","Passwords is Incorrect.")
        else :
            messagebox.showinfo("Incorrect","Please enter username.")

    frame = tk.Frame(window, bg='#99ffff')
    frame.place(relx = 0.5, rely=0.35, relwidth=0.4, relheight=0.6, anchor='n')
    Label(window, text="Username : ",fg="#000000" ,bg="#FFE4E1").place(relx=0.4, rely=0.4, relwidth=0.1, relheight=0.08, anchor='n')
    Entry(window,textvariable=user).place(relx=0.55, rely=0.4, relwidth=0.2, relheight=0.08, anchor='n')
    Label(window, text="Password : ",fg="#000000" ,bg="#FFE4E1").place(relx=0.4, rely=0.5, relwidth=0.1, relheight=0.08, anchor='n')
    Entry(window,show = 'x', textvariable=pass_w).place(relx=0.55, rely=0.5, relwidth=0.2, relheight=0.08, anchor='n')

    Button(window, text = "ENTER",command = check_login,fg="#000000" ,bg="#FFE4E1", width = 25).place(relx=0.5, rely=0.7, relwidth=0.2, relheight=0.07, anchor='n')
    Button(window, text = "BACK",command = back_login,fg="#000000" ,bg="#FFFACD", width = 25).place(relx=0.5, rely=0.8, relwidth=0.2, relheight=0.07, anchor='n')
########################
def back_login():
    clear()
    start()
########################
def back_regis():
    clear()
    start()
########################
def register():
    win_screen = tk.Frame(window, bg= '#cccc99', bd=5)
    win_screen.place(relx=0.5, rely=0.252, relwidth=0.6, relheight=0.74, anchor='n')
    def check_re():
        user_name2 = str(re_user.get())
        pass_word2 = str(re_pass_w.get())
        con_pass2 = str(re_con.get())
        def re_com():
            npw = len(pass_word2)
            if npw >= 4 :
                if pass_word2 == con_pass2:
                    conn = sqlite3.connect(r'D:\\Anurakbodin_python\\guitest.db')
                    c = conn.cursor()
                    try:
                        data = (user_name2,pass_word2)
                        c.execute('insert into user (username,password) VALUES (?,?)',data)
                        conn.commit()
                        conn.close()   
                    except sqlite3.Error as e:
                        print('Failed to insert : ',e)
                    finally :
                        if conn :
                            conn.close()
                    messagebox.showinfo("Completed","We have saved your information.")
                    start()
                else :
                    messagebox.showinfo("Incorrect","Passwords do not match.")
            else:
                messagebox.showinfo("Incorrect","Please create a password of 4 digits or more.")
        nore = 0
        conn = sqlite3.connect(r"D:\\Anurakbodin_python\\guitest.db")
        c = conn.cursor()
        data = (user_name2,)
        c.execute('select No FROM user WHERE username =?',data)
        result = c.fetchall()
        for x in result:
            nore = x[0] #ให้ตัวแปรมีค่าเท่ากับตัวที่อยู่ในตาราง ตามเงื่อนไข
        conn.commit()
        conn.close()
        if nore > 0 :
            messagebox.showinfo("Username has already.","Please create a new username.")
        else :
            re_com()
    frame = tk.Frame(window, bg='#99ffff')
    frame.place(relx = 0.5, rely=0.35, relwidth=0.4, relheight=0.6, anchor='n')
    Label(window, text="Username : ",fg="#000000" ,bg="#FFE4E1").place(relx=0.4, rely=0.4, relwidth=0.1, relheight=0.08, anchor='n')
    Entry(window,textvariable=re_user).place(relx=0.55, rely=0.4, relwidth=0.2, relheight=0.08, anchor='n')
    Label(window, text="Password : ",fg="#000000" ,bg="#FFE4E1").place(relx=0.4, rely=0.5, relwidth=0.1, relheight=0.08, anchor='n')
    Entry(window, textvariable=re_pass_w).place(relx=0.55, rely=0.5, relwidth=0.2, relheight=0.08, anchor='n')
    Label(window, text="Confirm : ",fg="#000000" ,bg="#FFE4E1").place(relx=0.4, rely=0.6, relwidth=0.1, relheight=0.08, anchor='n')
    Entry(window,show = 'x', textvariable=re_con).place(relx=0.55, rely=0.6, relwidth=0.2, relheight=0.08, anchor='n')

    Button(window, text = "ENTER",command = check_re,fg="#000000" ,bg="#FFE4E1", width = 25).place(relx=0.5, rely=0.7, relwidth=0.2, relheight=0.07, anchor='n')
    Button(window, text = "BACK",command = back_regis,fg="#000000" ,bg="#FFFACD", width = 25).place(relx=0.5, rely=0.8, relwidth=0.2, relheight=0.07, anchor='n')
########################
def login_com():
    win_screen = tk.Frame(window, bg= '#cccc99', bd=5)
    win_screen.place(relx=0.5, rely=0.252, relwidth=0.6, relheight=0.74, anchor='n')
    frame = tk.Frame(window, bg='#99ffff')
    frame.place(relx = 0.5, rely=0.35, relwidth=0.4, relheight=0.6, anchor='n')
    lc1 = Button(window, text='Show',command = show, bg='#00ccff', fg='#000000').place(relx=0.5, rely=0.453, relwidth=0.3, relheight=0.1, anchor='n')
    lc2 = Button(window, text='Booking',command = booking, bg='#00ccff', fg='#000000').place(relx=0.5, rely=0.556, relwidth=0.3, relheight=0.1, anchor='n')
    lc3 = Button(window, text='Cancel Booking',command = cancelbook, bg='#00ccff', fg='#000000').place(relx=0.5, rely=0.659, relwidth=0.3, relheight=0.1, anchor='n')
    lc4 = Button(window, text='Logout',command = log_out, bg='#00ccff', fg='#000000').place(relx=0.5, rely=0.762, relwidth=0.3, relheight=0.1, anchor='n')
#######################


def booking():
    win_screen = tk.Frame(window, bg= '#cccc99', bd=5)
    win_screen.place(relx=0.5, rely=0.252, relwidth=0.6, relheight=0.74, anchor='n')
    frame = tk.Frame(window, bg='#3366ff')
    frame.place(relx = 0.5, rely=0.29, relwidth=0.55, relheight=0.6, anchor='n')
    frame = tk.Frame(window, bg='#00ccff')
    frame.place(relx = 0.5, rely=0.295, relwidth=0.545, relheight=0.42, anchor='n')

    conn = sqlite3.connect(r"D:\\Anurakbodin_python\\guitest.db")
    c = conn.cursor()
    data = 1,
    c.execute('select availability FROM room WHERE No = ?',data)
    result = c.fetchall()
    for x in result:
        ava = str(x).strip("(',)")
    if ava == "Free" :
        r1 = Button(window,text = 1,command = Book1, bg='#00ff00').place(relx=0.28, rely=0.3, relwidth=0.1, relheight=0.2, anchor='n')
    else:
        r1 = Label(window,text = 1, bg='#cc3333').place(relx=0.28, rely=0.3, relwidth=0.1, relheight=0.2, anchor='n')

    data = 2,
    c.execute('select availability FROM room WHERE No = ?',data)
    result = c.fetchall()
    for x in result:
        ava = str(x).strip("(',)")
    if ava == "Free" :
        r2 = Button(window,text = 2,command = Book2, bg='#00ff00').place(relx=0.39, rely=0.3, relwidth=0.1, relheight=0.2, anchor='n')
    else:
        r2 = Label(window,text = 2, bg='#cc3333').place(relx=0.39, rely=0.3, relwidth=0.1, relheight=0.2, anchor='n')

    data = 3,
    c.execute('select availability FROM room WHERE No = ?',data)
    result = c.fetchall()
    for x in result:
        ava = str(x).strip("(',)")
    if ava == "Free" :
        r3 = Button(window,text = 3,command = Book3, bg='#00ff00').place(relx=0.5, rely=0.3, relwidth=0.1, relheight=0.2, anchor='n')
    else:
        r3 = Label(window,text = 3, bg='#cc3333').place(relx=0.5, rely=0.3, relwidth=0.1, relheight=0.2, anchor='n')

    data = 4,
    c.execute('select availability FROM room WHERE No = ?',data)
    result = c.fetchall()
    for x in result:
        ava = str(x).strip("(',)")
    if ava == "Free" :
        r4 = Button(window,text = 4,command = Book4, bg='#00ff00').place(relx=0.61, rely=0.3, relwidth=0.1, relheight=0.2, anchor='n')
    else:
        r4 = Label(window,text = 4, bg='#cc3333').place(relx=0.61, rely=0.3, relwidth=0.1, relheight=0.2, anchor='n')

    data = 5,
    c.execute('select availability FROM room WHERE No = ?',data)
    result = c.fetchall()
    for x in result:
        ava = str(x).strip("(',)")
    if ava == "Free" :
        r5 = Button(window,text = 5,command = Book5, bg='#00ff00').place(relx=0.72, rely=0.3, relwidth=0.1, relheight=0.2, anchor='n')
    else:
        r5 = Label(window,text = 5, bg='#cc3333').place(relx=0.72, rely=0.3, relwidth=0.1, relheight=0.2, anchor='n')

    data = 6,
    c.execute('select availability FROM room WHERE No = ?',data)
    result = c.fetchall()
    for x in result:
        ava = str(x).strip("(',)")
    if ava == "Free" :
        r6 = Button(window,text = 6,command = Book6, bg='#00ff00').place(relx=0.28, rely=0.51, relwidth=0.1, relheight=0.2, anchor='n')
    else:
        r6 = Label(window,text = 6, bg='#cc3333').place(relx=0.28, rely=0.51, relwidth=0.1, relheight=0.2, anchor='n')

    data = 7,
    c.execute('select availability FROM room WHERE No = ?',data)
    result = c.fetchall()
    for x in result:
        ava = str(x).strip("(',)")
    if ava == "Free" :
        r7 = Button(window,text = 7,command = Book7, bg='#00ff00').place(relx=0.39, rely=0.51, relwidth=0.1, relheight=0.2, anchor='n')
    else:
        r7 = Label(window,text = 7, bg='#cc3333').place(relx=0.39, rely=0.51, relwidth=0.1, relheight=0.2, anchor='n')

        data = 8,
    c.execute('select availability FROM room WHERE No = ?',data)
    result = c.fetchall()
    for x in result:
        ava = str(x).strip("(',)")
    if ava == "Free" :
        r8 = Button(window,text = 8,command = Book8, bg='#00ff00').place(relx=0.5, rely=0.51, relwidth=0.1, relheight=0.2, anchor='n')
    else:
        r8 = Label(window,text = 8, bg='#cc3333').place(relx=0.5, rely=0.51, relwidth=0.1, relheight=0.2, anchor='n')
    
    data = 9,
    c.execute('select availability FROM room WHERE No = ?',data)
    result = c.fetchall()
    for x in result:
        ava = str(x).strip("(',)")
    if ava == "Free" :
        r9 = Button(window,text = 9,command = Book9, bg='#00ff00').place(relx=0.61, rely=0.51, relwidth=0.1, relheight=0.2, anchor='n')
    else:
        r9 = Label(window,text = 9, bg='#cc3333').place(relx=0.61, rely=0.51, relwidth=0.1, relheight=0.2, anchor='n')
    
    data = 10,
    c.execute('select availability FROM room WHERE No = ?',data)
    result = c.fetchall()
    for x in result:
        ava = str(x).strip("(',)")
    if ava == "Free" :
        r10 = Button(window,text = 10,command = Book10, bg='#00ff00').place(relx=0.72, rely=0.51, relwidth=0.1, relheight=0.2, anchor='n')
    else:
        r10 = Label(window,text = 10, bg='#cc3333').place(relx=0.72, rely=0.51, relwidth=0.1, relheight=0.2, anchor='n')
    Label(window,text = "Menu BOOKING", bg='#00ccff').place(relx=0.35, rely=0.75, relwidth=0.13, relheight=0.1, anchor='n')
    Label(window,text = "Select Green Room", bg='#00ff00').place(relx=0.65, rely=0.75, relwidth=0.13, relheight=0.1, anchor='n')
    Button(window,text = "BACK",command = login_com, bg='#ffcc99').place(relx=0.5, rely=0.75, relwidth=0.1, relheight=0.1, anchor='n')
#######################
def back_book():#back book
    clear()
    booking()
########################
def Book1():
    win_screen = tk.Frame(window, bg= '#cccc99', bd=5)
    win_screen.place(relx=0.5, rely=0.252, relwidth=0.6, relheight=0.74, anchor='n')
    def booking1():
        win_screen = tk.Frame(window, bg= '#cccc99', bd=5)
        win_screen.place(relx=0.5, rely=0.252, relwidth=0.6, relheight=0.74, anchor='n')
        frame = tk.Frame(window, bg='#990000')
        frame.place(relx = 0.5, rely=0.28, relwidth=0.55, relheight=0.7, anchor='n')
        frame = tk.Frame(window, bg='#99ffff')
        frame.place(relx = 0.5, rely=0.3, relwidth=0.53, relheight=0.66, anchor='n')

        def comfirm1():
            firstname = str(fn.get())
            if len(firstname) > 0 :
                lastname =str(ln.get())
                if len(lastname) > 0 :
                    telephone = str(tel.get())
                    if len(telephone) == 10:
                        firstday = int(fd.get())
                        numday = int(nd.get())
                        lastday = firstday + numday 
                        if lastday <= 31:
                            win_screen = tk.Frame(window, bg= '#f0f0f0', bd=5)
                            win_screen.place(relx=0.5, rely=0.28, relwidth=0.6, relheight=0.8, anchor='n')
                            frame = tk.Frame(window, bg='#99ffff')
                            frame.place(relx = 0.5, rely=0.3, relwidth=0.53, relheight=0.66, anchor='n')
                            total = 500*numday
                            Label(window, text=("Total=",total),bg='#ff66ff').place(relx=0.5, rely=0.4, relwidth=0.2, relheight=0.1, anchor='n')
                            Label(window, text=("Confirm Booking"),bg='#ff66ff').place(relx=0.5, rely=0.5, relwidth=0.2, relheight=0.08, anchor='n')
                            def comfirm_book():
                                conn = sqlite3.connect(r"D:\\Anurakbodin_python\\guitest.db")
                                c = conn.cursor()
                                try:
                                    data = ("Busy",str(firstname),str(lastname),str(telephone),int(firstday),int(lastday),int(numday),int(total),1)
                                    c.execute('''UPDATE room SET availability =?,first_name =?,last_name=?,tel=?,first_day=?,last_day=?,day=?,total=? WHERE No = ?''',data)
                                    conn.commit()
                                    conn.close()
                                except sqlite3.Error as e:
                                    print('Failed to insert : ',e)
                                finally :
                                    if conn :
                                        conn.close()
                                messagebox.showinfo("Completed","Booking Successful.")
                                back_book()

                            Button(window,text = "ENTER",command = comfirm_book, bg='#999999').place(relx=0.4, rely=0.7, relwidth=0.1, relheight=0.1, anchor='n')
                            Button(window,text = "CANCEL",command = booking1, bg='#999999').place(relx=0.6, rely=0.7, relwidth=0.1, relheight=0.1, anchor='n')
                        else:
                            messagebox.showinfo("Incompleted","The reservation period is not later than this month.")
                    else :
                        messagebox.showinfo("Incompleted","Please fill out all phone numbers.")
                else:
                    messagebox.showinfo("Incompleted","Please enter your last name") 
            else :
                messagebox.showinfo("Incompleted","Please enter your first name")

        def number(S): #ฟังก์ชันพิมได้เฉพาะค่าตัวเลข
            if S.isdigit():
                return True
            window.bell()
            return False
        Nn = (window.register(number), '%S')
        
        def letters(S):
            if S.isalpha():
                return True
            window.bell()
            return False
        Ll = (window.register(letters), '%S')

        Label(window, text="First Name : ", bg='#99ffff').place(relx=0.37, rely=0.34, relwidth=0.1, relheight=0.05, anchor='n')
        f = Entry(window, textvariable=fn, validate='key', vcmd=Ll).place(relx=0.58, rely=0.34, relwidth=0.25, relheight=0.05, anchor='n')
        Label(window, text="Last Name : ", bg='#99ffff').place(relx=0.37, rely=0.44, relwidth=0.1, relheight=0.05, anchor='n')
        l = Entry(window, textvariable=ln, validate='key', vcmd=Ll).place(relx=0.58, rely=0.44, relwidth=0.25, relheight=0.05, anchor='n')

        Label(window, text="Tel : ", bg='#99ffff').place(relx=0.37, rely=0.54, relwidth=0.1, relheight=0.05, anchor='n')
        t = Entry(window, textvariable=tel, validate='key', vcmd=Nn).place(relx=0.58, rely=0.54, relwidth=0.25, relheight=0.05, anchor='n')

        Label(window, text="First day : ", bg='#99ffff').place(relx=0.37, rely=0.64, relwidth=0.1, relheight=0.05, anchor='n')
        fd = Spinbox(window, from_= 1, to = 31)
        fd.place(relx=0.58, rely=0.64, relwidth=0.25, relheight=0.05, anchor='n') 

        Label(window, text="Number of days : ", bg='#99ffff').place(relx=0.37, rely=0.74, relwidth=0.1, relheight=0.05, anchor='n')
        nd = Spinbox(window, from_= 1, to = 7)
        nd.place(relx=0.58, rely=0.74, relwidth=0.25, relheight=0.05, anchor='n')

        Button(window,text = "ENTER",command = comfirm1, bg='#999999').place(relx=0.4, rely=0.85, relwidth=0.1, relheight=0.1, anchor='n')
        Button(window,text = "BACK",command = Book1, bg='#999999').place(relx=0.6, rely=0.85, relwidth=0.1, relheight=0.1, anchor='n')

    Label(window,text = "No 1", bg= '#fff000').place(relx=0.5, rely=0.3, relwidth=0.2, relheight=0.1, anchor='n')
    Label(window,text = "category ->", bg= '#3399ff').place(relx=0.45, rely=0.42, relwidth=0.2, relheight=0.1, anchor='n')
    Label(window,text = "cost ->", bg= '#66ccff').place(relx=0.45, rely=0.52, relwidth=0.2, relheight=0.1, anchor='n')
    Label(window,text = "availability ->", bg= '#99ccff').place(relx=0.45, rely=0.62, relwidth=0.2, relheight=0.1, anchor='n')

    conn = sqlite3.connect(r"D:\\Anurakbodin_python\\guitest.db")
    c = conn.cursor()
    c.execute('select category FROM room WHERE No = 1')
    result = c.fetchall()
    for x in result:
        Label(window,text = x, bg='#ff00ff').place(relx=0.6, rely=0.42, relwidth=0.1, relheight=0.1, anchor='n')
    c.execute('select cost FROM room WHERE No = 1')
    result = c.fetchall()
    for x in result:
        Label(window,text = x, bg='#ff66ff').place(relx=0.6, rely=0.52, relwidth=0.1, relheight=0.1, anchor='n')
    c.execute('select availability FROM room WHERE No = 1')
    result = c.fetchall()
    for x in result:
        Label(window,text = x, bg='#ff99ff').place(relx=0.6, rely=0.62, relwidth=0.1, relheight=0.1, anchor='n')
    Button(window,text = "Booking",command = booking1, bg='#999999').place(relx=0.4, rely=0.8, relwidth=0.1, relheight=0.1, anchor='n')
    Button(window,text = "BACK",command = back_book, bg='#999999').place(relx=0.6, rely=0.8, relwidth=0.1, relheight=0.1, anchor='n')
########################
def Book2():
    win_screen = tk.Frame(window, bg= '#cccc99', bd=5)
    win_screen.place(relx=0.5, rely=0.252, relwidth=0.6, relheight=0.74, anchor='n')
    def booking2():
        win_screen = tk.Frame(window, bg= '#cccc99', bd=5)
        win_screen.place(relx=0.5, rely=0.252, relwidth=0.6, relheight=0.74, anchor='n')
        frame = tk.Frame(window, bg='#990000')
        frame.place(relx = 0.5, rely=0.28, relwidth=0.55, relheight=0.7, anchor='n')
        frame = tk.Frame(window, bg='#99ffff')
        frame.place(relx = 0.5, rely=0.3, relwidth=0.53, relheight=0.66, anchor='n')

        def comfirm2():
            firstname = str(fn.get())
            if len(firstname) > 0 :
                lastname =str(ln.get())
                if len(lastname) > 0 :
                    telephone = str(tel.get())
                    if len(telephone) == 10:
                        firstday = int(fd.get())
                        numday = int(nd.get())
                        lastday = firstday + numday 
                        if lastday <= 31:
                            win_screen = tk.Frame(window, bg= '#f0f0f0', bd=5)
                            win_screen.place(relx=0.5, rely=0.28, relwidth=0.6, relheight=0.8, anchor='n')
                            frame = tk.Frame(window, bg='#99ffff')
                            frame.place(relx = 0.5, rely=0.3, relwidth=0.53, relheight=0.66, anchor='n')
                            total = 500*numday
                            Label(window, text=("Total=",total),bg='#ff66ff').place(relx=0.5, rely=0.4, relwidth=0.2, relheight=0.1, anchor='n')
                            Label(window, text=("Confirm Booking"),bg='#ff66ff').place(relx=0.5, rely=0.5, relwidth=0.2, relheight=0.08, anchor='n')
                            def comfirm_book():
                                conn = sqlite3.connect(r"D:\\Anurakbodin_python\\guitest.db")
                                c = conn.cursor()
                                try:
                                    data = ("Busy",str(firstname),str(lastname),str(telephone),int(firstday),int(lastday),int(numday),int(total),2)
                                    c.execute('''UPDATE room SET availability =?,first_name =?,last_name=?,tel=?,first_day=?,last_day=?,day=?,total=? WHERE No = ?''',data)
                                    conn.commit()
                                    conn.close()
                                except sqlite3.Error as e:
                                    print('Failed to insert : ',e)
                                finally :
                                    if conn :
                                        conn.close()
                                messagebox.showinfo("Completed","Booking Successful.")
                                back_book()
                            Button(window,text = "ENTER",command = comfirm_book, bg='#999999').place(relx=0.4, rely=0.7, relwidth=0.1, relheight=0.1, anchor='n')
                            Button(window,text = "CANCEL",command = booking2, bg='#999999').place(relx=0.6, rely=0.7, relwidth=0.1, relheight=0.1, anchor='n')
                        else:
                            messagebox.showinfo("Incompleted","The reservation period is not later than this month.")
                    else :
                        messagebox.showinfo("Incompleted","Please fill out all phone numbers.")
                else:
                    messagebox.showinfo("Incompleted","Please enter your last name") 
            else :
                messagebox.showinfo("Incompleted","Please enter your first name")

        def number(S): #ฟังก์ชันพิมได้เฉพาะค่าตัวเลข
            if S.isdigit():
                return True
            window.bell()
            return False
        Nn = (window.register(number), '%S')
        
        def letters(S):
            if S.isalpha():
                return True
            window.bell()
            return False
        Ll = (window.register(letters), '%S')

        Label(window, text="First Name : ", bg='#99ffff').place(relx=0.37, rely=0.34, relwidth=0.1, relheight=0.05, anchor='n')
        f = Entry(window, textvariable=fn, validate='key', vcmd=Ll).place(relx=0.58, rely=0.34, relwidth=0.25, relheight=0.05, anchor='n')
        Label(window, text="Last Name : ", bg='#99ffff').place(relx=0.37, rely=0.44, relwidth=0.1, relheight=0.05, anchor='n')
        l = Entry(window, textvariable=ln, validate='key', vcmd=Ll).place(relx=0.58, rely=0.44, relwidth=0.25, relheight=0.05, anchor='n')

        Label(window, text="Tel : ", bg='#99ffff').place(relx=0.37, rely=0.54, relwidth=0.1, relheight=0.05, anchor='n')
        t = Entry(window, textvariable=tel, validate='key', vcmd=Nn).place(relx=0.58, rely=0.54, relwidth=0.25, relheight=0.05, anchor='n')

        Label(window, text="First day : ", bg='#99ffff').place(relx=0.37, rely=0.64, relwidth=0.1, relheight=0.05, anchor='n')
        fd = Spinbox(window, from_= 1, to = 31)
        fd.place(relx=0.58, rely=0.64, relwidth=0.25, relheight=0.05, anchor='n') 

        Label(window, text="Number of days : ", bg='#99ffff').place(relx=0.37, rely=0.74, relwidth=0.1, relheight=0.05, anchor='n')
        nd = Spinbox(window, from_= 1, to = 7)
        nd.place(relx=0.58, rely=0.74, relwidth=0.25, relheight=0.05, anchor='n')

        Button(window,text = "ENTER",command = comfirm2, bg='#999999').place(relx=0.4, rely=0.85, relwidth=0.1, relheight=0.1, anchor='n')
        Button(window,text = "BACK",command = Book2, bg='#999999').place(relx=0.6, rely=0.85, relwidth=0.1, relheight=0.1, anchor='n')

    Label(window,text = "No 2", bg= '#fff000').place(relx=0.5, rely=0.3, relwidth=0.2, relheight=0.1, anchor='n')
    Label(window,text = "category ->", bg= '#3399ff').place(relx=0.45, rely=0.42, relwidth=0.2, relheight=0.1, anchor='n')
    Label(window,text = "cost ->", bg= '#66ccff').place(relx=0.45, rely=0.52, relwidth=0.2, relheight=0.1, anchor='n')
    Label(window,text = "availability ->", bg= '#99ccff').place(relx=0.45, rely=0.62, relwidth=0.2, relheight=0.1, anchor='n')

    conn = sqlite3.connect(r"D:\\Anurakbodin_python\\guitest.db")
    c = conn.cursor()
    c.execute('select category FROM room WHERE No = 2')
    result = c.fetchall()
    for x in result:
        Label(window,text = x, bg='#ff00ff').place(relx=0.6, rely=0.42, relwidth=0.1, relheight=0.1, anchor='n')
    c.execute('select cost FROM room WHERE No = 2')
    result = c.fetchall()
    for x in result:
        Label(window,text = x, bg='#ff66ff').place(relx=0.6, rely=0.52, relwidth=0.1, relheight=0.1, anchor='n')
    c.execute('select availability FROM room WHERE No = 2')
    result = c.fetchall()
    for x in result:
        Label(window,text = x, bg='#ff99ff').place(relx=0.6, rely=0.62, relwidth=0.1, relheight=0.1, anchor='n')
    Button(window,text = "Booking",command = booking2, bg='#999999').place(relx=0.4, rely=0.8, relwidth=0.1, relheight=0.1, anchor='n')
    Button(window,text = "BACK",command = back_book, bg='#999999').place(relx=0.6, rely=0.8, relwidth=0.1, relheight=0.1, anchor='n')
########################
def Book3():
    win_screen = tk.Frame(window, bg= '#cccc99', bd=5)
    win_screen.place(relx=0.5, rely=0.252, relwidth=0.6, relheight=0.74, anchor='n')
    def booking3():
        win_screen = tk.Frame(window, bg= '#cccc99', bd=5)
        win_screen.place(relx=0.5, rely=0.252, relwidth=0.6, relheight=0.74, anchor='n')
        frame = tk.Frame(window, bg='#990000')
        frame.place(relx = 0.5, rely=0.28, relwidth=0.55, relheight=0.7, anchor='n')
        frame = tk.Frame(window, bg='#99ffff')
        frame.place(relx = 0.5, rely=0.3, relwidth=0.53, relheight=0.66, anchor='n')

        def comfirm3():
            firstname = str(fn.get())
            if len(firstname) > 0 :
                lastname =str(ln.get())
                if len(lastname) > 0 :
                    telephone = str(tel.get())
                    if len(telephone) == 10:
                        firstday = int(fd.get())
                        numday = int(nd.get())
                        lastday = firstday + numday 
                        if lastday <= 31:
                            win_screen = tk.Frame(window, bg= '#f0f0f0', bd=5)
                            win_screen.place(relx=0.5, rely=0.28, relwidth=0.6, relheight=0.8, anchor='n')
                            frame = tk.Frame(window, bg='#99ffff')
                            frame.place(relx = 0.5, rely=0.3, relwidth=0.53, relheight=0.66, anchor='n')
                            total = 500*numday
                            Label(window, text=("Total=",total),bg='#ff66ff').place(relx=0.5, rely=0.4, relwidth=0.2, relheight=0.1, anchor='n')
                            Label(window, text=("Confirm Booking"),bg='#ff66ff').place(relx=0.5, rely=0.5, relwidth=0.2, relheight=0.08, anchor='n')
                            def comfirm_book():
                                conn = sqlite3.connect(r"D:\\Anurakbodin_python\\guitest.db")
                                c = conn.cursor()
                                try:
                                    data = ("Busy",str(firstname),str(lastname),str(telephone),int(firstday),int(lastday),int(numday),int(total),3)
                                    c.execute('''UPDATE room SET availability =?,first_name =?,last_name=?,tel=?,first_day=?,last_day=?,day=?,total=? WHERE No = ?''',data)
                                    conn.commit()
                                    conn.close()
                                except sqlite3.Error as e:
                                    print('Failed to insert : ',e)
                                finally :
                                    if conn :
                                        conn.close()
                                messagebox.showinfo("Completed","Booking Successful.")
                                back_book()
                            Button(window,text = "ENTER",command = comfirm_book, bg='#999999').place(relx=0.4, rely=0.7, relwidth=0.1, relheight=0.1, anchor='n')
                            Button(window,text = "CANCEL",command = booking3, bg='#999999').place(relx=0.6, rely=0.7, relwidth=0.1, relheight=0.1, anchor='n')
                        else:
                            messagebox.showinfo("Incompleted","The reservation period is not later than this month.")
                    else :
                        messagebox.showinfo("Incompleted","Please fill out all phone numbers.")
                else:
                    messagebox.showinfo("Incompleted","Please enter your last name") 
            else :
                messagebox.showinfo("Incompleted","Please enter your first name")

        def number(S): #ฟังก์ชันพิมได้เฉพาะค่าตัวเลข
            if S.isdigit():
                return True
            window.bell()
            return False
        Nn = (window.register(number), '%S')
        
        def letters(S):
            if S.isalpha():
                return True
            window.bell()
            return False
        Ll = (window.register(letters), '%S')

        Label(window, text="First Name : ", bg='#99ffff').place(relx=0.37, rely=0.34, relwidth=0.1, relheight=0.05, anchor='n')
        f = Entry(window, textvariable=fn, validate='key', vcmd=Ll).place(relx=0.58, rely=0.34, relwidth=0.25, relheight=0.05, anchor='n')
        Label(window, text="Last Name : ", bg='#99ffff').place(relx=0.37, rely=0.44, relwidth=0.1, relheight=0.05, anchor='n')
        l = Entry(window, textvariable=ln, validate='key', vcmd=Ll).place(relx=0.58, rely=0.44, relwidth=0.25, relheight=0.05, anchor='n')

        Label(window, text="Tel : ", bg='#99ffff').place(relx=0.37, rely=0.54, relwidth=0.1, relheight=0.05, anchor='n')
        t = Entry(window, textvariable=tel, validate='key', vcmd=Nn).place(relx=0.58, rely=0.54, relwidth=0.25, relheight=0.05, anchor='n')

        Label(window, text="First day : ", bg='#99ffff').place(relx=0.37, rely=0.64, relwidth=0.1, relheight=0.05, anchor='n')
        fd = Spinbox(window, from_= 1, to = 31)
        fd.place(relx=0.58, rely=0.64, relwidth=0.25, relheight=0.05, anchor='n') 

        Label(window, text="Number of days : ", bg='#99ffff').place(relx=0.37, rely=0.74, relwidth=0.1, relheight=0.05, anchor='n')
        nd = Spinbox(window, from_= 1, to = 7)
        nd.place(relx=0.58, rely=0.74, relwidth=0.25, relheight=0.05, anchor='n')

        Button(window,text = "ENTER",command = comfirm3, bg='#999999').place(relx=0.4, rely=0.85, relwidth=0.1, relheight=0.1, anchor='n')
        Button(window,text = "BACK",command = Book3, bg='#999999').place(relx=0.6, rely=0.85, relwidth=0.1, relheight=0.1, anchor='n')

    Label(window,text = "No 3", bg= '#fff000').place(relx=0.5, rely=0.3, relwidth=0.2, relheight=0.1, anchor='n')
    Label(window,text = "category ->", bg= '#3399ff').place(relx=0.45, rely=0.42, relwidth=0.2, relheight=0.1, anchor='n')
    Label(window,text = "cost ->", bg= '#66ccff').place(relx=0.45, rely=0.52, relwidth=0.2, relheight=0.1, anchor='n')
    Label(window,text = "availability ->", bg= '#99ccff').place(relx=0.45, rely=0.62, relwidth=0.2, relheight=0.1, anchor='n')

    conn = sqlite3.connect(r"D:\\Anurakbodin_python\\guitest.db")
    c = conn.cursor()
    c.execute('select category FROM room WHERE No = 3')
    result = c.fetchall()
    for x in result:
        Label(window,text = x, bg='#ff00ff').place(relx=0.6, rely=0.42, relwidth=0.1, relheight=0.1, anchor='n')
    c.execute('select cost FROM room WHERE No = 3')
    result = c.fetchall()
    for x in result:
        Label(window,text = x, bg='#ff66ff').place(relx=0.6, rely=0.52, relwidth=0.1, relheight=0.1, anchor='n')
    c.execute('select availability FROM room WHERE No = 3')
    result = c.fetchall()
    for x in result:
        Label(window,text = x, bg='#ff99ff').place(relx=0.6, rely=0.62, relwidth=0.1, relheight=0.1, anchor='n')
    Button(window,text = "Booking",command = booking3, bg='#999999').place(relx=0.4, rely=0.8, relwidth=0.1, relheight=0.1, anchor='n')
    Button(window,text = "BACK",command = back_book, bg='#999999').place(relx=0.6, rely=0.8, relwidth=0.1, relheight=0.1, anchor='n')
########################
def Book4():
    win_screen = tk.Frame(window, bg= '#cccc99', bd=5)
    win_screen.place(relx=0.5, rely=0.252, relwidth=0.6, relheight=0.74, anchor='n')
    def booking4():
        win_screen = tk.Frame(window, bg= '#cccc99', bd=5)
        win_screen.place(relx=0.5, rely=0.252, relwidth=0.6, relheight=0.74, anchor='n')
        frame = tk.Frame(window, bg='#990000')
        frame.place(relx = 0.5, rely=0.28, relwidth=0.55, relheight=0.7, anchor='n')
        frame = tk.Frame(window, bg='#99ffff')
        frame.place(relx = 0.5, rely=0.3, relwidth=0.53, relheight=0.66, anchor='n')

        def comfirm4():
            firstname = str(fn.get())
            if len(firstname) > 0 :
                lastname =str(ln.get())
                if len(lastname) > 0 :
                    telephone = str(tel.get())
                    if len(telephone) == 10:
                        firstday = int(fd.get())
                        numday = int(nd.get())
                        lastday = firstday + numday 
                        if lastday <= 31:
                            win_screen = tk.Frame(window, bg= '#f0f0f0', bd=5)
                            win_screen.place(relx=0.5, rely=0.28, relwidth=0.6, relheight=0.8, anchor='n')
                            frame = tk.Frame(window, bg='#99ffff')
                            frame.place(relx = 0.5, rely=0.3, relwidth=0.53, relheight=0.66, anchor='n')
                            total = 500*numday
                            Label(window, text=("Total=",total),bg='#ff66ff').place(relx=0.5, rely=0.4, relwidth=0.2, relheight=0.1, anchor='n')
                            Label(window, text=("Confirm Booking"),bg='#ff66ff').place(relx=0.5, rely=0.5, relwidth=0.2, relheight=0.08, anchor='n')
                            def comfirm_book():
                                conn = sqlite3.connect(r"D:\\Anurakbodin_python\\guitest.db")
                                c = conn.cursor()
                                try:
                                    data = ("Busy",str(firstname),str(lastname),str(telephone),int(firstday),int(lastday),int(numday),int(total),4)
                                    c.execute('''UPDATE room SET availability =?,first_name =?,last_name=?,tel=?,first_day=?,last_day=?,day=?,total=? WHERE No = ?''',data)
                                    conn.commit()
                                    conn.close()
                                except sqlite3.Error as e:
                                    print('Failed to insert : ',e)
                                finally :
                                    if conn :
                                        conn.close()
                                messagebox.showinfo("Completed","Booking Successful.")
                                back_book()
                            Button(window,text = "ENTER",command = comfirm_book, bg='#999999').place(relx=0.4, rely=0.7, relwidth=0.1, relheight=0.1, anchor='n')
                            Button(window,text = "CANCEL",command = booking4, bg='#999999').place(relx=0.6, rely=0.7, relwidth=0.1, relheight=0.1, anchor='n')
                        else:
                            messagebox.showinfo("Incompleted","The reservation period is not later than this month.")
                    else :
                        messagebox.showinfo("Incompleted","Please fill out all phone numbers.")
                else:
                    messagebox.showinfo("Incompleted","Please enter your last name") 
            else :
                messagebox.showinfo("Incompleted","Please enter your first name")

        def number(S): #ฟังก์ชันพิมได้เฉพาะค่าตัวเลข
            if S.isdigit():
                return True
            window.bell()
            return False
        Nn = (window.register(number), '%S')
        
        def letters(S):
            if S.isalpha():
                return True
            window.bell()
            return False
        Ll = (window.register(letters), '%S')

        Label(window, text="First Name : ", bg='#99ffff').place(relx=0.37, rely=0.34, relwidth=0.1, relheight=0.05, anchor='n')
        f = Entry(window, textvariable=fn, validate='key', vcmd=Ll).place(relx=0.58, rely=0.34, relwidth=0.25, relheight=0.05, anchor='n')
        Label(window, text="Last Name : ", bg='#99ffff').place(relx=0.37, rely=0.44, relwidth=0.1, relheight=0.05, anchor='n')
        l = Entry(window, textvariable=ln, validate='key', vcmd=Ll).place(relx=0.58, rely=0.44, relwidth=0.25, relheight=0.05, anchor='n')

        Label(window, text="Tel : ", bg='#99ffff').place(relx=0.37, rely=0.54, relwidth=0.1, relheight=0.05, anchor='n')
        t = Entry(window, textvariable=tel, validate='key', vcmd=Nn).place(relx=0.58, rely=0.54, relwidth=0.25, relheight=0.05, anchor='n')

        Label(window, text="First day : ", bg='#99ffff').place(relx=0.37, rely=0.64, relwidth=0.1, relheight=0.05, anchor='n')
        fd = Spinbox(window, from_= 1, to = 31)
        fd.place(relx=0.58, rely=0.64, relwidth=0.25, relheight=0.05, anchor='n') 

        Label(window, text="Number of days : ", bg='#99ffff').place(relx=0.37, rely=0.74, relwidth=0.1, relheight=0.05, anchor='n')
        nd = Spinbox(window, from_= 1, to = 7)
        nd.place(relx=0.58, rely=0.74, relwidth=0.25, relheight=0.05, anchor='n')

        Button(window,text = "ENTER",command = comfirm4, bg='#999999').place(relx=0.4, rely=0.85, relwidth=0.1, relheight=0.1, anchor='n')
        Button(window,text = "BACK",command = Book4, bg='#999999').place(relx=0.6, rely=0.85, relwidth=0.1, relheight=0.1, anchor='n')

    Label(window,text = "No 4", bg= '#fff000').place(relx=0.5, rely=0.3, relwidth=0.2, relheight=0.1, anchor='n')
    Label(window,text = "category ->", bg= '#3399ff').place(relx=0.45, rely=0.42, relwidth=0.2, relheight=0.1, anchor='n')
    Label(window,text = "cost ->", bg= '#66ccff').place(relx=0.45, rely=0.52, relwidth=0.2, relheight=0.1, anchor='n')
    Label(window,text = "availability ->", bg= '#99ccff').place(relx=0.45, rely=0.62, relwidth=0.2, relheight=0.1, anchor='n')

    conn = sqlite3.connect(r"D:\\Anurakbodin_python\\guitest.db")
    c = conn.cursor()
    c.execute('select category FROM room WHERE No = 4')
    result = c.fetchall()
    for x in result:
        Label(window,text = x, bg='#ff00ff').place(relx=0.6, rely=0.42, relwidth=0.1, relheight=0.1, anchor='n')
    c.execute('select cost FROM room WHERE No = 4')
    result = c.fetchall()
    for x in result:
        Label(window,text = x, bg='#ff66ff').place(relx=0.6, rely=0.52, relwidth=0.1, relheight=0.1, anchor='n')
    c.execute('select availability FROM room WHERE No = 4')
    result = c.fetchall()
    for x in result:
        Label(window,text = x, bg='#ff99ff').place(relx=0.6, rely=0.62, relwidth=0.1, relheight=0.1, anchor='n')
    Button(window,text = "Booking",command = booking4, bg='#999999').place(relx=0.4, rely=0.8, relwidth=0.1, relheight=0.1, anchor='n')
    Button(window,text = "BACK",command = back_book, bg='#999999').place(relx=0.6, rely=0.8, relwidth=0.1, relheight=0.1, anchor='n')
########################
def Book5():
    win_screen = tk.Frame(window, bg= '#cccc99', bd=5)
    win_screen.place(relx=0.5, rely=0.252, relwidth=0.6, relheight=0.74, anchor='n')
    def booking5():
        win_screen = tk.Frame(window, bg= '#cccc99', bd=5)
        win_screen.place(relx=0.5, rely=0.252, relwidth=0.6, relheight=0.74, anchor='n')
        frame = tk.Frame(window, bg='#990000')
        frame.place(relx = 0.5, rely=0.28, relwidth=0.55, relheight=0.7, anchor='n')
        frame = tk.Frame(window, bg='#99ffff')
        frame.place(relx = 0.5, rely=0.3, relwidth=0.53, relheight=0.66, anchor='n')

        def comfirm5():
            firstname = str(fn.get())
            if len(firstname) > 0 :
                lastname =str(ln.get())
                if len(lastname) > 0 :
                    telephone = str(tel.get())
                    if len(telephone) == 10:
                        firstday = int(fd.get())
                        numday = int(nd.get())
                        lastday = firstday + numday 
                        if lastday <= 31:
                            win_screen = tk.Frame(window, bg= '#f0f0f0', bd=5)
                            win_screen.place(relx=0.5, rely=0.28, relwidth=0.6, relheight=0.8, anchor='n')
                            frame = tk.Frame(window, bg='#99ffff')
                            frame.place(relx = 0.5, rely=0.3, relwidth=0.53, relheight=0.66, anchor='n')
                            total = 500*numday
                            Label(window, text=("Total=",total),bg='#ff66ff').place(relx=0.5, rely=0.4, relwidth=0.2, relheight=0.1, anchor='n')
                            Label(window, text=("Confirm Booking"),bg='#ff66ff').place(relx=0.5, rely=0.5, relwidth=0.2, relheight=0.08, anchor='n')
                            def comfirm_book():
                                conn = sqlite3.connect(r"D:\\Anurakbodin_python\\guitest.db")
                                c = conn.cursor()
                                try:
                                    data = ("Busy",str(firstname),str(lastname),str(telephone),int(firstday),int(lastday),int(numday),int(total),5)
                                    c.execute('''UPDATE room SET availability =?,first_name =?,last_name=?,tel=?,first_day=?,last_day=?,day=?,total=? WHERE No = ?''',data)
                                    conn.commit()
                                    conn.close()
                                except sqlite3.Error as e:
                                    print('Failed to insert : ',e)
                                finally :
                                    if conn :
                                        conn.close()
                                messagebox.showinfo("Completed","Booking Successful.")
                                back_book()
                            Button(window,text = "ENTER",command = comfirm_book, bg='#999999').place(relx=0.4, rely=0.7, relwidth=0.1, relheight=0.1, anchor='n')
                            Button(window,text = "CANCEL",command = booking5, bg='#999999').place(relx=0.6, rely=0.7, relwidth=0.1, relheight=0.1, anchor='n')
                        else:
                            messagebox.showinfo("Incompleted","The reservation period is not later than this month.")
                    else :
                        messagebox.showinfo("Incompleted","Please fill out all phone numbers.")
                else:
                    messagebox.showinfo("Incompleted","Please enter your last name") 
            else :
                messagebox.showinfo("Incompleted","Please enter your first name")

        def number(S): #ฟังก์ชันพิมได้เฉพาะค่าตัวเลข
            if S.isdigit():
                return True
            window.bell()
            return False
        Nn = (window.register(number), '%S')
        
        def letters(S):
            if S.isalpha():
                return True
            window.bell()
            return False
        Ll = (window.register(letters), '%S')

        Label(window, text="First Name : ", bg='#99ffff').place(relx=0.37, rely=0.34, relwidth=0.1, relheight=0.05, anchor='n')
        f = Entry(window, textvariable=fn, validate='key', vcmd=Ll).place(relx=0.58, rely=0.34, relwidth=0.25, relheight=0.05, anchor='n')
        Label(window, text="Last Name : ", bg='#99ffff').place(relx=0.37, rely=0.44, relwidth=0.1, relheight=0.05, anchor='n')
        l = Entry(window, textvariable=ln, validate='key', vcmd=Ll).place(relx=0.58, rely=0.44, relwidth=0.25, relheight=0.05, anchor='n')

        Label(window, text="Tel : ", bg='#99ffff').place(relx=0.37, rely=0.54, relwidth=0.1, relheight=0.05, anchor='n')
        t = Entry(window, textvariable=tel, validate='key', vcmd=Nn).place(relx=0.58, rely=0.54, relwidth=0.25, relheight=0.05, anchor='n')

        Label(window, text="First day : ", bg='#99ffff').place(relx=0.37, rely=0.64, relwidth=0.1, relheight=0.05, anchor='n')
        fd = Spinbox(window, from_= 1, to = 31)
        fd.place(relx=0.58, rely=0.64, relwidth=0.25, relheight=0.05, anchor='n') 

        Label(window, text="Number of days : ", bg='#99ffff').place(relx=0.37, rely=0.74, relwidth=0.1, relheight=0.05, anchor='n')
        nd = Spinbox(window, from_= 1, to = 7)
        nd.place(relx=0.58, rely=0.74, relwidth=0.25, relheight=0.05, anchor='n')

        Button(window,text = "ENTER",command = comfirm5, bg='#999999').place(relx=0.4, rely=0.85, relwidth=0.1, relheight=0.1, anchor='n')
        Button(window,text = "BACK",command = Book5, bg='#999999').place(relx=0.6, rely=0.85, relwidth=0.1, relheight=0.1, anchor='n')

    Label(window,text = "No 5", bg= '#fff000').place(relx=0.5, rely=0.3, relwidth=0.2, relheight=0.1, anchor='n')
    Label(window,text = "category ->", bg= '#3399ff').place(relx=0.45, rely=0.42, relwidth=0.2, relheight=0.1, anchor='n')
    Label(window,text = "cost ->", bg= '#66ccff').place(relx=0.45, rely=0.52, relwidth=0.2, relheight=0.1, anchor='n')
    Label(window,text = "availability ->", bg= '#99ccff').place(relx=0.45, rely=0.62, relwidth=0.2, relheight=0.1, anchor='n')

    conn = sqlite3.connect(r"D:\\Anurakbodin_python\\guitest.db")
    c = conn.cursor()
    c.execute('select category FROM room WHERE No = 5')
    result = c.fetchall()
    for x in result:
        Label(window,text = x, bg='#ff00ff').place(relx=0.6, rely=0.42, relwidth=0.1, relheight=0.1, anchor='n')
    c.execute('select cost FROM room WHERE No = 5')
    result = c.fetchall()
    for x in result:
        Label(window,text = x, bg='#ff66ff').place(relx=0.6, rely=0.52, relwidth=0.1, relheight=0.1, anchor='n')
    c.execute('select availability FROM room WHERE No = 5')
    result = c.fetchall()
    for x in result:
        Label(window,text = x, bg='#ff99ff').place(relx=0.6, rely=0.62, relwidth=0.1, relheight=0.1, anchor='n')
    Button(window,text = "Booking",command = booking5, bg='#999999').place(relx=0.4, rely=0.8, relwidth=0.1, relheight=0.1, anchor='n')
    Button(window,text = "BACK",command = back_book, bg='#999999').place(relx=0.6, rely=0.8, relwidth=0.1, relheight=0.1, anchor='n')
########################
def Book6():
    win_screen = tk.Frame(window, bg= '#cccc99', bd=5)
    win_screen.place(relx=0.5, rely=0.252, relwidth=0.6, relheight=0.74, anchor='n')
    def booking6():
        win_screen = tk.Frame(window, bg= '#cccc99', bd=5)
        win_screen.place(relx=0.5, rely=0.252, relwidth=0.6, relheight=0.74, anchor='n')
        frame = tk.Frame(window, bg='#990000')
        frame.place(relx = 0.5, rely=0.28, relwidth=0.55, relheight=0.7, anchor='n')
        frame = tk.Frame(window, bg='#99ffff')
        frame.place(relx = 0.5, rely=0.3, relwidth=0.53, relheight=0.66, anchor='n')

        def comfirm6():
            firstname = str(fn.get())
            if len(firstname) > 0 :
                lastname =str(ln.get())
                if len(lastname) > 0 :
                    telephone = str(tel.get())
                    if len(telephone) == 10:
                        firstday = int(fd.get())
                        numday = int(nd.get())
                        lastday = firstday + numday 
                        if lastday <= 31:
                            win_screen = tk.Frame(window, bg= '#f0f0f0', bd=5)
                            win_screen.place(relx=0.5, rely=0.28, relwidth=0.6, relheight=0.8, anchor='n')
                            frame = tk.Frame(window, bg='#99ffff')
                            frame.place(relx = 0.5, rely=0.3, relwidth=0.53, relheight=0.66, anchor='n')
                            total = 1000*numday
                            Label(window, text=("Total=",total),bg='#ff66ff').place(relx=0.5, rely=0.4, relwidth=0.2, relheight=0.1, anchor='n')
                            Label(window, text=("Confirm Booking"),bg='#ff66ff').place(relx=0.5, rely=0.5, relwidth=0.2, relheight=0.08, anchor='n')
                            def comfirm_book():
                                conn = sqlite3.connect(r"D:\\Anurakbodin_python\\guitest.db")
                                c = conn.cursor()
                                try:
                                    data = ("Busy",str(firstname),str(lastname),str(telephone),int(firstday),int(lastday),int(numday),int(total),6)
                                    c.execute('''UPDATE room SET availability =?,first_name =?,last_name=?,tel=?,first_day=?,last_day=?,day=?,total=? WHERE No = ?''',data)
                                    conn.commit()
                                    conn.close()
                                except sqlite3.Error as e:
                                    print('Failed to insert : ',e)
                                finally :
                                    if conn :
                                        conn.close()
                                messagebox.showinfo("Completed","Booking Successful.")
                                back_book()
                            Button(window,text = "ENTER",command = comfirm_book, bg='#999999').place(relx=0.4, rely=0.7, relwidth=0.1, relheight=0.1, anchor='n')
                            Button(window,text = "CANCEL",command = booking6, bg='#999999').place(relx=0.6, rely=0.7, relwidth=0.1, relheight=0.1, anchor='n')
                        else:
                            messagebox.showinfo("Incompleted","The reservation period is not later than this month.")
                    else :
                        messagebox.showinfo("Incompleted","Please fill out all phone numbers.")
                else:
                    messagebox.showinfo("Incompleted","Please enter your last name") 
            else :
                messagebox.showinfo("Incompleted","Please enter your first name")

        def number(S): #ฟังก์ชันพิมได้เฉพาะค่าตัวเลข
            if S.isdigit():
                return True
            window.bell()
            return False
        Nn = (window.register(number), '%S')
        
        def letters(S):
            if S.isalpha():
                return True
            window.bell()
            return False
        Ll = (window.register(letters), '%S')

        Label(window, text="First Name : ", bg='#99ffff').place(relx=0.37, rely=0.34, relwidth=0.1, relheight=0.05, anchor='n')
        f = Entry(window, textvariable=fn, validate='key', vcmd=Ll).place(relx=0.58, rely=0.34, relwidth=0.25, relheight=0.05, anchor='n')
        Label(window, text="Last Name : ", bg='#99ffff').place(relx=0.37, rely=0.44, relwidth=0.1, relheight=0.05, anchor='n')
        l = Entry(window, textvariable=ln, validate='key', vcmd=Ll).place(relx=0.58, rely=0.44, relwidth=0.25, relheight=0.05, anchor='n')

        Label(window, text="Tel : ", bg='#99ffff').place(relx=0.37, rely=0.54, relwidth=0.1, relheight=0.05, anchor='n')
        t = Entry(window, textvariable=tel, validate='key', vcmd=Nn).place(relx=0.58, rely=0.54, relwidth=0.25, relheight=0.05, anchor='n')

        Label(window, text="First day : ", bg='#99ffff').place(relx=0.37, rely=0.64, relwidth=0.1, relheight=0.05, anchor='n')
        fd = Spinbox(window, from_= 1, to = 31)
        fd.place(relx=0.58, rely=0.64, relwidth=0.25, relheight=0.05, anchor='n') 

        Label(window, text="Number of days : ", bg='#99ffff').place(relx=0.37, rely=0.74, relwidth=0.1, relheight=0.05, anchor='n')
        nd = Spinbox(window, from_= 1, to = 7)
        nd.place(relx=0.58, rely=0.74, relwidth=0.25, relheight=0.05, anchor='n')

        Button(window,text = "ENTER",command = comfirm6, bg='#999999').place(relx=0.4, rely=0.85, relwidth=0.1, relheight=0.1, anchor='n')
        Button(window,text = "BACK",command = Book6, bg='#999999').place(relx=0.6, rely=0.85, relwidth=0.1, relheight=0.1, anchor='n')

    Label(window,text = "No 6", bg= '#fff000').place(relx=0.5, rely=0.3, relwidth=0.2, relheight=0.1, anchor='n')
    Label(window,text = "category ->", bg= '#3399ff').place(relx=0.45, rely=0.42, relwidth=0.2, relheight=0.1, anchor='n')
    Label(window,text = "cost ->", bg= '#66ccff').place(relx=0.45, rely=0.52, relwidth=0.2, relheight=0.1, anchor='n')
    Label(window,text = "availability ->", bg= '#99ccff').place(relx=0.45, rely=0.62, relwidth=0.2, relheight=0.1, anchor='n')

    conn = sqlite3.connect(r"D:\\Anurakbodin_python\\guitest.db")
    c = conn.cursor()
    c.execute('select category FROM room WHERE No = 6')
    result = c.fetchall()
    for x in result:
        Label(window,text = x, bg='#ff00ff').place(relx=0.6, rely=0.42, relwidth=0.1, relheight=0.1, anchor='n')
    c.execute('select cost FROM room WHERE No = 6')
    result = c.fetchall()
    for x in result:
        Label(window,text = x, bg='#ff66ff').place(relx=0.6, rely=0.52, relwidth=0.1, relheight=0.1, anchor='n')
    c.execute('select availability FROM room WHERE No = 6')
    result = c.fetchall()
    for x in result:
        Label(window,text = x, bg='#ff99ff').place(relx=0.6, rely=0.62, relwidth=0.1, relheight=0.1, anchor='n')
    Button(window,text = "Booking",command = booking6, bg='#999999').place(relx=0.4, rely=0.8, relwidth=0.1, relheight=0.1, anchor='n')
    Button(window,text = "BACK",command = back_book, bg='#999999').place(relx=0.6, rely=0.8, relwidth=0.1, relheight=0.1, anchor='n')
########################
def Book7():
    win_screen = tk.Frame(window, bg= '#cccc99', bd=5)
    win_screen.place(relx=0.5, rely=0.252, relwidth=0.6, relheight=0.74, anchor='n')
    def booking7():
        win_screen = tk.Frame(window, bg= '#cccc99', bd=5)
        win_screen.place(relx=0.5, rely=0.252, relwidth=0.6, relheight=0.74, anchor='n')
        frame = tk.Frame(window, bg='#990000')
        frame.place(relx = 0.5, rely=0.28, relwidth=0.55, relheight=0.7, anchor='n')
        frame = tk.Frame(window, bg='#99ffff')
        frame.place(relx = 0.5, rely=0.3, relwidth=0.53, relheight=0.66, anchor='n')

        def comfirm7():
            firstname = str(fn.get())
            if len(firstname) > 0 :
                lastname =str(ln.get())
                if len(lastname) > 0 :
                    telephone = str(tel.get())
                    if len(telephone) == 10:
                        firstday = int(fd.get())
                        numday = int(nd.get())
                        lastday = firstday + numday 
                        if lastday <= 31:
                            win_screen = tk.Frame(window, bg= '#f0f0f0', bd=5)
                            win_screen.place(relx=0.5, rely=0.28, relwidth=0.6, relheight=0.8, anchor='n')
                            frame = tk.Frame(window, bg='#99ffff')
                            frame.place(relx = 0.5, rely=0.3, relwidth=0.53, relheight=0.66, anchor='n')
                            total = 1000*numday
                            Label(window, text=("Total=",total),bg='#ff66ff').place(relx=0.5, rely=0.4, relwidth=0.2, relheight=0.1, anchor='n')
                            Label(window, text=("Confirm Booking"),bg='#ff66ff').place(relx=0.5, rely=0.5, relwidth=0.2, relheight=0.08, anchor='n')
                            def comfirm_book():
                                conn = sqlite3.connect(r"D:\\Anurakbodin_python\\guitest.db")
                                c = conn.cursor()
                                try:
                                    data = ("Busy",str(firstname),str(lastname),str(telephone),int(firstday),int(lastday),int(numday),int(total),7)
                                    c.execute('''UPDATE room SET availability =?,first_name =?,last_name=?,tel=?,first_day=?,last_day=?,day=?,total=? WHERE No = ?''',data)
                                    conn.commit()
                                    conn.close()
                                except sqlite3.Error as e:
                                    print('Failed to insert : ',e)
                                finally :
                                    if conn :
                                        conn.close()
                                messagebox.showinfo("Completed","Booking Successful.")
                                back_book()
                            Button(window,text = "ENTER",command = comfirm_book, bg='#999999').place(relx=0.4, rely=0.7, relwidth=0.1, relheight=0.1, anchor='n')
                            Button(window,text = "CANCEL",command = booking7, bg='#999999').place(relx=0.6, rely=0.7, relwidth=0.1, relheight=0.1, anchor='n')
                        else:
                            messagebox.showinfo("Incompleted","The reservation period is not later than this month.")
                    else :
                        messagebox.showinfo("Incompleted","Please fill out all phone numbers.")
                else:
                    messagebox.showinfo("Incompleted","Please enter your last name") 
            else :
                messagebox.showinfo("Incompleted","Please enter your first name")

        def number(S): #ฟังก์ชันพิมได้เฉพาะค่าตัวเลข
            if S.isdigit():
                return True
            window.bell()
            return False
        Nn = (window.register(number), '%S')
        
        def letters(S):
            if S.isalpha():
                return True
            window.bell()
            return False
        Ll = (window.register(letters), '%S')

        Label(window, text="First Name : ", bg='#99ffff').place(relx=0.37, rely=0.34, relwidth=0.1, relheight=0.05, anchor='n')
        f = Entry(window, textvariable=fn, validate='key', vcmd=Ll).place(relx=0.58, rely=0.34, relwidth=0.25, relheight=0.05, anchor='n')
        Label(window, text="Last Name : ", bg='#99ffff').place(relx=0.37, rely=0.44, relwidth=0.1, relheight=0.05, anchor='n')
        l = Entry(window, textvariable=ln, validate='key', vcmd=Ll).place(relx=0.58, rely=0.44, relwidth=0.25, relheight=0.05, anchor='n')

        Label(window, text="Tel : ", bg='#99ffff').place(relx=0.37, rely=0.54, relwidth=0.1, relheight=0.05, anchor='n')
        t = Entry(window, textvariable=tel, validate='key', vcmd=Nn).place(relx=0.58, rely=0.54, relwidth=0.25, relheight=0.05, anchor='n')

        Label(window, text="First day : ", bg='#99ffff').place(relx=0.37, rely=0.64, relwidth=0.1, relheight=0.05, anchor='n')
        fd = Spinbox(window, from_= 1, to = 31)
        fd.place(relx=0.58, rely=0.64, relwidth=0.25, relheight=0.05, anchor='n') 

        Label(window, text="Number of days : ", bg='#99ffff').place(relx=0.37, rely=0.74, relwidth=0.1, relheight=0.05, anchor='n')
        nd = Spinbox(window, from_= 1, to = 7)
        nd.place(relx=0.58, rely=0.74, relwidth=0.25, relheight=0.05, anchor='n')

        Button(window,text = "ENTER",command = comfirm7, bg='#999999').place(relx=0.4, rely=0.85, relwidth=0.1, relheight=0.1, anchor='n')
        Button(window,text = "BACK",command = Book7, bg='#999999').place(relx=0.6, rely=0.85, relwidth=0.1, relheight=0.1, anchor='n')

    Label(window,text = "No 7", bg= '#fff000').place(relx=0.5, rely=0.3, relwidth=0.2, relheight=0.1, anchor='n')
    Label(window,text = "category ->", bg= '#3399ff').place(relx=0.45, rely=0.42, relwidth=0.2, relheight=0.1, anchor='n')
    Label(window,text = "cost ->", bg= '#66ccff').place(relx=0.45, rely=0.52, relwidth=0.2, relheight=0.1, anchor='n')
    Label(window,text = "availability ->", bg= '#99ccff').place(relx=0.45, rely=0.62, relwidth=0.2, relheight=0.1, anchor='n')

    conn = sqlite3.connect(r"D:\\Anurakbodin_python\\guitest.db")
    c = conn.cursor()
    c.execute('select category FROM room WHERE No = 7')
    result = c.fetchall()
    for x in result:
        Label(window,text = x, bg='#ff00ff').place(relx=0.6, rely=0.42, relwidth=0.1, relheight=0.1, anchor='n')
    c.execute('select cost FROM room WHERE No = 7')
    result = c.fetchall()
    for x in result:
        Label(window,text = x, bg='#ff66ff').place(relx=0.6, rely=0.52, relwidth=0.1, relheight=0.1, anchor='n')
    c.execute('select availability FROM room WHERE No = 7')
    result = c.fetchall()
    for x in result:
        Label(window,text = x, bg='#ff99ff').place(relx=0.6, rely=0.62, relwidth=0.1, relheight=0.1, anchor='n')
    Button(window,text = "Booking",command = booking7, bg='#999999').place(relx=0.4, rely=0.8, relwidth=0.1, relheight=0.1, anchor='n')
    Button(window,text = "BACK",command = back_book, bg='#999999').place(relx=0.6, rely=0.8, relwidth=0.1, relheight=0.1, anchor='n')
########################
def Book8():
    win_screen = tk.Frame(window, bg= '#cccc99', bd=5)
    win_screen.place(relx=0.5, rely=0.252, relwidth=0.6, relheight=0.74, anchor='n')
    def booking8():
        win_screen = tk.Frame(window, bg= '#cccc99', bd=5)
        win_screen.place(relx=0.5, rely=0.252, relwidth=0.6, relheight=0.74, anchor='n')
        frame = tk.Frame(window, bg='#990000')
        frame.place(relx = 0.5, rely=0.28, relwidth=0.55, relheight=0.7, anchor='n')
        frame = tk.Frame(window, bg='#99ffff')
        frame.place(relx = 0.5, rely=0.3, relwidth=0.53, relheight=0.66, anchor='n')

        def comfirm8():
            firstname = str(fn.get())
            if len(firstname) > 0 :
                lastname =str(ln.get())
                if len(lastname) > 0 :
                    telephone = str(tel.get())
                    if len(telephone) == 10:
                        firstday = int(fd.get())
                        numday = int(nd.get())
                        lastday = firstday + numday 
                        if lastday <= 31:
                            win_screen = tk.Frame(window, bg= '#f0f0f0', bd=5)
                            win_screen.place(relx=0.5, rely=0.28, relwidth=0.6, relheight=0.8, anchor='n')
                            frame = tk.Frame(window, bg='#99ffff')
                            frame.place(relx = 0.5, rely=0.3, relwidth=0.53, relheight=0.66, anchor='n')
                            total = 1000*numday
                            Label(window, text=("Total=",total),bg='#ff66ff').place(relx=0.5, rely=0.4, relwidth=0.2, relheight=0.1, anchor='n')
                            Label(window, text=("Confirm Booking"),bg='#ff66ff').place(relx=0.5, rely=0.5, relwidth=0.2, relheight=0.08, anchor='n')
                            def comfirm_book():
                                conn = sqlite3.connect(r"D:\\Anurakbodin_python\\guitest.db")
                                c = conn.cursor()
                                try:
                                    data = ("Busy",str(firstname),str(lastname),str(telephone),int(firstday),int(lastday),int(numday),int(total),8)
                                    c.execute('''UPDATE room SET availability =?,first_name =?,last_name=?,tel=?,first_day=?,last_day=?,day=?,total=? WHERE No = ?''',data)
                                    conn.commit()
                                    conn.close()
                                except sqlite3.Error as e:
                                    print('Failed to insert : ',e)
                                finally :
                                    if conn :
                                        conn.close()
                                messagebox.showinfo("Completed","Booking Successful.")
                                back_book()
                            Button(window,text = "ENTER",command = comfirm_book, bg='#999999').place(relx=0.4, rely=0.7, relwidth=0.1, relheight=0.1, anchor='n')
                            Button(window,text = "CANCEL",command = booking8, bg='#999999').place(relx=0.6, rely=0.7, relwidth=0.1, relheight=0.1, anchor='n')
                        else:
                            messagebox.showinfo("Incompleted","The reservation period is not later than this month.")
                    else :
                        messagebox.showinfo("Incompleted","Please fill out all phone numbers.")
                else:
                    messagebox.showinfo("Incompleted","Please enter your last name") 
            else :
                messagebox.showinfo("Incompleted","Please enter your first name")

        def number(S): #ฟังก์ชันพิมได้เฉพาะค่าตัวเลข
            if S.isdigit():
                return True
            window.bell()
            return False
        Nn = (window.register(number), '%S')
        
        def letters(S):
            if S.isalpha():
                return True
            window.bell()
            return False
        Ll = (window.register(letters), '%S')

        Label(window, text="First Name : ", bg='#99ffff').place(relx=0.37, rely=0.34, relwidth=0.1, relheight=0.05, anchor='n')
        f = Entry(window, textvariable=fn, validate='key', vcmd=Ll).place(relx=0.58, rely=0.34, relwidth=0.25, relheight=0.05, anchor='n')
        Label(window, text="Last Name : ", bg='#99ffff').place(relx=0.37, rely=0.44, relwidth=0.1, relheight=0.05, anchor='n')
        l = Entry(window, textvariable=ln, validate='key', vcmd=Ll).place(relx=0.58, rely=0.44, relwidth=0.25, relheight=0.05, anchor='n')

        Label(window, text="Tel : ", bg='#99ffff').place(relx=0.37, rely=0.54, relwidth=0.1, relheight=0.05, anchor='n')
        t = Entry(window, textvariable=tel, validate='key', vcmd=Nn).place(relx=0.58, rely=0.54, relwidth=0.25, relheight=0.05, anchor='n')

        Label(window, text="First day : ", bg='#99ffff').place(relx=0.37, rely=0.64, relwidth=0.1, relheight=0.05, anchor='n')
        fd = Spinbox(window, from_= 1, to = 31)
        fd.place(relx=0.58, rely=0.64, relwidth=0.25, relheight=0.05, anchor='n') 

        Label(window, text="Number of days : ", bg='#99ffff').place(relx=0.37, rely=0.74, relwidth=0.1, relheight=0.05, anchor='n')
        nd = Spinbox(window, from_= 1, to = 7)
        nd.place(relx=0.58, rely=0.74, relwidth=0.25, relheight=0.05, anchor='n')

        Button(window,text = "ENTER",command = comfirm8, bg='#999999').place(relx=0.4, rely=0.85, relwidth=0.1, relheight=0.1, anchor='n')
        Button(window,text = "BACK",command = Book8, bg='#999999').place(relx=0.6, rely=0.85, relwidth=0.1, relheight=0.1, anchor='n')

    Label(window,text = "No 8", bg= '#fff000').place(relx=0.5, rely=0.3, relwidth=0.2, relheight=0.1, anchor='n')
    Label(window,text = "category ->", bg= '#3399ff').place(relx=0.45, rely=0.42, relwidth=0.2, relheight=0.1, anchor='n')
    Label(window,text = "cost ->", bg= '#66ccff').place(relx=0.45, rely=0.52, relwidth=0.2, relheight=0.1, anchor='n')
    Label(window,text = "availability ->", bg= '#99ccff').place(relx=0.45, rely=0.62, relwidth=0.2, relheight=0.1, anchor='n')

    conn = sqlite3.connect(r"D:\\Anurakbodin_python\\guitest.db")
    c = conn.cursor()
    c.execute('select category FROM room WHERE No = 8')
    result = c.fetchall()
    for x in result:
        Label(window,text = x, bg='#ff00ff').place(relx=0.6, rely=0.42, relwidth=0.1, relheight=0.1, anchor='n')
    c.execute('select cost FROM room WHERE No = 8')
    result = c.fetchall()
    for x in result:
        Label(window,text = x, bg='#ff66ff').place(relx=0.6, rely=0.52, relwidth=0.1, relheight=0.1, anchor='n')
    c.execute('select availability FROM room WHERE No = 8')
    result = c.fetchall()
    for x in result:
        Label(window,text = x, bg='#ff99ff').place(relx=0.6, rely=0.62, relwidth=0.1, relheight=0.1, anchor='n')
    Button(window,text = "Booking",command = booking8, bg='#999999').place(relx=0.4, rely=0.8, relwidth=0.1, relheight=0.1, anchor='n')
    Button(window,text = "BACK",command = back_book, bg='#999999').place(relx=0.6, rely=0.8, relwidth=0.1, relheight=0.1, anchor='n')
########################
def Book9():
    win_screen = tk.Frame(window, bg= '#cccc99', bd=5)
    win_screen.place(relx=0.5, rely=0.252, relwidth=0.6, relheight=0.74, anchor='n')
    def booking9():
        win_screen = tk.Frame(window, bg= '#cccc99', bd=5)
        win_screen.place(relx=0.5, rely=0.252, relwidth=0.6, relheight=0.74, anchor='n')
        frame = tk.Frame(window, bg='#990000')
        frame.place(relx = 0.5, rely=0.28, relwidth=0.55, relheight=0.7, anchor='n')
        frame = tk.Frame(window, bg='#99ffff')
        frame.place(relx = 0.5, rely=0.3, relwidth=0.53, relheight=0.66, anchor='n')

        def comfirm9():
            firstname = str(fn.get())
            if len(firstname) > 0 :
                lastname =str(ln.get())
                if len(lastname) > 0 :
                    telephone = str(tel.get())
                    if len(telephone) == 10:
                        firstday = int(fd.get())
                        numday = int(nd.get())
                        lastday = firstday + numday 
                        if lastday <= 31:
                            win_screen = tk.Frame(window, bg= '#f0f0f0', bd=5)
                            win_screen.place(relx=0.5, rely=0.28, relwidth=0.6, relheight=0.8, anchor='n')
                            frame = tk.Frame(window, bg='#99ffff')
                            frame.place(relx = 0.5, rely=0.3, relwidth=0.53, relheight=0.66, anchor='n')
                            total = 1000*numday
                            Label(window, text=("Total=",total),bg='#ff66ff').place(relx=0.5, rely=0.4, relwidth=0.2, relheight=0.1, anchor='n')
                            Label(window, text=("Confirm Booking"),bg='#ff66ff').place(relx=0.5, rely=0.5, relwidth=0.2, relheight=0.08, anchor='n')
                            def comfirm_book():
                                conn = sqlite3.connect(r"D:\\Anurakbodin_python\\guitest.db")
                                c = conn.cursor()
                                try:
                                    data = ("Busy",str(firstname),str(lastname),str(telephone),int(firstday),int(lastday),int(numday),int(total),9)
                                    c.execute('''UPDATE room SET availability =?,first_name =?,last_name=?,tel=?,first_day=?,last_day=?,day=?,total=? WHERE No = ?''',data)
                                    conn.commit()
                                    conn.close()
                                except sqlite3.Error as e:
                                    print('Failed to insert : ',e)
                                finally :
                                    if conn :
                                        conn.close()
                                messagebox.showinfo("Completed","Booking Successful.")
                                back_book()
                            Button(window,text = "ENTER",command = comfirm_book, bg='#999999').place(relx=0.4, rely=0.7, relwidth=0.1, relheight=0.1, anchor='n')
                            Button(window,text = "CANCEL",command = booking9, bg='#999999').place(relx=0.6, rely=0.7, relwidth=0.1, relheight=0.1, anchor='n')
                        else:
                            messagebox.showinfo("Incompleted","The reservation period is not later than this month.")
                    else :
                        messagebox.showinfo("Incompleted","Please fill out all phone numbers.")
                else:
                    messagebox.showinfo("Incompleted","Please enter your last name") 
            else :
                messagebox.showinfo("Incompleted","Please enter your first name")

        def number(S): #ฟังก์ชันพิมได้เฉพาะค่าตัวเลข
            if S.isdigit():
                return True
            window.bell()
            return False
        Nn = (window.register(number), '%S')
        
        def letters(S):
            if S.isalpha():
                return True
            window.bell()
            return False
        Ll = (window.register(letters), '%S')

        Label(window, text="First Name : ", bg='#99ffff').place(relx=0.37, rely=0.34, relwidth=0.1, relheight=0.05, anchor='n')
        f = Entry(window, textvariable=fn, validate='key', vcmd=Ll).place(relx=0.58, rely=0.34, relwidth=0.25, relheight=0.05, anchor='n')
        Label(window, text="Last Name : ", bg='#99ffff').place(relx=0.37, rely=0.44, relwidth=0.1, relheight=0.05, anchor='n')
        l = Entry(window, textvariable=ln, validate='key', vcmd=Ll).place(relx=0.58, rely=0.44, relwidth=0.25, relheight=0.05, anchor='n')

        Label(window, text="Tel : ", bg='#99ffff').place(relx=0.37, rely=0.54, relwidth=0.1, relheight=0.05, anchor='n')
        t = Entry(window, textvariable=tel, validate='key', vcmd=Nn).place(relx=0.58, rely=0.54, relwidth=0.25, relheight=0.05, anchor='n')

        Label(window, text="First day : ", bg='#99ffff').place(relx=0.37, rely=0.64, relwidth=0.1, relheight=0.05, anchor='n')
        fd = Spinbox(window, from_= 1, to = 31)
        fd.place(relx=0.58, rely=0.64, relwidth=0.25, relheight=0.05, anchor='n') 

        Label(window, text="Number of days : ", bg='#99ffff').place(relx=0.37, rely=0.74, relwidth=0.1, relheight=0.05, anchor='n')
        nd = Spinbox(window, from_= 1, to = 7)
        nd.place(relx=0.58, rely=0.74, relwidth=0.25, relheight=0.05, anchor='n')

        Button(window,text = "ENTER",command = comfirm9, bg='#999999').place(relx=0.4, rely=0.85, relwidth=0.1, relheight=0.1, anchor='n')
        Button(window,text = "BACK",command = Book9, bg='#999999').place(relx=0.6, rely=0.85, relwidth=0.1, relheight=0.1, anchor='n')

    Label(window,text = "No 9", bg= '#fff000').place(relx=0.5, rely=0.3, relwidth=0.2, relheight=0.1, anchor='n')
    Label(window,text = "category ->", bg= '#3399ff').place(relx=0.45, rely=0.42, relwidth=0.2, relheight=0.1, anchor='n')
    Label(window,text = "cost ->", bg= '#66ccff').place(relx=0.45, rely=0.52, relwidth=0.2, relheight=0.1, anchor='n')
    Label(window,text = "availability ->", bg= '#99ccff').place(relx=0.45, rely=0.62, relwidth=0.2, relheight=0.1, anchor='n')

    conn = sqlite3.connect(r"D:\\Anurakbodin_python\\guitest.db")
    c = conn.cursor()
    c.execute('select category FROM room WHERE No = 9')
    result = c.fetchall()
    for x in result:
        Label(window,text = x, bg='#ff00ff').place(relx=0.6, rely=0.42, relwidth=0.1, relheight=0.1, anchor='n')
    c.execute('select cost FROM room WHERE No = 9')
    result = c.fetchall()
    for x in result:
        Label(window,text = x, bg='#ff66ff').place(relx=0.6, rely=0.52, relwidth=0.1, relheight=0.1, anchor='n')
    c.execute('select availability FROM room WHERE No = 9')
    result = c.fetchall()
    for x in result:
        Label(window,text = x, bg='#ff99ff').place(relx=0.6, rely=0.62, relwidth=0.1, relheight=0.1, anchor='n')
    Button(window,text = "Booking",command = booking9, bg='#999999').place(relx=0.4, rely=0.8, relwidth=0.1, relheight=0.1, anchor='n')
    Button(window,text = "BACK",command = back_book, bg='#999999').place(relx=0.6, rely=0.8, relwidth=0.1, relheight=0.1, anchor='n')
########################
def Book10():
    win_screen = tk.Frame(window, bg= '#cccc99', bd=5)
    win_screen.place(relx=0.5, rely=0.252, relwidth=0.6, relheight=0.74, anchor='n')
    def booking10():
        win_screen = tk.Frame(window, bg= '#cccc99', bd=5)
        win_screen.place(relx=0.5, rely=0.252, relwidth=0.6, relheight=0.74, anchor='n')
        frame = tk.Frame(window, bg='#990000')
        frame.place(relx = 0.5, rely=0.28, relwidth=0.55, relheight=0.7, anchor='n')
        frame = tk.Frame(window, bg='#99ffff')
        frame.place(relx = 0.5, rely=0.3, relwidth=0.53, relheight=0.66, anchor='n')

        def comfirm10():
            firstname = str(fn.get())
            if len(firstname) > 0 :
                lastname =str(ln.get())
                if len(lastname) > 0 :
                    telephone = str(tel.get())
                    if len(telephone) == 10:
                        firstday = int(fd.get())
                        numday = int(nd.get())
                        lastday = firstday + numday 
                        if lastday <= 31:
                            win_screen = tk.Frame(window, bg= '#f0f0f0', bd=5)
                            win_screen.place(relx=0.5, rely=0.28, relwidth=0.6, relheight=0.8, anchor='n')
                            frame = tk.Frame(window, bg='#99ffff')
                            frame.place(relx = 0.5, rely=0.3, relwidth=0.53, relheight=0.66, anchor='n')
                            total = 1000*numday
                            Label(window, text=("Total=",total),bg='#ff66ff').place(relx=0.5, rely=0.4, relwidth=0.2, relheight=0.1, anchor='n')
                            Label(window, text=("Confirm Booking"),bg='#ff66ff').place(relx=0.5, rely=0.5, relwidth=0.2, relheight=0.08, anchor='n')
                            def comfirm_book():
                                conn = sqlite3.connect(r"D:\\Anurakbodin_python\\guitest.db")
                                c = conn.cursor()
                                try:
                                    data = ("Busy",str(firstname),str(lastname),str(telephone),int(firstday),int(lastday),int(numday),int(total),10)
                                    c.execute('''UPDATE room SET availability =?,first_name =?,last_name=?,tel=?,first_day=?,last_day=?,day=?,total=? WHERE No = ?''',data)
                                    conn.commit()
                                    conn.close()
                                except sqlite3.Error as e:
                                    print('Failed to insert : ',e)
                                finally :
                                    if conn :
                                        conn.close()
                                messagebox.showinfo("Completed","Booking Successful.")
                                back_book()
                            Button(window,text = "ENTER",command = comfirm_book, bg='#999999').place(relx=0.4, rely=0.7, relwidth=0.1, relheight=0.1, anchor='n')
                            Button(window,text = "CANCEL",command = booking10, bg='#999999').place(relx=0.6, rely=0.7, relwidth=0.1, relheight=0.1, anchor='n')
                        else:
                            messagebox.showinfo("Incompleted","The reservation period is not later than this month.")
                    else :
                        messagebox.showinfo("Incompleted","Please fill out all phone numbers.")
                else:
                    messagebox.showinfo("Incompleted","Please enter your last name") 
            else :
                messagebox.showinfo("Incompleted","Please enter your first name")

        def number(S): #ฟังก์ชันพิมได้เฉพาะค่าตัวเลข
            if S.isdigit():
                return True
            window.bell()
            return False
        Nn = (window.register(number), '%S')
        
        def letters(S):
            if S.isalpha():
                return True
            window.bell()
            return False
        Ll = (window.register(letters), '%S')

        Label(window, text="First Name : ", bg='#99ffff').place(relx=0.37, rely=0.34, relwidth=0.1, relheight=0.05, anchor='n')
        f = Entry(window, textvariable=fn, validate='key', vcmd=Ll).place(relx=0.58, rely=0.34, relwidth=0.25, relheight=0.05, anchor='n')
        Label(window, text="Last Name : ", bg='#99ffff').place(relx=0.37, rely=0.44, relwidth=0.1, relheight=0.05, anchor='n')
        l = Entry(window, textvariable=ln, validate='key', vcmd=Ll).place(relx=0.58, rely=0.44, relwidth=0.25, relheight=0.05, anchor='n')

        Label(window, text="Tel : ", bg='#99ffff').place(relx=0.37, rely=0.54, relwidth=0.1, relheight=0.05, anchor='n')
        t = Entry(window, textvariable=tel, validate='key', vcmd=Nn).place(relx=0.58, rely=0.54, relwidth=0.25, relheight=0.05, anchor='n')

        Label(window, text="First day : ", bg='#99ffff').place(relx=0.37, rely=0.64, relwidth=0.1, relheight=0.05, anchor='n')
        fd = Spinbox(window, from_= 1, to = 31)
        fd.place(relx=0.58, rely=0.64, relwidth=0.25, relheight=0.05, anchor='n') 

        Label(window, text="Number of days : ", bg='#99ffff').place(relx=0.37, rely=0.74, relwidth=0.1, relheight=0.05, anchor='n')
        nd = Spinbox(window, from_= 1, to = 7)
        nd.place(relx=0.58, rely=0.74, relwidth=0.25, relheight=0.05, anchor='n')

        Button(window,text = "ENTER",command = comfirm10, bg='#999999').place(relx=0.4, rely=0.85, relwidth=0.1, relheight=0.1, anchor='n')
        Button(window,text = "BACK",command = Book10, bg='#999999').place(relx=0.6, rely=0.85, relwidth=0.1, relheight=0.1, anchor='n')

    Label(window,text = "No 10", bg= '#fff000').place(relx=0.5, rely=0.3, relwidth=0.2, relheight=0.1, anchor='n')
    Label(window,text = "category ->", bg= '#3399ff').place(relx=0.45, rely=0.42, relwidth=0.2, relheight=0.1, anchor='n')
    Label(window,text = "cost ->", bg= '#66ccff').place(relx=0.45, rely=0.52, relwidth=0.2, relheight=0.1, anchor='n')
    Label(window,text = "availability ->", bg= '#99ccff').place(relx=0.45, rely=0.62, relwidth=0.2, relheight=0.1, anchor='n')

    conn = sqlite3.connect(r"D:\\Anurakbodin_python\\guitest.db")
    c = conn.cursor()
    c.execute('select category FROM room WHERE No = 10')
    result = c.fetchall()
    for x in result:
        Label(window,text = x, bg='#ff00ff').place(relx=0.6, rely=0.42, relwidth=0.1, relheight=0.1, anchor='n')
    c.execute('select cost FROM room WHERE No = 10')
    result = c.fetchall()
    for x in result:
        Label(window,text = x, bg='#ff66ff').place(relx=0.6, rely=0.52, relwidth=0.1, relheight=0.1, anchor='n')
    c.execute('select availability FROM room WHERE No = 10')
    result = c.fetchall()
    for x in result:
        Label(window,text = x, bg='#ff99ff').place(relx=0.6, rely=0.62, relwidth=0.1, relheight=0.1, anchor='n')
    Button(window,text = "Booking",command = booking10, bg='#999999').place(relx=0.4, rely=0.8, relwidth=0.1, relheight=0.1, anchor='n')
    Button(window,text = "BACK",command = back_book, bg='#999999').place(relx=0.6, rely=0.8, relwidth=0.1, relheight=0.1, anchor='n')
########################


def show():
    Nor = 1
    scy = 0.3
    scx = 0.28
    win_screen = tk.Frame(window, bg= '#cccc99', bd=5)
    win_screen.place(relx=0.5, rely=0.252, relwidth=0.6, relheight=0.74, anchor='n')
    frame = tk.Frame(window, bg='#3399ff')
    frame.place(relx = 0.5, rely=0.29, relwidth=0.55, relheight=0.7, anchor='n')
    free = PhotoImage(file=r"D:\Anurakbodin_python\ico\free.png")
    busy = PhotoImage(file=r"D:\Anurakbodin_python\ico\busy.png")
    while Nor <= 10 :
        conn = sqlite3.connect(r"D:\\Anurakbodin_python\\guitest.db")
        c = conn.cursor()
        data = Nor,
        c.execute('select availability FROM room WHERE No = ?',data)
        result = c.fetchall()
        for x in result:
            ava = str(x).strip("(',)")
        if ava == "Free":
            if Nor <= 5:
                Label(window,text = Nor, bg='#00ff00').place(relx=scx, rely=scy, relwidth=0.1, relheight=0.2, anchor='n')
                scx = scx + 0.11
            elif Nor == 6 :
                scx = 0.28
                scy = 0.6
                Label(window,text = Nor, bg='#00ff00').place(relx=scx, rely=scy, relwidth=0.1, relheight=0.2, anchor='n')
            else :
                scx = scx + 0.11
                Label(window,text = Nor, bg='#00ff00').place(relx=scx, rely=scy, relwidth=0.1, relheight=0.2, anchor='n')
        else :
            if Nor <= 5:
               Label(window,text = Nor, bg='#cc3333').place(relx=scx, rely=scy, relwidth=0.1, relheight=0.2, anchor='n')
               scx = scx + 0.11
            elif Nor == 6 :
                scx = 0.28
                scy = 0.51
                Label(window,text = Nor, bg='#cc3333').place(relx=scx, rely=scy, relwidth=0.1, relheight=0.2, anchor='n')
            else :
                scx = scx + 0.11
                Label(window,text = Nor, bg='#cc3333').place(relx=scx, rely=scy, relwidth=0.1, relheight=0.2, anchor='n')
        Nor = Nor + 1
    Label(window,text = "Green is Free room", bg='#00ff00').place(relx=0.38, rely=0.75, relwidth=0.3, relheight=0.1, anchor='n')
    Label(window,text = "Red is Busy room", bg='#cc3333').place(relx=0.63, rely=0.75, relwidth=0.28, relheight=0.1, anchor='n')
    Button(window, text='BACK',command = login_com, bg='#00ccff', fg='#000000').place(relx=0.5, rely=0.88, relwidth=0.3, relheight=0.1, anchor='n')
########################


def cancelbook():
    win_screen = tk.Frame(window, bg= '#cccc99', bd=5)
    win_screen.place(relx=0.5, rely=0.252, relwidth=0.6, relheight=0.74, anchor='n')
    frame = tk.Frame(window, bg='#3366ff')
    frame.place(relx = 0.5, rely=0.29, relwidth=0.55, relheight=0.6, anchor='n')
    frame = tk.Frame(window, bg='#00ccff')
    frame.place(relx = 0.5, rely=0.295, relwidth=0.545, relheight=0.42, anchor='n')
    conn = sqlite3.connect(r"D:\\Anurakbodin_python\\guitest.db")
    c = conn.cursor()
    data = 1,
    c.execute('select availability FROM room WHERE No = ?',data)
    result = c.fetchall()
    for x in result:
        ava = str(x).strip("(',)")
    if ava == "Free" :
        r1 = Label(window,text = 1, bg='#00ff00').place(relx=0.28, rely=0.3, relwidth=0.1, relheight=0.2, anchor='n')
    else:
        r1 = Button(window,text = 1,command = cancelBook1, bg='#cc3333').place(relx=0.28, rely=0.3, relwidth=0.1, relheight=0.2, anchor='n')

    data = 2,
    c.execute('select availability FROM room WHERE No = ?',data)
    result = c.fetchall()
    for x in result:
        ava = str(x).strip("(',)")
    if ava == "Free" :
        r2 = Label(window,text = 2, bg='#00ff00').place(relx=0.39, rely=0.3, relwidth=0.1, relheight=0.2, anchor='n')
    else:
        r2 = Button(window,text = 2,command = cancelBook2, bg='#cc3333').place(relx=0.39, rely=0.3, relwidth=0.1, relheight=0.2, anchor='n')

    data = 3,
    c.execute('select availability FROM room WHERE No = ?',data)
    result = c.fetchall()
    for x in result:
        ava = str(x).strip("(',)")
    if ava == "Free" :
        r3 = Label(window,text = 3, bg='#00ff00').place(relx=0.5, rely=0.3, relwidth=0.1, relheight=0.2, anchor='n')
    else:
        r3 = Button(window,text = 3,command = cancelBook3, bg='#cc3333').place(relx=0.5, rely=0.3, relwidth=0.1, relheight=0.2, anchor='n')

    data = 4,
    c.execute('select availability FROM room WHERE No = ?',data)
    result = c.fetchall()
    for x in result:
        ava = str(x).strip("(',)")
    if ava == "Free" :
        r4 = Label(window,text = 4, bg='#00ff00').place(relx=0.61, rely=0.3, relwidth=0.1, relheight=0.2, anchor='n')
    else:
        r4 = Button(window,text = 4,command = cancelBook4, bg='#cc3333').place(relx=0.61, rely=0.3, relwidth=0.1, relheight=0.2, anchor='n')

    data = 5,
    c.execute('select availability FROM room WHERE No = ?',data)
    result = c.fetchall()
    for x in result:
        ava = str(x).strip("(',)")
    if ava == "Free" :
        r5 = Label(window,text = 5, bg='#00ff00').place(relx=0.72, rely=0.3, relwidth=0.1, relheight=0.2, anchor='n')
    else:
        r5 = Button(window,text = 5,command = cancelBook5, bg='#cc3333').place(relx=0.72, rely=0.3, relwidth=0.1, relheight=0.2, anchor='n')

    data = 6,
    c.execute('select availability FROM room WHERE No = ?',data)
    result = c.fetchall()
    for x in result:
        ava = str(x).strip("(',)")
    if ava == "Free" :
        r6 = Label(window,text = 6, bg='#00ff00').place(relx=0.28, rely=0.51, relwidth=0.1, relheight=0.2, anchor='n')
    else:
        r6 = Button(window,text = 6,command = cancelBook6, bg='#cc3333').place(relx=0.28, rely=0.51, relwidth=0.1, relheight=0.2, anchor='n')

    data = 7,
    c.execute('select availability FROM room WHERE No = ?',data)
    result = c.fetchall()
    for x in result:
        ava = str(x).strip("(',)")
    if ava == "Free" :
        r7 = Label(window,text = 7, bg='#00ff00').place(relx=0.39, rely=0.51, relwidth=0.1, relheight=0.2, anchor='n')
    else:
        r7 = Button(window,text = 7,command = cancelBook7, bg='#cc3333').place(relx=0.39, rely=0.51, relwidth=0.1, relheight=0.2, anchor='n')

        data = 8,
    c.execute('select availability FROM room WHERE No = ?',data)
    result = c.fetchall()
    for x in result:
        ava = str(x).strip("(',)")
    if ava == "Free" :
        r8 = Label(window,text = 8, bg='#00ff00').place(relx=0.5, rely=0.51, relwidth=0.1, relheight=0.2, anchor='n')
    else:
        r8 = Button(window,text = 8,command = cancelBook8, bg='#cc3333').place(relx=0.5, rely=0.51, relwidth=0.1, relheight=0.2, anchor='n')
    
    data = 9,
    c.execute('select availability FROM room WHERE No = ?',data)
    result = c.fetchall()
    for x in result:
        ava = str(x).strip("(',)")
    if ava == "Free" :
        r9 = Label(window,text = 9, bg='#00ff00').place(relx=0.61, rely=0.51, relwidth=0.1, relheight=0.2, anchor='n')
    else:
        r9 = Button(window,text = 9,command = cancelBook9, bg='#cc3333').place(relx=0.61, rely=0.51, relwidth=0.1, relheight=0.2, anchor='n')
    
    data = 10,
    c.execute('select availability FROM room WHERE No = ?',data)
    result = c.fetchall()
    for x in result:
        ava = str(x).strip("(',)")
    if ava == "Free" :
        r10 = Label(window,text = 10, bg='#00ff00').place(relx=0.72, rely=0.51, relwidth=0.1, relheight=0.2, anchor='n')
    else:
        r10 = Button(window,text = 10,command = cancelBook10, bg='#cc3333').place(relx=0.72, rely=0.51, relwidth=0.1, relheight=0.2, anchor='n')
    Label(window,text = "Menu Cancel BOOKING", bg='#ff9999').place(relx=0.34, rely=0.75, relwidth=0.17, relheight=0.1, anchor='n')
    Label(window,text = "Select Red Room", bg='#cc3333').place(relx=0.65, rely=0.75, relwidth=0.13, relheight=0.1, anchor='n')
    Button(window,text = "BACK",command=login_com, bg='#ffcc99').place(relx=0.5, rely=0.75, relwidth=0.1, relheight=0.1, anchor='n')
########################
def back_cancelbook():
    cancelbook()
########################
def cancelBook1():
    win_screen = tk.Frame(window, bg= '#cccc99', bd=5)
    win_screen.place(relx=0.5, rely=0.252, relwidth=0.6, relheight=0.74, anchor='n')
    frame = tk.Frame(window, bg='#ff9966')
    frame.place(relx = 0.5, rely=0.29, relwidth=0.5, relheight=0.7, anchor='n')
    Label(window,text = "No 1", bg= '#fff000').place(relx=0.5, rely=0.3, relwidth=0.2, relheight=0.1, anchor='n')
    Label(window,text = "First Name ->", bg= '#0066ff').place(relx=0.4, rely=0.42, relwidth=0.2, relheight=0.1, anchor='n')
    Label(window,text = "Last Name ->", bg= '#3399ff').place(relx=0.4, rely=0.52, relwidth=0.2, relheight=0.1, anchor='n')
    Label(window,text = "Tel ->", bg= '#66ccff').place(relx=0.4, rely=0.62, relwidth=0.2, relheight=0.1, anchor='n')
    Label(window,text = "Total ->", bg= '#99ccff').place(relx=0.4, rely=0.72, relwidth=0.2, relheight=0.1, anchor='n')
    def cancel_book1() :
        win_screen = tk.Frame(window, bg= '#cccc99', bd=5)
        win_screen.place(relx=0.5, rely=0.252, relwidth=0.6, relheight=0.74, anchor='n')
        frame = tk.Frame(window, bg='#ff9966')
        frame.place(relx = 0.5, rely=0.38, relwidth=0.5, relheight=0.4, anchor='n')
        def comfirm_cancel_book1():
            conn = sqlite3.connect(r"D:\\Anurakbodin_python\\guitest.db")
            c = conn.cursor()
            try:
                data = ("Free","-","-","-",0,0,0,0)
                c.execute('UPDATE room set availability =?,first_name=?,last_name=?,tel=?,first_day=?,last_day=?,day=?,total=? WHERE No =1',data)
                conn.commit()
                conn.close()
            except sqlite3.Error as e:
                print('Failed to insert : ',e)
            finally :
                if conn :
                    conn.close()
            messagebox.showinfo("Completed","Cancel Booking Completed")
            back_cancelbook()
        conn = sqlite3.connect(r"D:\\Anurakbodin_python\\guitest.db")
        c = conn.cursor()
        c.execute('select total FROM room WHERE No = 1')
        result = c.fetchall()
        for x in result:
            total = x[0]
        servicecharge = total*10/100
        Label(window,text = "If you cancel booking, 10 percent of the total rental price will be charged.", bg='#66ccff').place(relx=0.5, rely=0.4, relwidth=0.45, relheight=0.1, anchor='n')
        Label(window,text = ("Total=",servicecharge), bg='#66ccff').place(relx=0.5, rely=0.5, relwidth=0.45, relheight=0.1, anchor='n')
        Button(window,text = "ENTER",command = comfirm_cancel_book1, bg='#999999').place(relx=0.4, rely=0.65, relwidth=0.1, relheight=0.1, anchor='n')
        Button(window,text = "BACK",command = cancelBook1, bg='#999999').place(relx=0.6, rely=0.65, relwidth=0.1, relheight=0.1, anchor='n')
    conn = sqlite3.connect(r"D:\\Anurakbodin_python\\guitest.db")
    c = conn.cursor()
    c.execute('select first_name FROM room WHERE No = 1')
    result = c.fetchall()
    for x in result:
        Label(window,text = x, bg='#ff0099').place(relx=0.6, rely=0.42, relwidth=0.2, relheight=0.1, anchor='n')
    c.execute('select last_name FROM room WHERE No = 1')
    result = c.fetchall()
    for x in result:
        Label(window,text = x, bg='#ff00ff').place(relx=0.6, rely=0.52, relwidth=0.2, relheight=0.1, anchor='n')

    c.execute('select tel FROM room WHERE No = 1')
    result = c.fetchall()
    for x in result:
        Label(window,text = x, bg='#ff66ff').place(relx=0.6, rely=0.62, relwidth=0.2, relheight=0.1, anchor='n')
    c.execute('select total FROM room WHERE No = 1')
    result = c.fetchall()
    for x in result:
        Label(window,text = x, bg='#ff99ff').place(relx=0.6, rely=0.72, relwidth=0.2, relheight=0.1, anchor='n')
    Button(window,text = "Cancel Booking",command = cancel_book1, bg='#999999').place(relx=0.4, rely=0.85, relwidth=0.1, relheight=0.1, anchor='n')
    Button(window,text = "BACK",command = back_cancelbook, bg='#999999').place(relx=0.6, rely=0.85, relwidth=0.1, relheight=0.1, anchor='n')
########################
def cancelBook2():
    win_screen = tk.Frame(window, bg= '#cccc99', bd=5)
    win_screen.place(relx=0.5, rely=0.252, relwidth=0.6, relheight=0.74, anchor='n')
    frame = tk.Frame(window, bg='#ff9966')
    frame.place(relx = 0.5, rely=0.29, relwidth=0.5, relheight=0.7, anchor='n')
    Label(window,text = "No 2", bg= '#fff000').place(relx=0.5, rely=0.3, relwidth=0.2, relheight=0.1, anchor='n')
    Label(window,text = "First Name ->", bg= '#0066ff').place(relx=0.4, rely=0.42, relwidth=0.2, relheight=0.1, anchor='n')
    Label(window,text = "Last Name ->", bg= '#3399ff').place(relx=0.4, rely=0.52, relwidth=0.2, relheight=0.1, anchor='n')
    Label(window,text = "Tel ->", bg= '#66ccff').place(relx=0.4, rely=0.62, relwidth=0.2, relheight=0.1, anchor='n')
    Label(window,text = "Total ->", bg= '#99ccff').place(relx=0.4, rely=0.72, relwidth=0.2, relheight=0.1, anchor='n')
    def cancel_book2() :
        win_screen = tk.Frame(window, bg= '#cccc99', bd=5)
        win_screen.place(relx=0.5, rely=0.252, relwidth=0.6, relheight=0.74, anchor='n')
        frame = tk.Frame(window, bg='#ff9966')
        frame.place(relx = 0.5, rely=0.38, relwidth=0.5, relheight=0.4, anchor='n')
        def comfirm_cancel_book2():
            conn = sqlite3.connect(r"D:\\Anurakbodin_python\\guitest.db")
            c = conn.cursor()
            try:
                data = ("Free","-","-","-",0,0,0,0)
                c.execute('UPDATE room set availability =?,first_name=?,last_name=?,tel=?,first_day=?,last_day=?,day=?,total=? WHERE No =2',data)
                conn.commit()
                conn.close()
            except sqlite3.Error as e:
                print('Failed to insert : ',e)
            finally :
                if conn :
                    conn.close()
            messagebox.showinfo("Completed","Cancel Booking Completed")
            back_cancelbook()
        conn = sqlite3.connect(r"D:\\Anurakbodin_python\\guitest.db")
        c = conn.cursor()
        c.execute('select total FROM room WHERE No = 2')
        result = c.fetchall()
        for x in result:
            total = x[0]
        servicecharge = total*10/100
        Label(window,text = "If you cancel booking, 10 percent of the total rental price will be charged.", bg='#66ccff').place(relx=0.5, rely=0.4, relwidth=0.45, relheight=0.1, anchor='n')
        Label(window,text = ("Total=",servicecharge), bg='#66ccff').place(relx=0.5, rely=0.5, relwidth=0.45, relheight=0.1, anchor='n')
        Button(window,text = "ENTER",command = comfirm_cancel_book2, bg='#999999').place(relx=0.4, rely=0.65, relwidth=0.1, relheight=0.1, anchor='n')
        Button(window,text = "BACK",command = cancelBook2, bg='#999999').place(relx=0.6, rely=0.65, relwidth=0.1, relheight=0.1, anchor='n')
    conn = sqlite3.connect(r"D:\\Anurakbodin_python\\guitest.db")
    c = conn.cursor()
    c.execute('select first_name FROM room WHERE No = 2')
    result = c.fetchall()
    for x in result:
        Label(window,text = x, bg='#ff0099').place(relx=0.6, rely=0.42, relwidth=0.2, relheight=0.1, anchor='n')
    c.execute('select last_name FROM room WHERE No = 2')
    result = c.fetchall()
    for x in result:
        Label(window,text = x, bg='#ff00ff').place(relx=0.6, rely=0.52, relwidth=0.2, relheight=0.1, anchor='n')

    c.execute('select tel FROM room WHERE No = 2')
    result = c.fetchall()
    for x in result:
        Label(window,text = x, bg='#ff66ff').place(relx=0.6, rely=0.62, relwidth=0.2, relheight=0.1, anchor='n')
    c.execute('select total FROM room WHERE No = 2')
    result = c.fetchall()
    for x in result:
        Label(window,text = x, bg='#ff99ff').place(relx=0.6, rely=0.72, relwidth=0.2, relheight=0.1, anchor='n')
    Button(window,text = "Cancel Booking",command = cancel_book2, bg='#999999').place(relx=0.4, rely=0.85, relwidth=0.1, relheight=0.1, anchor='n')
    Button(window,text = "BACK",command = back_cancelbook, bg='#999999').place(relx=0.6, rely=0.85, relwidth=0.1, relheight=0.1, anchor='n')
########################
def cancelBook3():
    win_screen = tk.Frame(window, bg= '#cccc99', bd=5)
    win_screen.place(relx=0.5, rely=0.252, relwidth=0.6, relheight=0.74, anchor='n')
    frame = tk.Frame(window, bg='#ff9966')
    frame.place(relx = 0.5, rely=0.29, relwidth=0.5, relheight=0.7, anchor='n')
    Label(window,text = "No 3", bg= '#fff000').place(relx=0.5, rely=0.3, relwidth=0.2, relheight=0.1, anchor='n')
    Label(window,text = "First Name ->", bg= '#0066ff').place(relx=0.4, rely=0.42, relwidth=0.2, relheight=0.1, anchor='n')
    Label(window,text = "Last Name ->", bg= '#3399ff').place(relx=0.4, rely=0.52, relwidth=0.2, relheight=0.1, anchor='n')
    Label(window,text = "Tel ->", bg= '#66ccff').place(relx=0.4, rely=0.62, relwidth=0.2, relheight=0.1, anchor='n')
    Label(window,text = "Total ->", bg= '#99ccff').place(relx=0.4, rely=0.72, relwidth=0.2, relheight=0.1, anchor='n')
    def cancel_book3() :
        win_screen = tk.Frame(window, bg= '#cccc99', bd=5)
        win_screen.place(relx=0.5, rely=0.252, relwidth=0.6, relheight=0.74, anchor='n')
        frame = tk.Frame(window, bg='#ff9966')
        frame.place(relx = 0.5, rely=0.38, relwidth=0.5, relheight=0.4, anchor='n')
        def comfirm_cancel_book3():
            conn = sqlite3.connect(r"D:\\Anurakbodin_python\\guitest.db")
            c = conn.cursor()
            try:
                data = ("Free","-","-","-",0,0,0,0)
                c.execute('UPDATE room set availability =?,first_name=?,last_name=?,tel=?,first_day=?,last_day=?,day=?,total=? WHERE No =3',data)
                conn.commit()
                conn.close()
            except sqlite3.Error as e:
                print('Failed to insert : ',e)
            finally :
                if conn :
                    conn.close()
            messagebox.showinfo("Completed","Cancel Booking Completed")
            back_cancelbook()
        conn = sqlite3.connect(r"D:\\Anurakbodin_python\\guitest.db")
        c = conn.cursor()
        c.execute('select total FROM room WHERE No = 3')
        result = c.fetchall()
        for x in result:
            total = x[0]
        servicecharge = total*10/100
        Label(window,text = "If you cancel booking, 10 percent of the total rental price will be charged.", bg='#66ccff').place(relx=0.5, rely=0.4, relwidth=0.45, relheight=0.1, anchor='n')
        Label(window,text = ("Total=",servicecharge), bg='#66ccff').place(relx=0.5, rely=0.5, relwidth=0.45, relheight=0.1, anchor='n')
        Button(window,text = "ENTER",command = comfirm_cancel_book3, bg='#999999').place(relx=0.4, rely=0.65, relwidth=0.1, relheight=0.1, anchor='n')
        Button(window,text = "BACK",command = cancelBook3, bg='#999999').place(relx=0.6, rely=0.65, relwidth=0.1, relheight=0.1, anchor='n')
    conn = sqlite3.connect(r"D:\\Anurakbodin_python\\guitest.db")
    c = conn.cursor()
    c.execute('select first_name FROM room WHERE No = 3')
    result = c.fetchall()
    for x in result:
        Label(window,text = x, bg='#ff0099').place(relx=0.6, rely=0.42, relwidth=0.2, relheight=0.1, anchor='n')
    c.execute('select last_name FROM room WHERE No = 3')
    result = c.fetchall()
    for x in result:
        Label(window,text = x, bg='#ff00ff').place(relx=0.6, rely=0.52, relwidth=0.2, relheight=0.1, anchor='n')

    c.execute('select tel FROM room WHERE No = 3')
    result = c.fetchall()
    for x in result:
        Label(window,text = x, bg='#ff66ff').place(relx=0.6, rely=0.62, relwidth=0.2, relheight=0.1, anchor='n')
    c.execute('select total FROM room WHERE No = 3')
    result = c.fetchall()
    for x in result:
        Label(window,text = x, bg='#ff99ff').place(relx=0.6, rely=0.72, relwidth=0.2, relheight=0.1, anchor='n')
    Button(window,text = "Cancel Booking",command = cancel_book3, bg='#999999').place(relx=0.4, rely=0.85, relwidth=0.1, relheight=0.1, anchor='n')
    Button(window,text = "BACK",command = back_cancelbook, bg='#999999').place(relx=0.6, rely=0.85, relwidth=0.1, relheight=0.1, anchor='n')
########################
def cancelBook4():
    win_screen = tk.Frame(window, bg= '#cccc99', bd=5)
    win_screen.place(relx=0.5, rely=0.252, relwidth=0.6, relheight=0.74, anchor='n')
    frame = tk.Frame(window, bg='#ff9966')
    frame.place(relx = 0.5, rely=0.29, relwidth=0.5, relheight=0.7, anchor='n')
    Label(window,text = "No 4", bg= '#fff000').place(relx=0.5, rely=0.3, relwidth=0.2, relheight=0.1, anchor='n')
    Label(window,text = "First Name ->", bg= '#0066ff').place(relx=0.4, rely=0.42, relwidth=0.2, relheight=0.1, anchor='n')
    Label(window,text = "Last Name ->", bg= '#3399ff').place(relx=0.4, rely=0.52, relwidth=0.2, relheight=0.1, anchor='n')
    Label(window,text = "Tel ->", bg= '#66ccff').place(relx=0.4, rely=0.62, relwidth=0.2, relheight=0.1, anchor='n')
    Label(window,text = "Total ->", bg= '#99ccff').place(relx=0.4, rely=0.72, relwidth=0.2, relheight=0.1, anchor='n')
    def cancel_book4() :
        win_screen = tk.Frame(window, bg= '#cccc99', bd=5)
        win_screen.place(relx=0.5, rely=0.252, relwidth=0.6, relheight=0.74, anchor='n')
        frame = tk.Frame(window, bg='#ff9966')
        frame.place(relx = 0.5, rely=0.38, relwidth=0.5, relheight=0.4, anchor='n')
        def comfirm_cancel_book4():
            conn = sqlite3.connect(r"D:\\Anurakbodin_python\\guitest.db")
            c = conn.cursor()
            try:
                data = ("Free","-","-","-",0,0,0,0)
                c.execute('UPDATE room set availability =?,first_name=?,last_name=?,tel=?,first_day=?,last_day=?,day=?,total=? WHERE No =4',data)
                conn.commit()
                conn.close()
            except sqlite3.Error as e:
                print('Failed to insert : ',e)
            finally :
                if conn :
                    conn.close()
            messagebox.showinfo("Completed","Cancel Booking Completed")
            back_cancelbook()
        conn = sqlite3.connect(r"D:\\Anurakbodin_python\\guitest.db")
        c = conn.cursor()
        c.execute('select total FROM room WHERE No = 4')
        result = c.fetchall()
        for x in result:
            total = x[0]
        servicecharge = total*10/100
        Label(window,text = "If you cancel booking, 10 percent of the total rental price will be charged.", bg='#66ccff').place(relx=0.5, rely=0.4, relwidth=0.45, relheight=0.1, anchor='n')
        Label(window,text = ("Total=",servicecharge), bg='#66ccff').place(relx=0.5, rely=0.5, relwidth=0.45, relheight=0.1, anchor='n')
        Button(window,text = "ENTER",command = comfirm_cancel_book4, bg='#999999').place(relx=0.4, rely=0.65, relwidth=0.1, relheight=0.1, anchor='n')
        Button(window,text = "BACK",command = cancelBook4, bg='#999999').place(relx=0.6, rely=0.65, relwidth=0.1, relheight=0.1, anchor='n')
    conn = sqlite3.connect(r"D:\\Anurakbodin_python\\guitest.db")
    c = conn.cursor()
    c.execute('select first_name FROM room WHERE No = 4')
    result = c.fetchall()
    for x in result:
        Label(window,text = x, bg='#ff0099').place(relx=0.6, rely=0.42, relwidth=0.2, relheight=0.1, anchor='n')
    c.execute('select last_name FROM room WHERE No = 4')
    result = c.fetchall()
    for x in result:
        Label(window,text = x, bg='#ff00ff').place(relx=0.6, rely=0.52, relwidth=0.2, relheight=0.1, anchor='n')

    c.execute('select tel FROM room WHERE No = 4')
    result = c.fetchall()
    for x in result:
        Label(window,text = x, bg='#ff66ff').place(relx=0.6, rely=0.62, relwidth=0.2, relheight=0.1, anchor='n')
    c.execute('select total FROM room WHERE No = 4')
    result = c.fetchall()
    for x in result:
        Label(window,text = x, bg='#ff99ff').place(relx=0.6, rely=0.72, relwidth=0.2, relheight=0.1, anchor='n')
    Button(window,text = "Cancel Booking",command = cancel_book4, bg='#999999').place(relx=0.4, rely=0.85, relwidth=0.1, relheight=0.1, anchor='n')
    Button(window,text = "BACK",command = back_cancelbook, bg='#999999').place(relx=0.6, rely=0.85, relwidth=0.1, relheight=0.1, anchor='n')
########################
def cancelBook5():
    win_screen = tk.Frame(window, bg= '#cccc99', bd=5)
    win_screen.place(relx=0.5, rely=0.252, relwidth=0.6, relheight=0.74, anchor='n')
    frame = tk.Frame(window, bg='#ff9966')
    frame.place(relx = 0.5, rely=0.29, relwidth=0.5, relheight=0.7, anchor='n')
    Label(window,text = "No 5", bg= '#fff000').place(relx=0.5, rely=0.3, relwidth=0.2, relheight=0.1, anchor='n')
    Label(window,text = "First Name ->", bg= '#0066ff').place(relx=0.4, rely=0.42, relwidth=0.2, relheight=0.1, anchor='n')
    Label(window,text = "Last Name ->", bg= '#3399ff').place(relx=0.4, rely=0.52, relwidth=0.2, relheight=0.1, anchor='n')
    Label(window,text = "Tel ->", bg= '#66ccff').place(relx=0.4, rely=0.62, relwidth=0.2, relheight=0.1, anchor='n')
    Label(window,text = "Total ->", bg= '#99ccff').place(relx=0.4, rely=0.72, relwidth=0.2, relheight=0.1, anchor='n')
    def cancel_book5() :
        win_screen = tk.Frame(window, bg= '#cccc99', bd=5)
        win_screen.place(relx=0.5, rely=0.252, relwidth=0.6, relheight=0.74, anchor='n')
        frame = tk.Frame(window, bg='#ff9966')
        frame.place(relx = 0.5, rely=0.38, relwidth=0.5, relheight=0.4, anchor='n')
        def comfirm_cancel_book5():
            conn = sqlite3.connect(r"D:\\Anurakbodin_python\\guitest.db")
            c = conn.cursor()
            try:
                data = ("Free","-","-","-",0,0,0,0)
                c.execute('UPDATE room set availability =?,first_name=?,last_name=?,tel=?,first_day=?,last_day=?,day=?,total=? WHERE No =5',data)
                conn.commit()
                conn.close()
            except sqlite3.Error as e:
                print('Failed to insert : ',e)
            finally :
                if conn :
                    conn.close()
            messagebox.showinfo("Completed","Cancel Booking Completed")
            back_cancelbook()
        conn = sqlite3.connect(r"D:\\Anurakbodin_python\\guitest.db")
        c = conn.cursor()
        c.execute('select total FROM room WHERE No = 5')
        result = c.fetchall()
        for x in result:
            total = x[0]
        servicecharge = total*10/100
        Label(window,text = "If you cancel booking, 10 percent of the total rental price will be charged.", bg='#66ccff').place(relx=0.5, rely=0.4, relwidth=0.45, relheight=0.1, anchor='n')
        Label(window,text = ("Total=",servicecharge), bg='#66ccff').place(relx=0.5, rely=0.5, relwidth=0.45, relheight=0.1, anchor='n')
        Button(window,text = "ENTER",command = comfirm_cancel_book5, bg='#999999').place(relx=0.4, rely=0.65, relwidth=0.1, relheight=0.1, anchor='n')
        Button(window,text = "BACK",command = cancelBook5, bg='#999999').place(relx=0.6, rely=0.65, relwidth=0.1, relheight=0.1, anchor='n')
    conn = sqlite3.connect(r"D:\\Anurakbodin_python\\guitest.db")
    c = conn.cursor()
    c.execute('select first_name FROM room WHERE No = 5')
    result = c.fetchall()
    for x in result:
        Label(window,text = x, bg='#ff0099').place(relx=0.6, rely=0.42, relwidth=0.2, relheight=0.1, anchor='n')
    c.execute('select last_name FROM room WHERE No = 5')
    result = c.fetchall()
    for x in result:
        Label(window,text = x, bg='#ff00ff').place(relx=0.6, rely=0.52, relwidth=0.2, relheight=0.1, anchor='n')

    c.execute('select tel FROM room WHERE No = 5')
    result = c.fetchall()
    for x in result:
        Label(window,text = x, bg='#ff66ff').place(relx=0.6, rely=0.62, relwidth=0.2, relheight=0.1, anchor='n')
    c.execute('select total FROM room WHERE No = 5')
    result = c.fetchall()
    for x in result:
        Label(window,text = x, bg='#ff99ff').place(relx=0.6, rely=0.72, relwidth=0.2, relheight=0.1, anchor='n')
    Button(window,text = "Cancel Booking",command = cancel_book5, bg='#999999').place(relx=0.4, rely=0.85, relwidth=0.1, relheight=0.1, anchor='n')
    Button(window,text = "BACK",command = back_cancelbook, bg='#999999').place(relx=0.6, rely=0.85, relwidth=0.1, relheight=0.1, anchor='n')
########################
def cancelBook6():
    win_screen = tk.Frame(window, bg= '#cccc99', bd=5)
    win_screen.place(relx=0.5, rely=0.252, relwidth=0.6, relheight=0.74, anchor='n')
    frame = tk.Frame(window, bg='#ff9966')
    frame.place(relx = 0.5, rely=0.29, relwidth=0.5, relheight=0.7, anchor='n')
    Label(window,text = "No 6", bg= '#fff000').place(relx=0.5, rely=0.3, relwidth=0.2, relheight=0.1, anchor='n')
    Label(window,text = "First Name ->", bg= '#0066ff').place(relx=0.4, rely=0.42, relwidth=0.2, relheight=0.1, anchor='n')
    Label(window,text = "Last Name ->", bg= '#3399ff').place(relx=0.4, rely=0.52, relwidth=0.2, relheight=0.1, anchor='n')
    Label(window,text = "Tel ->", bg= '#66ccff').place(relx=0.4, rely=0.62, relwidth=0.2, relheight=0.1, anchor='n')
    Label(window,text = "Total ->", bg= '#99ccff').place(relx=0.4, rely=0.72, relwidth=0.2, relheight=0.1, anchor='n')
    def cancel_book6() :
        win_screen = tk.Frame(window, bg= '#cccc99', bd=5)
        win_screen.place(relx=0.5, rely=0.252, relwidth=0.6, relheight=0.74, anchor='n')
        frame = tk.Frame(window, bg='#ff9966')
        frame.place(relx = 0.5, rely=0.38, relwidth=0.5, relheight=0.4, anchor='n')
        def comfirm_cancel_book6():
            conn = sqlite3.connect(r"D:\\Anurakbodin_python\\guitest.db")
            c = conn.cursor()
            try:
                data = ("Free","-","-","-",0,0,0,0)
                c.execute('UPDATE room set availability =?,first_name=?,last_name=?,tel=?,first_day=?,last_day=?,day=?,total=? WHERE No =6',data)
                conn.commit()
                conn.close()
            except sqlite3.Error as e:
                print('Failed to insert : ',e)
            finally :
                if conn :
                    conn.close()
            messagebox.showinfo("Completed","Cancel Booking Completed")
            back_cancelbook()
        conn = sqlite3.connect(r"D:\\Anurakbodin_python\\guitest.db")
        c = conn.cursor()
        c.execute('select total FROM room WHERE No = 6')
        result = c.fetchall()
        for x in result:
            total = x[0]
        servicecharge = total*10/100
        Label(window,text = "If you cancel booking, 10 percent of the total rental price will be charged.", bg='#66ccff').place(relx=0.5, rely=0.4, relwidth=0.45, relheight=0.1, anchor='n')
        Label(window,text = ("Total=",servicecharge), bg='#66ccff').place(relx=0.5, rely=0.5, relwidth=0.45, relheight=0.1, anchor='n')
        Button(window,text = "ENTER",command = comfirm_cancel_book6, bg='#999999').place(relx=0.4, rely=0.65, relwidth=0.1, relheight=0.1, anchor='n')
        Button(window,text = "BACK",command = cancelBook6, bg='#999999').place(relx=0.6, rely=0.65, relwidth=0.1, relheight=0.1, anchor='n')
    conn = sqlite3.connect(r"D:\\Anurakbodin_python\\guitest.db")
    c = conn.cursor()
    c.execute('select first_name FROM room WHERE No = 6')
    result = c.fetchall()
    for x in result:
        Label(window,text = x, bg='#ff0099').place(relx=0.6, rely=0.42, relwidth=0.2, relheight=0.1, anchor='n')
    c.execute('select last_name FROM room WHERE No = 6')
    result = c.fetchall()
    for x in result:
        Label(window,text = x, bg='#ff00ff').place(relx=0.6, rely=0.52, relwidth=0.2, relheight=0.1, anchor='n')

    c.execute('select tel FROM room WHERE No = 6')
    result = c.fetchall()
    for x in result:
        Label(window,text = x, bg='#ff66ff').place(relx=0.6, rely=0.62, relwidth=0.2, relheight=0.1, anchor='n')
    c.execute('select total FROM room WHERE No = 6')
    result = c.fetchall()
    for x in result:
        Label(window,text = x, bg='#ff99ff').place(relx=0.6, rely=0.72, relwidth=0.2, relheight=0.1, anchor='n')
    Button(window,text = "Cancel Booking",command = cancel_book6, bg='#999999').place(relx=0.4, rely=0.85, relwidth=0.1, relheight=0.1, anchor='n')
    Button(window,text = "BACK",command = back_cancelbook, bg='#999999').place(relx=0.6, rely=0.85, relwidth=0.1, relheight=0.1, anchor='n')
########################
def cancelBook7():
    win_screen = tk.Frame(window, bg= '#cccc99', bd=5)
    win_screen.place(relx=0.5, rely=0.252, relwidth=0.6, relheight=0.74, anchor='n')
    frame = tk.Frame(window, bg='#ff9966')
    frame.place(relx = 0.5, rely=0.29, relwidth=0.5, relheight=0.7, anchor='n')
    Label(window,text = "No 7", bg= '#fff000').place(relx=0.5, rely=0.3, relwidth=0.2, relheight=0.1, anchor='n')
    Label(window,text = "First Name ->", bg= '#0066ff').place(relx=0.4, rely=0.42, relwidth=0.2, relheight=0.1, anchor='n')
    Label(window,text = "Last Name ->", bg= '#3399ff').place(relx=0.4, rely=0.52, relwidth=0.2, relheight=0.1, anchor='n')
    Label(window,text = "Tel ->", bg= '#66ccff').place(relx=0.4, rely=0.62, relwidth=0.2, relheight=0.1, anchor='n')
    Label(window,text = "Total ->", bg= '#99ccff').place(relx=0.4, rely=0.72, relwidth=0.2, relheight=0.1, anchor='n')
    def cancel_book7() :
        win_screen = tk.Frame(window, bg= '#cccc99', bd=5)
        win_screen.place(relx=0.5, rely=0.252, relwidth=0.6, relheight=0.74, anchor='n')
        frame = tk.Frame(window, bg='#ff9966')
        frame.place(relx = 0.5, rely=0.38, relwidth=0.5, relheight=0.4, anchor='n')
        def comfirm_cancel_book7():
            conn = sqlite3.connect(r"D:\\Anurakbodin_python\\guitest.db")
            c = conn.cursor()
            try:
                data = ("Free","-","-","-",0,0,0,0)
                c.execute('UPDATE room set availability =?,first_name=?,last_name=?,tel=?,first_day=?,last_day=?,day=?,total=? WHERE No =7',data)
                conn.commit()
                conn.close()
            except sqlite3.Error as e:
                print('Failed to insert : ',e)
            finally :
                if conn :
                    conn.close()
            messagebox.showinfo("Completed","Cancel Booking Completed")
            back_cancelbook()
        conn = sqlite3.connect(r"D:\\Anurakbodin_python\\guitest.db")
        c = conn.cursor()
        c.execute('select total FROM room WHERE No = 7')
        result = c.fetchall()
        for x in result:
            total = x[0]
        servicecharge = total*10/100
        Label(window,text = "If you cancel booking, 10 percent of the total rental price will be charged.", bg='#66ccff').place(relx=0.5, rely=0.4, relwidth=0.45, relheight=0.1, anchor='n')
        Label(window,text = ("Total=",servicecharge), bg='#66ccff').place(relx=0.5, rely=0.5, relwidth=0.45, relheight=0.1, anchor='n')
        Button(window,text = "ENTER",command = comfirm_cancel_book7, bg='#999999').place(relx=0.4, rely=0.65, relwidth=0.1, relheight=0.1, anchor='n')
        Button(window,text = "BACK",command = cancelBook7, bg='#999999').place(relx=0.6, rely=0.65, relwidth=0.1, relheight=0.1, anchor='n')
    conn = sqlite3.connect(r"D:\\Anurakbodin_python\\guitest.db")
    c = conn.cursor()
    c.execute('select first_name FROM room WHERE No = 7')
    result = c.fetchall()
    for x in result:
        Label(window,text = x, bg='#ff0099').place(relx=0.6, rely=0.42, relwidth=0.2, relheight=0.1, anchor='n')
    c.execute('select last_name FROM room WHERE No = 7')
    result = c.fetchall()
    for x in result:
        Label(window,text = x, bg='#ff00ff').place(relx=0.6, rely=0.52, relwidth=0.2, relheight=0.1, anchor='n')

    c.execute('select tel FROM room WHERE No = 7')
    result = c.fetchall()
    for x in result:
        Label(window,text = x, bg='#ff66ff').place(relx=0.6, rely=0.62, relwidth=0.2, relheight=0.1, anchor='n')
    c.execute('select total FROM room WHERE No = 7')
    result = c.fetchall()
    for x in result:
        Label(window,text = x, bg='#ff99ff').place(relx=0.6, rely=0.72, relwidth=0.2, relheight=0.1, anchor='n')
    Button(window,text = "Cancel Booking",command = cancel_book7, bg='#999999').place(relx=0.4, rely=0.85, relwidth=0.1, relheight=0.1, anchor='n')
    Button(window,text = "BACK",command = back_cancelbook, bg='#999999').place(relx=0.6, rely=0.85, relwidth=0.1, relheight=0.1, anchor='n')
########################
def cancelBook8():
    win_screen = tk.Frame(window, bg= '#cccc99', bd=5)
    win_screen.place(relx=0.5, rely=0.252, relwidth=0.6, relheight=0.74, anchor='n')
    frame = tk.Frame(window, bg='#ff9966')
    frame.place(relx = 0.5, rely=0.29, relwidth=0.5, relheight=0.7, anchor='n')
    Label(window,text = "No 8", bg= '#fff000').place(relx=0.5, rely=0.3, relwidth=0.2, relheight=0.1, anchor='n')
    Label(window,text = "First Name ->", bg= '#0066ff').place(relx=0.4, rely=0.42, relwidth=0.2, relheight=0.1, anchor='n')
    Label(window,text = "Last Name ->", bg= '#3399ff').place(relx=0.4, rely=0.52, relwidth=0.2, relheight=0.1, anchor='n')
    Label(window,text = "Tel ->", bg= '#66ccff').place(relx=0.4, rely=0.62, relwidth=0.2, relheight=0.1, anchor='n')
    Label(window,text = "Total ->", bg= '#99ccff').place(relx=0.4, rely=0.72, relwidth=0.2, relheight=0.1, anchor='n')
    def cancel_book8() :
        win_screen = tk.Frame(window, bg= '#cccc99', bd=5)
        win_screen.place(relx=0.5, rely=0.252, relwidth=0.6, relheight=0.74, anchor='n')
        frame = tk.Frame(window, bg='#ff9966')
        frame.place(relx = 0.5, rely=0.38, relwidth=0.5, relheight=0.4, anchor='n')
        def comfirm_cancel_book8():
            conn = sqlite3.connect(r"D:\\Anurakbodin_python\\guitest.db")
            c = conn.cursor()
            try:
                data = ("Free","-","-","-",0,0,0,0)
                c.execute('UPDATE room set availability =?,first_name=?,last_name=?,tel=?,first_day=?,last_day=?,day=?,total=? WHERE No =8',data)
                conn.commit()
                conn.close()
            except sqlite3.Error as e:
                print('Failed to insert : ',e)
            finally :
                if conn :
                    conn.close()
            messagebox.showinfo("Completed","Cancel Booking Completed")
            back_cancelbook()
        conn = sqlite3.connect(r"D:\\Anurakbodin_python\\guitest.db")
        c = conn.cursor()
        c.execute('select total FROM room WHERE No = 8')
        result = c.fetchall()
        for x in result:
            total = x[0]
        servicecharge = total*10/100
        Label(window,text = "If you cancel booking, 10 percent of the total rental price will be charged.", bg='#66ccff').place(relx=0.5, rely=0.4, relwidth=0.45, relheight=0.1, anchor='n')
        Label(window,text = ("Total=",servicecharge), bg='#66ccff').place(relx=0.5, rely=0.5, relwidth=0.45, relheight=0.1, anchor='n')
        Button(window,text = "ENTER",command = comfirm_cancel_book8, bg='#999999').place(relx=0.4, rely=0.65, relwidth=0.1, relheight=0.1, anchor='n')
        Button(window,text = "BACK",command = cancelBook8, bg='#999999').place(relx=0.6, rely=0.65, relwidth=0.1, relheight=0.1, anchor='n')
    conn = sqlite3.connect(r"D:\\Anurakbodin_python\\guitest.db")
    c = conn.cursor()
    c.execute('select first_name FROM room WHERE No = 8')
    result = c.fetchall()
    for x in result:
        Label(window,text = x, bg='#ff0099').place(relx=0.6, rely=0.42, relwidth=0.2, relheight=0.1, anchor='n')
    c.execute('select last_name FROM room WHERE No = 8')
    result = c.fetchall()
    for x in result:
        Label(window,text = x, bg='#ff00ff').place(relx=0.6, rely=0.52, relwidth=0.2, relheight=0.1, anchor='n')

    c.execute('select tel FROM room WHERE No = 8')
    result = c.fetchall()
    for x in result:
        Label(window,text = x, bg='#ff66ff').place(relx=0.6, rely=0.62, relwidth=0.2, relheight=0.1, anchor='n')
    c.execute('select total FROM room WHERE No = 8')
    result = c.fetchall()
    for x in result:
        Label(window,text = x, bg='#ff99ff').place(relx=0.6, rely=0.72, relwidth=0.2, relheight=0.1, anchor='n')
    Button(window,text = "Cancel Booking",command = cancel_book8, bg='#999999').place(relx=0.4, rely=0.85, relwidth=0.1, relheight=0.1, anchor='n')
    Button(window,text = "BACK",command = back_cancelbook, bg='#999999').place(relx=0.6, rely=0.85, relwidth=0.1, relheight=0.1, anchor='n')
########################
def cancelBook9():
    win_screen = tk.Frame(window, bg= '#cccc99', bd=5)
    win_screen.place(relx=0.5, rely=0.252, relwidth=0.6, relheight=0.74, anchor='n')
    frame = tk.Frame(window, bg='#ff9966')
    frame.place(relx = 0.5, rely=0.29, relwidth=0.5, relheight=0.7, anchor='n')
    Label(window,text = "No 9", bg= '#fff000').place(relx=0.5, rely=0.3, relwidth=0.2, relheight=0.1, anchor='n')
    Label(window,text = "First Name ->", bg= '#0066ff').place(relx=0.4, rely=0.42, relwidth=0.2, relheight=0.1, anchor='n')
    Label(window,text = "Last Name ->", bg= '#3399ff').place(relx=0.4, rely=0.52, relwidth=0.2, relheight=0.1, anchor='n')
    Label(window,text = "Tel ->", bg= '#66ccff').place(relx=0.4, rely=0.62, relwidth=0.2, relheight=0.1, anchor='n')
    Label(window,text = "Total ->", bg= '#99ccff').place(relx=0.4, rely=0.72, relwidth=0.2, relheight=0.1, anchor='n')
    def cancel_book9() :
        win_screen = tk.Frame(window, bg= '#cccc99', bd=5)
        win_screen.place(relx=0.5, rely=0.252, relwidth=0.6, relheight=0.74, anchor='n')
        frame = tk.Frame(window, bg='#ff9966')
        frame.place(relx = 0.5, rely=0.38, relwidth=0.5, relheight=0.4, anchor='n')
        def comfirm_cancel_book9():
            conn = sqlite3.connect(r"D:\\Anurakbodin_python\\guitest.db")
            c = conn.cursor()
            try:
                data = ("Free","-","-","-",0,0,0,0)
                c.execute('UPDATE room set availability =?,first_name=?,last_name=?,tel=?,first_day=?,last_day=?,day=?,total=? WHERE No =9',data)
                conn.commit()
                conn.close()
            except sqlite3.Error as e:
                print('Failed to insert : ',e)
            finally :
                if conn :
                    conn.close()
            messagebox.showinfo("Completed","Cancel Booking Completed")
            back_cancelbook()
        conn = sqlite3.connect(r"D:\\Anurakbodin_python\\guitest.db")
        c = conn.cursor()
        c.execute('select total FROM room WHERE No = 9')
        result = c.fetchall()
        for x in result:
            total = x[0]
        servicecharge = total*10/100
        Label(window,text = "If you cancel booking, 10 percent of the total rental price will be charged.", bg='#66ccff').place(relx=0.5, rely=0.4, relwidth=0.45, relheight=0.1, anchor='n')
        Label(window,text = ("Total=",servicecharge), bg='#66ccff').place(relx=0.5, rely=0.5, relwidth=0.45, relheight=0.1, anchor='n')
        Button(window,text = "ENTER",command = comfirm_cancel_book9, bg='#999999').place(relx=0.4, rely=0.65, relwidth=0.1, relheight=0.1, anchor='n')
        Button(window,text = "BACK",command = cancelBook9, bg='#999999').place(relx=0.6, rely=0.65, relwidth=0.1, relheight=0.1, anchor='n')
    conn = sqlite3.connect(r"D:\\Anurakbodin_python\\guitest.db")
    c = conn.cursor()
    c.execute('select first_name FROM room WHERE No = 9')
    result = c.fetchall()
    for x in result:
        Label(window,text = x, bg='#ff0099').place(relx=0.6, rely=0.42, relwidth=0.2, relheight=0.1, anchor='n')
    c.execute('select last_name FROM room WHERE No = 9')
    result = c.fetchall()
    for x in result:
        Label(window,text = x, bg='#ff00ff').place(relx=0.6, rely=0.52, relwidth=0.2, relheight=0.1, anchor='n')

    c.execute('select tel FROM room WHERE No = 9')
    result = c.fetchall()
    for x in result:
        Label(window,text = x, bg='#ff66ff').place(relx=0.6, rely=0.62, relwidth=0.2, relheight=0.1, anchor='n')
    c.execute('select total FROM room WHERE No = 9')
    result = c.fetchall()
    for x in result:
        Label(window,text = x, bg='#ff99ff').place(relx=0.6, rely=0.72, relwidth=0.2, relheight=0.1, anchor='n')
    Button(window,text = "Cancel Booking",command = cancel_book9, bg='#999999').place(relx=0.4, rely=0.85, relwidth=0.1, relheight=0.1, anchor='n')
    Button(window,text = "BACK",command = back_cancelbook, bg='#999999').place(relx=0.6, rely=0.85, relwidth=0.1, relheight=0.1, anchor='n')
########################
def cancelBook10():
    win_screen = tk.Frame(window, bg= '#cccc99', bd=5)
    win_screen.place(relx=0.5, rely=0.252, relwidth=0.6, relheight=0.74, anchor='n')
    frame = tk.Frame(window, bg='#ff9966')
    frame.place(relx = 0.5, rely=0.29, relwidth=0.5, relheight=0.7, anchor='n')
    Label(window,text = "No 10", bg= '#fff000').place(relx=0.5, rely=0.3, relwidth=0.2, relheight=0.1, anchor='n')
    Label(window,text = "First Name ->", bg= '#0066ff').place(relx=0.4, rely=0.42, relwidth=0.2, relheight=0.1, anchor='n')
    Label(window,text = "Last Name ->", bg= '#3399ff').place(relx=0.4, rely=0.52, relwidth=0.2, relheight=0.1, anchor='n')
    Label(window,text = "Tel ->", bg= '#66ccff').place(relx=0.4, rely=0.62, relwidth=0.2, relheight=0.1, anchor='n')
    Label(window,text = "Total ->", bg= '#99ccff').place(relx=0.4, rely=0.72, relwidth=0.2, relheight=0.1, anchor='n')
    def cancel_book10() :
        win_screen = tk.Frame(window, bg= '#cccc99', bd=5)
        win_screen.place(relx=0.5, rely=0.252, relwidth=0.6, relheight=0.74, anchor='n')
        frame = tk.Frame(window, bg='#ff9966')
        frame.place(relx = 0.5, rely=0.38, relwidth=0.5, relheight=0.4, anchor='n')
        def comfirm_cancel_book10():
            conn = sqlite3.connect(r"D:\\Anurakbodin_python\\guitest.db")
            c = conn.cursor()
            try:
                data = ("Free","-","-","-",0,0,0,0)
                c.execute('UPDATE room set availability =?,first_name=?,last_name=?,tel=?,first_day=?,last_day=?,day=?,total=? WHERE No =10',data)
                conn.commit()
                conn.close()
            except sqlite3.Error as e:
                print('Failed to insert : ',e)
            finally :
                if conn :
                    conn.close()
            messagebox.showinfo("Completed","Cancel Booking Completed")
            back_cancelbook()
        conn = sqlite3.connect(r"D:\\Anurakbodin_python\\guitest.db")
        c = conn.cursor()
        c.execute('select total FROM room WHERE No = 10')
        result = c.fetchall()
        for x in result:
            total = x[0]
        servicecharge = total*10/100
        Label(window,text = "If you cancel booking, 10 percent of the total rental price will be charged.", bg='#66ccff').place(relx=0.5, rely=0.4, relwidth=0.45, relheight=0.1, anchor='n')
        Label(window,text = ("Total=",servicecharge), bg='#66ccff').place(relx=0.5, rely=0.5, relwidth=0.45, relheight=0.1, anchor='n')
        Button(window,text = "ENTER",command = comfirm_cancel_book10, bg='#999999').place(relx=0.4, rely=0.65, relwidth=0.1, relheight=0.1, anchor='n')
        Button(window,text = "BACK",command = cancelBook10, bg='#999999').place(relx=0.6, rely=0.65, relwidth=0.1, relheight=0.1, anchor='n')
    conn = sqlite3.connect(r"D:\\Anurakbodin_python\\guitest.db")
    c = conn.cursor()
    c.execute('select first_name FROM room WHERE No = 10')
    result = c.fetchall()
    for x in result:
        Label(window,text = x, bg='#ff0099').place(relx=0.6, rely=0.42, relwidth=0.2, relheight=0.1, anchor='n')
    c.execute('select last_name FROM room WHERE No = 10')
    result = c.fetchall()
    for x in result:
        Label(window,text = x, bg='#ff00ff').place(relx=0.6, rely=0.52, relwidth=0.2, relheight=0.1, anchor='n')

    c.execute('select tel FROM room WHERE No = 10')
    result = c.fetchall()
    for x in result:
        Label(window,text = x, bg='#ff66ff').place(relx=0.6, rely=0.62, relwidth=0.2, relheight=0.1, anchor='n')
    c.execute('select total FROM room WHERE No = 10')
    result = c.fetchall()
    for x in result:
        Label(window,text = x, bg='#ff99ff').place(relx=0.6, rely=0.72, relwidth=0.2, relheight=0.1, anchor='n')
    Button(window,text = "Cancel Booking",command = cancel_book10, bg='#999999').place(relx=0.4, rely=0.85, relwidth=0.1, relheight=0.1, anchor='n')
    Button(window,text = "BACK",command = back_cancelbook, bg='#999999').place(relx=0.6, rely=0.85, relwidth=0.1, relheight=0.1, anchor='n')
########################


def log_out():
    win_screen = tk.Frame(window, bg= '#cccc99', bd=5)
    win_screen.place(relx=0.5, rely=0.252, relwidth=0.6, relheight=0.74, anchor='n')
    frame = tk.Frame(window, bg='#99ffff')
    frame.place(relx = 0.5, rely=0.35, relwidth=0.4, relheight=0.4, anchor='n')
    Label(window,text = "COMFIRM LOGOUT",bg='#ff99ff').place(relx=0.5, rely=0.38, relwidth=0.3, relheight=0.1, anchor='n')
    def logout():
        messagebox.showinfo("Completed","Logout Successful")
        clear()
        start()
    lc1 = Button(window, text='ENTER',command = logout, bg='#00ccff', fg='#000000').place(relx=0.5, rely=0.503, relwidth=0.3, relheight=0.1, anchor='n')
    lc2 = Button(window, text='BACK',command = login_com, bg='#00ccff', fg='#000000').place(relx=0.5, rely=0.606, relwidth=0.3, relheight=0.1, anchor='n') 
########################
def start():
    win_screen = tk.Frame(window, bg= '#cccc99', bd=5)
    win_screen.place(relx=0.5, rely=0.252, relwidth=0.6, relheight=0.74, anchor='n')
    frame = tk.Frame(window, bg='#99ffff')
    frame.place(relx = 0.5, rely=0.35, relwidth=0.4, relheight=0.5, anchor='n')
    tnow = Label(font='times 16')
    def tick():
        global curtime
        now = datetime.today()
        Label(window,text = now.ctime(),bg='#ff99ff').place(relx=0.9, rely=0, relwidth=0.2, relheight=0.08, anchor='n')
        tnow.after(1000, tick)
    tick()
    Label(window,text = "MENU", bg='#ff99ff').place(relx=0.5, rely=0.38, relwidth=0.2, relheight=0.1, anchor='n')
    m1 = Button(window, text='Login',command = login, bg='#00ccff', fg='#000000').place(relx=0.5, rely=0.503, relwidth=0.3, relheight=0.1, anchor='n')
    m2 = Button(window, text='Register',command = register, bg='#00ccff', fg='#000000').place(relx=0.5, rely=0.606, relwidth=0.3, relheight=0.1, anchor='n')
    m3 = Button(window, text='Exit',command = exit_pro, bg='#00ccff', fg='#000000').place(relx=0.5, rely=0.709, relwidth=0.3, relheight=0.1, anchor='n')
#######################
def exit_pro():
    win_screen = tk.Frame(window, bg= '#cccc99', bd=5)
    win_screen.place(relx=0.5, rely=0.252, relwidth=0.6, relheight=0.74, anchor='n')
    frame = tk.Frame(window, bg='#99ffff')
    frame.place(relx = 0.5, rely=0.35, relwidth=0.4, relheight=0.4, anchor='n')
    Label(window,text = "COMFIRM EXIT", bg='#ff99ff').place(relx=0.5, rely=0.38, relwidth=0.3, relheight=0.1, anchor='n')
    e1 = Button(window, text='ENTER',command = window.destroy, bg='#00ccff', fg='#000000').place(relx=0.5, rely=0.503, relwidth=0.3, relheight=0.1, anchor='n')
    e2 = Button(window, text='BACK',command = start, bg='#00ccff', fg='#000000').place(relx=0.5, rely=0.606, relwidth=0.3, relheight=0.1, anchor='n') 
########################
def base():
    photo = PhotoImage(file=r"D:\Anurakbodin_python\ico\pockk.png")
    Label(window, image = photo).pack(anchor='n')
    start()
    frameCnt = 12
    g1 = [PhotoImage(file='D:\Anurakbodin_python\ico\dd.gif',format = 'gif -index %i' %(i)) for i in range(frameCnt)]
    g2 = [PhotoImage(file='D:\Anurakbodin_python\ico\\ad.gif',format = 'gif -index %i' %(i)) for i in range(frameCnt)]    
    def update(ind):
        frame = g1[ind]
        ind += 1
        if ind == frameCnt:
            ind = 0
        x.configure(image=frame)
        window.after(100, update, ind)
    x = Label(window)
    x.place(relx=0, rely=0.5, relwidth=0.2, relheight=0.331)
    window.after(0, update, 0)
    def update1(ind):
        frame = g2[ind]
        ind += 1
        if ind == frameCnt:
            ind = 0
        y.configure(image=frame)
        window.after(100, update1, ind)
    y = Label(window)
    y.place(relx=0.8, rely=0.5, relwidth=0.2, relheight=0.331)
    window.after(0, update1, 0)

    window.mainloop()
########################
def clear():
    user.set("")
    pass_w.set("")
    con.set("")
    re_user.set("")
    re_pass_w.set("")
    re_con.set("")
    fn.set("")
    ln.set("")
    tel.set("")
    fd.set("")
    nd.set("")
    today =""
    firstname =""
    firstday =""
    numday = 0
    lastday = 0
    total = 0
########################
fn = StringVar()
ln = StringVar()
tel = StringVar()
fd = StringVar()
nd = StringVar()
today = ""

user = StringVar()
pass_w = StringVar()
con = StringVar()
re_user = StringVar()
re_pass_w = StringVar()
re_con = StringVar()
base()
