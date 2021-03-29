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

def number(S): #ฟังก์ชันพิมได้เฉพาะค่าตัวเลข
    if S.isdigit():
        return True
    window.bell()
    return False
Nn = (window.register(number), '%S')

def letters(S): #ฟังก์ชันพิมได้เฉพาะค่าตัวอักษร
    if S.isalpha():
        return True
    window.bell()
    return False
Ll = (window.register(letters), '%S')

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
        if len(user_name2) > 0:
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
        else:
            messagebox.showinfo("Incorrect","Please enter username")
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
    lc3 = Button(window, text='Cancel Booking',command = cancelbooking, bg='#00ccff', fg='#000000').place(relx=0.5, rely=0.659, relwidth=0.3, relheight=0.1, anchor='n')
    lc4 = Button(window, text='Logout',command = log_out, bg='#00ccff', fg='#000000').place(relx=0.5, rely=0.762, relwidth=0.3, relheight=0.1, anchor='n')
#######################

def booking():
    win_screen = tk.Frame(window, bg= '#cccc99', bd=5)
    win_screen.place(relx=0.5, rely=0.252, relwidth=0.6, relheight=0.74, anchor='n')
    frame = tk.Frame(window, bg='#3366ff')
    frame.place(relx = 0.5, rely=0.29, relwidth=0.55, relheight=0.6, anchor='n')
    frame = tk.Frame(window, bg='#00ccff')
    frame.place(relx = 0.5, rely=0.295, relwidth=0.545, relheight=0.42, anchor='n')

    def onClick(no):
        win_screen = tk.Frame(window, bg= '#cccc99', bd=5)
        win_screen.place(relx=0.5, rely=0.252, relwidth=0.6, relheight=0.74, anchor='n')
        def booking2():
            win_screen = tk.Frame(window, bg= '#cccc99', bd=5)
            win_screen.place(relx=0.5, rely=0.252, relwidth=0.6, relheight=0.74, anchor='n')
            frame = tk.Frame(window, bg='#990000')
            frame.place(relx = 0.5, rely=0.28, relwidth=0.55, relheight=0.7, anchor='n')
            frame = tk.Frame(window, bg='#99ffff')
            frame.place(relx = 0.5, rely=0.3, relwidth=0.53, relheight=0.66, anchor='n')
            def comfirm():
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
                                if text <= 5 :
                                    total = 500*numday
                                elif text > 5 :
                                    total = 1000*numday
                                Label(window, text=("Total=",total),bg='#ff66ff').place(relx=0.5, rely=0.4, relwidth=0.2, relheight=0.1, anchor='n')
                                Label(window, text=("Confirm Booking"),bg='#ff66ff').place(relx=0.5, rely=0.5, relwidth=0.2, relheight=0.08, anchor='n')
                                def comfirm_book():
                                    conn = sqlite3.connect(r"D:\\Anurakbodin_python\\guitest.db")
                                    c = conn.cursor()
                                    try:
                                        data = ("Busy",str(firstname),str(lastname),str(telephone),int(firstday),int(lastday),int(numday),int(total),text)
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
                            messagebox.showinfo("Incompleted","Please enter a valid phone number.")
                    else:
                        messagebox.showinfo("Incompleted","Please enter your last name") 
                else :
                    messagebox.showinfo("Incompleted","Please enter your first name")

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

            Button(window,text = "ENTER",command = comfirm, bg='#999999').place(relx=0.4, rely=0.85, relwidth=0.1, relheight=0.1, anchor='n')
            Button(window,text = "BACK",command =lambda: onClick(no), bg='#999999').place(relx=0.6, rely=0.85, relwidth=0.1, relheight=0.1, anchor='n')

        Label(window,text = ("No-",no), bg= '#fff000').place(relx=0.5, rely=0.3, relwidth=0.2, relheight=0.1, anchor='n')
        Label(window,text = "category ->", bg= '#3399ff').place(relx=0.45, rely=0.42, relwidth=0.2, relheight=0.1, anchor='n')
        Label(window,text = "cost ->", bg= '#66ccff').place(relx=0.45, rely=0.52, relwidth=0.2, relheight=0.1, anchor='n')
        Label(window,text = "availability ->", bg= '#99ccff').place(relx=0.45, rely=0.62, relwidth=0.2, relheight=0.1, anchor='n')

        conn = sqlite3.connect(r"D:\\Anurakbodin_python\\guitest.db")
        c = conn.cursor()
        data = no,
        c.execute('select category FROM room WHERE No = ?',data)
        result = c.fetchall()
        for x in result:
            Label(window,text = x, bg='#ff00ff').place(relx=0.6, rely=0.42, relwidth=0.1, relheight=0.1, anchor='n')
        data = no,
        c.execute('select cost FROM room WHERE No = ?',data)
        result = c.fetchall()
        for x in result:
            Label(window,text = x, bg='#ff66ff').place(relx=0.6, rely=0.52, relwidth=0.1, relheight=0.1, anchor='n')
        data = no,
        c.execute('select availability FROM room WHERE No = ?',data)
        result = c.fetchall()
        for x in result:
            Label(window,text = x, bg='#ff99ff').place(relx=0.6, rely=0.62, relwidth=0.1, relheight=0.1, anchor='n')
        Button(window,text = "Booking",command = booking2, bg='#999999').place(relx=0.4, rely=0.8, relwidth=0.1, relheight=0.1, anchor='n')
        Button(window,text = "BACK",command = back_book, bg='#999999').place(relx=0.6, rely=0.8, relwidth=0.1, relheight=0.1, anchor='n')
    def back_book():#back book
        clear()
        booking()

    conn = sqlite3.connect(r"D:\\Anurakbodin_python\\guitest.db")
    c = conn.cursor()
    data = 1,
    c.execute('select availability FROM room WHERE No = ?',data)
    result = c.fetchall()
    for x in result:
        ava = str(x).strip("(',)")
    if ava == "Free" :
        Button(text = 1,command=lambda: onClick(1), bg='#00ff00').place(relx=0.28, rely=0.3, relwidth=0.1, relheight=0.2, anchor='n')
    else:
        Label(window,text = 1, bg='#cc3333').place(relx=0.28, rely=0.3, relwidth=0.1, relheight=0.2, anchor='n')

    data = 2,
    c.execute('select availability FROM room WHERE No = ?',data)
    result = c.fetchall()
    for x in result:
        ava = str(x).strip("(',)")
    if ava == "Free" :
        Button(text = 2,command=lambda: onClick(2), bg='#00ff00').place(relx=0.39, rely=0.3, relwidth=0.1, relheight=0.2, anchor='n')
    else:
        Label(window,text = 2, bg='#cc3333').place(relx=0.39, rely=0.3, relwidth=0.1, relheight=0.2, anchor='n')

    data = 3,
    c.execute('select availability FROM room WHERE No = ?',data)
    result = c.fetchall()
    for x in result:
        ava = str(x).strip("(',)")
    if ava == "Free" :
        Button(text = 3,command=lambda: onClick(3), bg='#00ff00').place(relx=0.5, rely=0.3, relwidth=0.1, relheight=0.2, anchor='n')
    else:
        Label(window,text = 3, bg='#cc3333').place(relx=0.5, rely=0.3, relwidth=0.1, relheight=0.2, anchor='n')

    data = 4,
    c.execute('select availability FROM room WHERE No = ?',data)
    result = c.fetchall()
    for x in result:
        ava = str(x).strip("(',)")
    if ava == "Free" :
        Button(text = 4,command=lambda: onClick(4), bg='#00ff00').place(relx=0.61, rely=0.3, relwidth=0.1, relheight=0.2, anchor='n')
    else:
        Label(window,text = 4, bg='#cc3333').place(relx=0.61, rely=0.3, relwidth=0.1, relheight=0.2, anchor='n')

    data = 5,
    c.execute('select availability FROM room WHERE No = ?',data)
    result = c.fetchall()
    for x in result:
        ava = str(x).strip("(',)")
    if ava == "Free" :
        Button(text = 5,command=lambda: onClick(5), bg='#00ff00').place(relx=0.72, rely=0.3, relwidth=0.1, relheight=0.2, anchor='n')
    else:
        Label(window,text = 5, bg='#cc3333').place(relx=0.72, rely=0.3, relwidth=0.1, relheight=0.2, anchor='n')

    data = 6,
    c.execute('select availability FROM room WHERE No = ?',data)
    result = c.fetchall()
    for x in result:
        ava = str(x).strip("(',)")
    if ava == "Free" :
        Button(text = 6,command=lambda: onClick(6), bg='#00ff00').place(relx=0.28, rely=0.51, relwidth=0.1, relheight=0.2, anchor='n')
    else:
        Label(window,text = 6, bg='#cc3333').place(relx=0.28, rely=0.51, relwidth=0.1, relheight=0.2, anchor='n')

    data = 7,
    c.execute('select availability FROM room WHERE No = ?',data)
    result = c.fetchall()
    for x in result:
        ava = str(x).strip("(',)")
    if ava == "Free" :
        Button(text = 7,command=lambda: onClick(7), bg='#00ff00').place(relx=0.39, rely=0.51, relwidth=0.1, relheight=0.2, anchor='n')
    else:
        Label(window,text = 7, bg='#cc3333').place(relx=0.39, rely=0.51, relwidth=0.1, relheight=0.2, anchor='n')

    data = 8,
    c.execute('select availability FROM room WHERE No = ?',data)
    result = c.fetchall()
    for x in result:
        ava = str(x).strip("(',)")
    if ava == "Free" :
        Button(text = 8,command=lambda: onClick(8), bg='#00ff00').place(relx=0.5, rely=0.51, relwidth=0.1, relheight=0.2, anchor='n')
    else:
        Label(window,text = 8, bg='#cc3333').place(relx=0.5, rely=0.51, relwidth=0.1, relheight=0.2, anchor='n')

    data = 9,
    c.execute('select availability FROM room WHERE No = ?',data)
    result = c.fetchall()
    for x in result:
        ava = str(x).strip("(',)")
    if ava == "Free" :
        Button(text = 9,command=lambda: onClick(9), bg='#00ff00').place(relx=0.61, rely=0.51, relwidth=0.1, relheight=0.2, anchor='n')
    else:
        Label(window,text = 9, bg='#cc3333').place(relx=0.61, rely=0.51, relwidth=0.1, relheight=0.2, anchor='n')
    
    data = 10,
    c.execute('select availability FROM room WHERE No = ?',data)
    result = c.fetchall()
    for x in result:
        ava = str(x).strip("(',)")
    if ava == "Free" :
        Button(text = 10,command=lambda: onClick(10), bg='#00ff00').place(relx=0.72, rely=0.51, relwidth=0.1, relheight=0.2, anchor='n')
    else:
        Label(window,text = 10, bg='#cc3333').place(relx=0.72, rely=0.51, relwidth=0.1, relheight=0.2, anchor='n')

    Label(window,text = "Menu BOOKING", bg='#00ccff').place(relx=0.35, rely=0.75, relwidth=0.13, relheight=0.1, anchor='n')
    Label(window,text = "Select Green Room", bg='#00ff00').place(relx=0.65, rely=0.75, relwidth=0.13, relheight=0.1, anchor='n')
    Button(window,text = "BACK",command = login_com, bg='#ffcc99').place(relx=0.5, rely=0.75, relwidth=0.1, relheight=0.1, anchor='n')
#######################

def show():
    win_screen = tk.Frame(window, bg= '#cccc99', bd=5)
    win_screen.place(relx=0.5, rely=0.252, relwidth=0.6, relheight=0.74, anchor='n')
    frame = tk.Frame(window, bg='#3366ff')
    frame.place(relx = 0.5, rely=0.29, relwidth=0.55, relheight=0.6, anchor='n')
    frame = tk.Frame(window, bg='#00ccff')
    frame.place(relx = 0.5, rely=0.295, relwidth=0.545, relheight=0.42, anchor='n')

    def onClick2(no):
        win_screen = tk.Frame(window, bg= '#cccc99', bd=5)
        win_screen.place(relx=0.5, rely=0.252, relwidth=0.6, relheight=0.74, anchor='n')
            
        def edit():
            win_screen = tk.Frame(window, bg= '#cccc99', bd=5)
            win_screen.place(relx=0.5, rely=0.252, relwidth=0.6, relheight=0.74, anchor='n')
            def edit1():
                def save1():
                    new_firstname=str(edit_first_name1.get())
                    if len(new_firstname) > 0 :
                        conn = sqlite3.connect(r"D:\\Anurakbodin_python\\guitest.db")
                        c = conn.cursor()
                        data = (str(new_firstname),no)
                        c.execute('''UPDATE room SET first_name =? WHERE No = ?''',data)
                        data = no,
                        c.execute('select first_name FROM room WHERE No = ?',data)
                        result = c.fetchall()
                        for x in result:
                            Label(window,text = x, bg='#ff66ff').place(relx=0.6, rely=0.4, relwidth=0.2, relheight=0.05, anchor='n')
                        conn.commit()
                        conn.close()
                        clear()
                        win_screen = tk.Frame(window, bg= '#cccc99', bd=5)
                        win_screen.place(relx=0.774, rely=0.4, relwidth=0.05, relheight=0.047, anchor='n')
                    else:
                        messagebox.showinfo("Incompleted","Please enter your first name")
                def back1():
                    conn = sqlite3.connect(r"D:\\Anurakbodin_python\\guitest.db")
                    c = conn.cursor()
                    data = no,
                    c.execute('select first_name FROM room WHERE No = ?',data)
                    result = c.fetchall()
                    for x in result:
                        Label(window,text = x, bg='#ff66ff').place(relx=0.6, rely=0.4, relwidth=0.2, relheight=0.05, anchor='n')
                    win_screen = tk.Frame(window, bg= '#cccc99', bd=5)
                    win_screen.place(relx=0.774, rely=0.4, relwidth=0.05, relheight=0.047, anchor='n') 
                    Button(window,text = "EDIT",command = edit1, bg='#999999').place(relx=0.724, rely=0.4, relwidth=0.05, relheight=0.047, anchor='n')
                    clear()
                Entry(window, textvariable= edit_first_name1, validate='key', vcmd=Ll).place(relx=0.6, rely=0.4, relwidth=0.2, relheight=0.05, anchor='n')
                Button(window,text = "Back",command = back1, bg='#999999').place(relx=0.774, rely=0.4, relwidth=0.05, relheight=0.047, anchor='n')
                Button(window,text = "SAVE",command = save1, bg='#999999').place(relx=0.724, rely=0.4, relwidth=0.05, relheight=0.047, anchor='n')
            def edit2():
                def save2():
                    new_lastname=str(edit_last_name1.get())
                    if len(new_lastname) > 0 :
                        conn = sqlite3.connect(r"D:\\Anurakbodin_python\\guitest.db")
                        c = conn.cursor()
                        data = (str(new_lastname),no)
                        c.execute('''UPDATE room SET last_name =? WHERE No = ?''',data)
                        data = no,
                        c.execute('select last_name FROM room WHERE No = ?',data)
                        result = c.fetchall()
                        for x in result:
                            Label(window,text = x, bg='#ff99ff').place(relx=0.6, rely=0.45, relwidth=0.2, relheight=0.05, anchor='n')
                        conn.commit()
                        conn.close()
                        clear()
                        win_screen = tk.Frame(window, bg= '#cccc99', bd=5)
                        win_screen.place(relx=0.774, rely=0.45, relwidth=0.05, relheight=0.047, anchor='n') 
                    else:
                        messagebox.showinfo("Incompleted","Please enter your last name")
                def back2():
                    conn = sqlite3.connect(r"D:\\Anurakbodin_python\\guitest.db")
                    c = conn.cursor()
                    data = no,
                    c.execute('select last_name FROM room WHERE No = ?',data)
                    result = c.fetchall()
                    for x in result:
                        Label(window,text = x, bg='#ff99ff').place(relx=0.6, rely=0.45, relwidth=0.2, relheight=0.05, anchor='n')
                    win_screen = tk.Frame(window, bg= '#cccc99', bd=5)
                    win_screen.place(relx=0.774, rely=0.45, relwidth=0.05, relheight=0.047, anchor='n') 
                    Button(window,text = "EDIT",command = edit2, bg='#999999').place(relx=0.724, rely=0.45, relwidth=0.05, relheight=0.047, anchor='n')
                    clear()
                Entry(window, textvariable= edit_last_name1, validate='key', vcmd=Ll).place(relx=0.6, rely=0.45, relwidth=0.2, relheight=0.05, anchor='n')
                Button(window,text = "Back",command = back2, bg='#999999').place(relx=0.774, rely=0.45, relwidth=0.05, relheight=0.047, anchor='n')
                Button(window,text = "SAVE",command = save2, bg='#999999').place(relx=0.724, rely=0.45, relwidth=0.05, relheight=0.047, anchor='n')
            def edit3():
                def save3():
                    new_tel=str(edit_tel1.get())
                    if len(new_tel) == 10:
                        conn = sqlite3.connect(r"D:\\Anurakbodin_python\\guitest.db")
                        c = conn.cursor()
                        data = (str(new_lastname),no)
                        c.execute('''UPDATE room SET tel =? WHERE No = ?''',data)
                        data = no,
                        c.execute('select tel FROM room WHERE No = ?',data)
                        result = c.fetchall()
                        for x in result:
                            Label(window,text = x, bg='#ff00ff').place(relx=0.6, rely=0.5, relwidth=0.2, relheight=0.05, anchor='n')
                        conn.commit()
                        conn.close()
                        clear()
                        win_screen = tk.Frame(window, bg= '#cccc99', bd=5)
                        win_screen.place(relx=0.774, rely=0.5, relwidth=0.05, relheight=0.047, anchor='n') 
                    else:
                        messagebox.showinfo("Incompleted","Please enter a valid phone number.")
                def back3():
                    conn = sqlite3.connect(r"D:\\Anurakbodin_python\\guitest.db")
                    c = conn.cursor()
                    data = no,
                    c.execute('select tel FROM room WHERE No = ?',data)
                    result = c.fetchall()
                    for x in result:
                        Label(window,text = x, bg='#ff00ff').place(relx=0.6, rely=0.5, relwidth=0.2, relheight=0.05, anchor='n')
                    win_screen = tk.Frame(window, bg= '#cccc99', bd=5)
                    win_screen.place(relx=0.774, rely=0.5, relwidth=0.05, relheight=0.047, anchor='n')  
                    Button(window,text = "EDIT",command = edit3, bg='#999999').place(relx=0.724, rely=0.5, relwidth=0.05, relheight=0.047, anchor='n')
                    clear()
                Entry(window, textvariable= edit_tel1, validate='key', vcmd=Nn).place(relx=0.6, rely=0.5, relwidth=0.2, relheight=0.05, anchor='n')
                Button(window,text = "Back",command = back3, bg='#999999').place(relx=0.774, rely=0.5, relwidth=0.05, relheight=0.047, anchor='n')
                Button(window,text = "SAVE",command = save3, bg='#999999').place(relx=0.724, rely=0.5, relwidth=0.05, relheight=0.047, anchor='n')

            Label(window,text = ("No-",no), bg= '#fff000').place(relx=0.5, rely=0.3, relwidth=0.2, relheight=0.1, anchor='n')
            Label(window,text = "First Name ->", bg= '#66ccff').place(relx=0.4, rely=0.4, relwidth=0.2, relheight=0.05, anchor='n')
            Label(window,text = "Last Name ->", bg= '#99ccff').place(relx=0.4, rely=0.45, relwidth=0.2, relheight=0.05, anchor='n')
            Label(window,text = "Tel", bg= '#3399ff').place(relx=0.4, rely=0.5, relwidth=0.2, relheight=0.05, anchor='n')

            conn = sqlite3.connect(r"D:\\Anurakbodin_python\\guitest.db")
            c = conn.cursor()
            data = no,
            c.execute('select first_name FROM room WHERE No = ?',data)
            result = c.fetchall()
            for x in result:
                Label(window,text = x, bg='#ff66ff').place(relx=0.6, rely=0.4, relwidth=0.2, relheight=0.05, anchor='n')
            data = no,
            c.execute('select last_name FROM room WHERE No = ?',data)
            result = c.fetchall()
            for x in result:
                Label(window,text = x, bg='#ff99ff').place(relx=0.6, rely=0.45, relwidth=0.2, relheight=0.05, anchor='n')
            data = no,
            c.execute('select tel FROM room WHERE No = ?',data)
            result = c.fetchall()
            for x in result:
                Label(window,text = x, bg='#ff00ff').place(relx=0.6, rely=0.5, relwidth=0.2, relheight=0.05, anchor='n')

            Button(window,text = "EDIT",command = edit1, bg='#999999').place(relx=0.724, rely=0.4, relwidth=0.05, relheight=0.047, anchor='n')
            Button(window,text = "EDIT",command = edit2, bg='#999999').place(relx=0.724, rely=0.45, relwidth=0.05, relheight=0.047, anchor='n')
            Button(window,text = "EDIT",command = edit3, bg='#999999').place(relx=0.724, rely=0.5, relwidth=0.05, relheight=0.047, anchor='n')

            Button(window,text = "BACK",command = lambda: onClick2(no), bg='#999999').place(relx=0.5, rely=0.8, relwidth=0.1, relheight=0.1, anchor='n')
        
        Label(window,text = ("No-",no), bg= '#fff000').place(relx=0.5, rely=0.3, relwidth=0.2, relheight=0.1, anchor='n')
        Label(window,text = "Category ->", bg= '#3399ff').place(relx=0.4, rely=0.4, relwidth=0.2, relheight=0.05, anchor='n')
        Label(window,text = "Availability ->", bg= '#66ccff').place(relx=0.4, rely=0.45, relwidth=0.2, relheight=0.05, anchor='n')
        Label(window,text = "Name ->", bg= '#99ccff').place(relx=0.4, rely=0.5, relwidth=0.2, relheight=0.05, anchor='n')
        Label(window,text = "Tel", bg= '#3399ff').place(relx=0.4, rely=0.55, relwidth=0.2, relheight=0.05, anchor='n')
        Label(window,text = "First Day", bg= '#66ccff').place(relx=0.4, rely=0.60, relwidth=0.2, relheight=0.05, anchor='n')
        Label(window,text = "Last Day", bg= '#99ccff').place(relx=0.4, rely=0.65, relwidth=0.2, relheight=0.05, anchor='n')
        Label(window,text = "Total", bg= '#3399ff').place(relx=0.4, rely=0.7, relwidth=0.2, relheight=0.05, anchor='n')

        conn = sqlite3.connect(r"D:\\Anurakbodin_python\\guitest.db")
        c = conn.cursor()
        data = no,
        c.execute('select category FROM room WHERE No = ?',data)
        result = c.fetchall()
        for x in result:
            Label(window,text = x, bg='#ff00ff').place(relx=0.6, rely=0.4, relwidth=0.2, relheight=0.05, anchor='n')
        data = no,
        c.execute('select availability FROM room WHERE No = ?',data)
        result = c.fetchall()
        for x in result:
            avail = str(x).strip("(',)")
            Label(window,text = x, bg='#ff66ff').place(relx=0.6, rely=0.45, relwidth=0.2, relheight=0.05, anchor='n')
        data = no,
        c.execute('select first_name FROM room WHERE No = ?',data)
        result = c.fetchall()
        for x in result:
            firstn = str(x).strip("(',)")
        data = no,
        c.execute('select last_name FROM room WHERE No = ?',data)
        result = c.fetchall()
        for x in result:
            lastn = str(x).strip("(',)")
        if len(firstn) == 1:
            name = "-"
        else :
            name = (str(firstn),"_",str(lastn))
        Label(window,text = name, bg='#ff99ff').place(relx=0.6, rely=0.5, relwidth=0.2, relheight=0.05, anchor='n')

        data = no,
        c.execute('select tel FROM room WHERE No = ?',data)
        result = c.fetchall()
        for x in result:
            Label(window,text = x, bg='#ff00ff').place(relx=0.6, rely=0.55, relwidth=0.2, relheight=0.05, anchor='n')
        data = no,
        c.execute('select first_day FROM room WHERE No = ?',data)
        result = c.fetchall()
        for x in result:
            Label(window,text = x, bg='#ff66ff').place(relx=0.6, rely=0.6, relwidth=0.2, relheight=0.05, anchor='n')
        data = no,
        c.execute('select last_day FROM room WHERE No = ?',data)
        result = c.fetchall()
        for x in result:
            Label(window,text = x, bg='#ff99ff').place(relx=0.6, rely=0.65, relwidth=0.2, relheight=0.05, anchor='n')
        data = no,
        c.execute('select total FROM room WHERE No = ?',data)
        result = c.fetchall()
        for x in result:
            Label(window,text = x, bg='#ff00ff').place(relx=0.6, rely=0.7, relwidth=0.2, relheight=0.05, anchor='n')

        if avail == "Busy":
            Button(window,text = "EDIT",command = edit, bg='#999999').place(relx=0.7, rely=0.8, relwidth=0.05, relheight=0.05, anchor='n')
        Button(window,text = "BACK",command = show, bg='#999999').place(relx=0.5, rely=0.8, relwidth=0.1, relheight=0.1, anchor='n')

    def back_edit():
        clear()
        show()
    
    conn = sqlite3.connect(r"D:\\Anurakbodin_python\\guitest.db")
    c = conn.cursor()
    data = 1,
    c.execute('select availability FROM room WHERE No = ?',data)
    result = c.fetchall()
    for x in result:
        ava = str(x).strip("(',)")
    if ava == "Free" :
        Button(window,text = 1,command=lambda: onClick2(1), bg='#00ff00').place(relx=0.28, rely=0.3, relwidth=0.1, relheight=0.2, anchor='n')
    else:
        Button(window,text = 1,command=lambda: onClick2(1), bg='#cc3333').place(relx=0.28, rely=0.3, relwidth=0.1, relheight=0.2, anchor='n')

    data = 2,
    c.execute('select availability FROM room WHERE No = ?',data)
    result = c.fetchall()
    for x in result:
        ava = str(x).strip("(',)")
    if ava == "Free" :
        Button(window,text = 2,command=lambda: onClick2(2), bg='#00ff00').place(relx=0.39, rely=0.3, relwidth=0.1, relheight=0.2, anchor='n')
    else:
        Button(window,text = 2,command=lambda: onClick2(2), bg='#cc3333').place(relx=0.39, rely=0.3, relwidth=0.1, relheight=0.2, anchor='n')

    data = 3,
    c.execute('select availability FROM room WHERE No = ?',data)
    result = c.fetchall()
    for x in result:
        ava = str(x).strip("(',)")
    if ava == "Free" :
        Button(window,text = 3,command=lambda: onClick2(3), bg='#00ff00').place(relx=0.5, rely=0.3, relwidth=0.1, relheight=0.2, anchor='n')
    else:
        Button(window,text = 3,command=lambda: onClick2(3), bg='#cc3333').place(relx=0.5, rely=0.3, relwidth=0.1, relheight=0.2, anchor='n')

    data = 4,
    c.execute('select availability FROM room WHERE No = ?',data)
    result = c.fetchall()
    for x in result:
        ava = str(x).strip("(',)")
    if ava == "Free" :
        Button(window,text = 4,command=lambda: onClick2(4), bg='#00ff00').place(relx=0.61, rely=0.3, relwidth=0.1, relheight=0.2, anchor='n')
    else:
        Button(window,text = 4,command=lambda: onClick2(4), bg='#cc3333').place(relx=0.61, rely=0.3, relwidth=0.1, relheight=0.2, anchor='n')

    data = 5,
    c.execute('select availability FROM room WHERE No = ?',data)
    result = c.fetchall()
    for x in result:
        ava = str(x).strip("(',)")
    if ava == "Free" :
        Button(window,text = 5,command=lambda: onClick2(5), bg='#00ff00').place(relx=0.72, rely=0.3, relwidth=0.1, relheight=0.2, anchor='n')
    else:
        Button(window,text = 5,command=lambda: onClick2(5), bg='#cc3333').place(relx=0.72, rely=0.3, relwidth=0.1, relheight=0.2, anchor='n')

    data = 6,
    c.execute('select availability FROM room WHERE No = ?',data)
    result = c.fetchall()
    for x in result:
        ava = str(x).strip("(',)")
    if ava == "Free" :
        Button(window,text = 6,command=lambda: onClick2(6), bg='#00ff00').place(relx=0.28, rely=0.51, relwidth=0.1, relheight=0.2, anchor='n')
    else:
        Button(window,text = 6,command=lambda: onClick2(6), bg='#cc3333').place(relx=0.28, rely=0.51, relwidth=0.1, relheight=0.2, anchor='n')

    data = 7,
    c.execute('select availability FROM room WHERE No = ?',data)
    result = c.fetchall()
    for x in result:
        ava = str(x).strip("(',)")
    if ava == "Free" :
        Button(window,text = 7,command=lambda: onClick2(7), bg='#00ff00').place(relx=0.39, rely=0.51, relwidth=0.1, relheight=0.2, anchor='n')
    else:
        Button(window,text = 7,command=lambda: onClick2(7), bg='#cc3333').place(relx=0.39, rely=0.51, relwidth=0.1, relheight=0.2, anchor='n')

    data = 8,
    c.execute('select availability FROM room WHERE No = ?',data)
    result = c.fetchall()
    for x in result:
        ava = str(x).strip("(',)")
    if ava == "Free" :
        Button(window,text = 8,command=lambda: onClick2(8), bg='#00ff00').place(relx=0.5, rely=0.51, relwidth=0.1, relheight=0.2, anchor='n')
    else:
        Button(window,text = 8,command=lambda: onClick2(8), bg='#cc3333').place(relx=0.5, rely=0.51, relwidth=0.1, relheight=0.2, anchor='n')

    data = 9,
    c.execute('select availability FROM room WHERE No = ?',data)
    result = c.fetchall()
    for x in result:
        ava = str(x).strip("(',)")
    if ava == "Free" :
        Button(window,text = 9,command=lambda: onClick2(9), bg='#00ff00').place(relx=0.61, rely=0.51, relwidth=0.1, relheight=0.2, anchor='n')
    else:
        Button(window,text = 9,command=lambda: onClick2(9), bg='#cc3333').place(relx=0.61, rely=0.51, relwidth=0.1, relheight=0.2, anchor='n')
    
    data = 10,
    c.execute('select availability FROM room WHERE No = ?',data)
    result = c.fetchall()
    for x in result:
        ava = str(x).strip("(',)")
    if ava == "Free" :
        Button(window,text = 10,command=lambda: onClick2(10), bg='#00ff00').place(relx=0.72, rely=0.51, relwidth=0.1, relheight=0.2, anchor='n')
    else:
        Button(window,text = 10,command=lambda: onClick2(10), bg='#cc3333').place(relx=0.72, rely=0.51, relwidth=0.1, relheight=0.2, anchor='n')

    Label(window,text = "Green is Free room", bg='#00ff00').place(relx=0.38, rely=0.75, relwidth=0.3, relheight=0.1, anchor='n')
    Label(window,text = "Red is Busy room", bg='#cc3333').place(relx=0.63, rely=0.75, relwidth=0.28, relheight=0.1, anchor='n')
    Button(window, text='BACK',command = login_com, bg='#00ccff', fg='#000000').place(relx=0.5, rely=0.88, relwidth=0.3, relheight=0.1, anchor='n')
########################

def cancelbooking():
    win_screen = tk.Frame(window, bg= '#cccc99', bd=5)
    win_screen.place(relx=0.5, rely=0.252, relwidth=0.6, relheight=0.74, anchor='n')
    frame = tk.Frame(window, bg='#3366ff')
    frame.place(relx = 0.5, rely=0.29, relwidth=0.55, relheight=0.6, anchor='n')
    frame = tk.Frame(window, bg='#00ccff')
    frame.place(relx = 0.5, rely=0.295, relwidth=0.545, relheight=0.42, anchor='n')

    def onClick(no):
        win_screen = tk.Frame(window, bg= '#cccc99', bd=5)
        win_screen.place(relx=0.5, rely=0.252, relwidth=0.6, relheight=0.74, anchor='n')
        frame = tk.Frame(window, bg='#ff9966')
        frame.place(relx = 0.5, rely=0.29, relwidth=0.5, relheight=0.7, anchor='n')
        Label(window,text = ("No-",no), bg= '#fff000').place(relx=0.5, rely=0.3, relwidth=0.2, relheight=0.1, anchor='n')
        Label(window,text = "First Name ->", bg= '#0066ff').place(relx=0.4, rely=0.42, relwidth=0.2, relheight=0.1, anchor='n')
        Label(window,text = "Last Name ->", bg= '#3399ff').place(relx=0.4, rely=0.52, relwidth=0.2, relheight=0.1, anchor='n')
        Label(window,text = "Tel ->", bg= '#66ccff').place(relx=0.4, rely=0.62, relwidth=0.2, relheight=0.1, anchor='n')
        Label(window,text = "Total ->", bg= '#99ccff').place(relx=0.4, rely=0.72, relwidth=0.2, relheight=0.1, anchor='n')
        def cancel_book() :
            win_screen = tk.Frame(window, bg= '#cccc99', bd=5)
            win_screen.place(relx=0.5, rely=0.252, relwidth=0.6, relheight=0.74, anchor='n')
            frame = tk.Frame(window, bg='#ff9966')
            frame.place(relx = 0.5, rely=0.38, relwidth=0.5, relheight=0.4, anchor='n')
            def comfirm_cancel_book():
                conn = sqlite3.connect(r"D:\\Anurakbodin_python\\guitest.db")
                c = conn.cursor()
                try:
                    data = ("Free","-","-","-",0,0,0,0,no)
                    c.execute('UPDATE room set availability =?,first_name=?,last_name=?,tel=?,first_day=?,last_day=?,day=?,total=? WHERE No =?',data)
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
            data = no,
            c.execute('select total FROM room WHERE No = ?',data)
            result = c.fetchall()
            for x in result:
                total = x[0]
            servicecharge = total*10/100
            Label(window,text = "If you cancel booking, 10 percent of the total rental price will be charged.", bg='#66ccff').place(relx=0.5, rely=0.4, relwidth=0.45, relheight=0.1, anchor='n')
            Label(window,text = ("Total=",servicecharge), bg='#66ccff').place(relx=0.5, rely=0.5, relwidth=0.45, relheight=0.1, anchor='n')
            Button(window,text = "ENTER",command = comfirm_cancel_book, bg='#999999').place(relx=0.4, rely=0.65, relwidth=0.1, relheight=0.1, anchor='n')
            Button(window,text = "BACK",command =lambda: onClick(no), bg='#999999').place(relx=0.6, rely=0.65, relwidth=0.1, relheight=0.1, anchor='n')
        conn = sqlite3.connect(r"D:\\Anurakbodin_python\\guitest.db")
        c = conn.cursor()
        data = no,
        c.execute('select first_name FROM room WHERE No = ?',data)
        result = c.fetchall()
        for x in result:
            Label(window,text = x, bg='#ff0099').place(relx=0.6, rely=0.42, relwidth=0.2, relheight=0.1, anchor='n')
        data = no,
        c.execute('select last_name FROM room WHERE No = ?',data)
        result = c.fetchall()
        for x in result:
            Label(window,text = x, bg='#ff00ff').place(relx=0.6, rely=0.52, relwidth=0.2, relheight=0.1, anchor='n')
        data = no,
        c.execute('select tel FROM room WHERE No = ?',data)
        result = c.fetchall()
        for x in result:
            Label(window,text = x, bg='#ff66ff').place(relx=0.6, rely=0.62, relwidth=0.2, relheight=0.1, anchor='n')
        data = no,
        c.execute('select total FROM room WHERE No = ?',data)
        result = c.fetchall()
        for x in result:
            Label(window,text = x, bg='#ff99ff').place(relx=0.6, rely=0.72, relwidth=0.2, relheight=0.1, anchor='n')
        Button(window,text = "Cancel Booking",command = cancel_book, bg='#999999').place(relx=0.4, rely=0.85, relwidth=0.1, relheight=0.1, anchor='n')
        Button(window,text = "BACK",command = back_cancelbook, bg='#999999').place(relx=0.6, rely=0.85, relwidth=0.1, relheight=0.1, anchor='n')
    def back_cancelbook():
        clear()
        cancelbooking()

    conn = sqlite3.connect(r"D:\\Anurakbodin_python\\guitest.db")
    c = conn.cursor()
    data = 1,
    c.execute('select availability FROM room WHERE No = ?',data)
    result = c.fetchall()
    for x in result:
        ava = str(x).strip("(',)")
    if ava == "Free" :
        Label(window,text = 1, bg='#00ff00').place(relx=0.28, rely=0.3, relwidth=0.1, relheight=0.2, anchor='n')
    else:
        Button(text = 1,command=lambda: onClick(1), bg='#cc3333').place(relx=0.28, rely=0.3, relwidth=0.1, relheight=0.2, anchor='n')

    data = 2,
    c.execute('select availability FROM room WHERE No = ?',data)
    result = c.fetchall()
    for x in result:
        ava = str(x).strip("(',)")
    if ava == "Free" :
        Label(window,text = 2, bg='#00ff00').place(relx=0.39, rely=0.3, relwidth=0.1, relheight=0.2, anchor='n')
    else:
        Button(text = 2,command=lambda: onClick(2), bg='#cc3333').place(relx=0.39, rely=0.3, relwidth=0.1, relheight=0.2, anchor='n')

    data = 3,
    c.execute('select availability FROM room WHERE No = ?',data)
    result = c.fetchall()
    for x in result:
        ava = str(x).strip("(',)")
    if ava == "Free" :
        Label(window,text = 3, bg='#00ff00').place(relx=0.5, rely=0.3, relwidth=0.1, relheight=0.2, anchor='n')
    else:
        Button(text = 3,command=lambda: onClick(3), bg='#cc3333').place(relx=0.5, rely=0.3, relwidth=0.1, relheight=0.2, anchor='n')

    data = 4,
    c.execute('select availability FROM room WHERE No = ?',data)
    result = c.fetchall()
    for x in result:
        ava = str(x).strip("(',)")
    if ava == "Free" :
        Label(window,text = 4, bg='#00ff00').place(relx=0.61, rely=0.3, relwidth=0.1, relheight=0.2, anchor='n')
    else:
        Button(text = 4,command=lambda: onClick(4), bg='#cc3333').place(relx=0.61, rely=0.3, relwidth=0.1, relheight=0.2, anchor='n')

    data = 5,
    c.execute('select availability FROM room WHERE No = ?',data)
    result = c.fetchall()
    for x in result:
        ava = str(x).strip("(',)")
    if ava == "Free" :
        Label(window,text = 5, bg='#00ff00').place(relx=0.72, rely=0.3, relwidth=0.1, relheight=0.2, anchor='n')
    else:
        Button(text = 5,command=lambda: onClick(5), bg='#cc3333').place(relx=0.72, rely=0.3, relwidth=0.1, relheight=0.2, anchor='n')

    data = 6,
    c.execute('select availability FROM room WHERE No = ?',data)
    result = c.fetchall()
    for x in result:
        ava = str(x).strip("(',)")
    if ava == "Free" :
        Label(window,text = 6, bg='#00ff00').place(relx=0.28, rely=0.51, relwidth=0.1, relheight=0.2, anchor='n')
    else:
        Button(text = 6,command=lambda: onClick(6), bg='#cc3333').place(relx=0.28, rely=0.51, relwidth=0.1, relheight=0.2, anchor='n')

    data = 7,
    c.execute('select availability FROM room WHERE No = ?',data)
    result = c.fetchall()
    for x in result:
        ava = str(x).strip("(',)")
    if ava == "Free" :
        Label(window,text = 7, bg='#00ff00').place(relx=0.39, rely=0.51, relwidth=0.1, relheight=0.2, anchor='n')
    else:
        Button(text = 7,command=lambda: onClick(7), bg='#cc3333').place(relx=0.39, rely=0.51, relwidth=0.1, relheight=0.2, anchor='n')

    data = 8,
    c.execute('select availability FROM room WHERE No = ?',data)
    result = c.fetchall()
    for x in result:
        ava = str(x).strip("(',)")
    if ava == "Free" :
        Label(window,text = 8, bg='#00ff00').place(relx=0.5, rely=0.51, relwidth=0.1, relheight=0.2, anchor='n')
    else:
        Button(text = 8,command=lambda: onClick(8), bg='#cc3333').place(relx=0.5, rely=0.51, relwidth=0.1, relheight=0.2, anchor='n')

    data = 9,
    c.execute('select availability FROM room WHERE No = ?',data)
    result = c.fetchall()
    for x in result:
        ava = str(x).strip("(',)")
    if ava == "Free" :
        Label(window,text = 9, bg='#00ff00').place(relx=0.61, rely=0.51, relwidth=0.1, relheight=0.2, anchor='n')
    else:
        Button(text = 9,command=lambda: onClick(9), bg='#cc3333').place(relx=0.61, rely=0.51, relwidth=0.1, relheight=0.2, anchor='n')

    data = 10,
    c.execute('select availability FROM room WHERE No = ?',data)
    result = c.fetchall()
    for x in result:
        ava = str(x).strip("(',)")
    if ava == "Free" :
        Label(window,text = 10, bg='#00ff00').place(relx=0.72, rely=0.51, relwidth=0.1, relheight=0.2, anchor='n')
    else:
        Button(text = 10,command=lambda: onClick(10), bg='#cc3333').place(relx=0.72, rely=0.51, relwidth=0.1, relheight=0.2, anchor='n')

    Label(window,text = "Menu Cancel BOOKING", bg='#ff9999').place(relx=0.34, rely=0.75, relwidth=0.17, relheight=0.1, anchor='n')
    Label(window,text = "Select Red Room", bg='#cc3333').place(relx=0.65, rely=0.75, relwidth=0.13, relheight=0.1, anchor='n')
    Button(window,text = "BACK",command=login_com, bg='#ffcc99').place(relx=0.5, rely=0.75, relwidth=0.1, relheight=0.1, anchor='n')
#######################

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

    edit_first_name1.set("")
    edit_last_name1.set("")
    edit_tel1.set("")
    new_firstname = ""
    new_lastname = ""
    new_tel = ""
########################
fn = StringVar()
ln = StringVar()
tel = StringVar()
fd = StringVar()
nd = StringVar()
today = ""

edit_first_name1= StringVar()
edit_last_name1= StringVar()
edit_tel1= StringVar()

user = StringVar()
pass_w = StringVar()
con = StringVar()
re_user = StringVar()
re_pass_w = StringVar()
re_con = StringVar()
base()
