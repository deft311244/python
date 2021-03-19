"""
import sqlite3
conn = sqlite3.connect(r"D:\\Anurakbodin_python\\guitest.db")
c = conn.cursor()
c.execute ('''CREATE TABLE user (No integer PRIMARY KEY AUTOINCREMENT,
    username varchar(30) NOT NULL,
    password varchar(30) NOT NULL,
    wallet integer(30) NOT NULL)''')
c.execute ('''CREATE TABLE room (No integer PRIMARY KEY AUTOINCREMENT,
    category varchar(30) NOT NULL,
    cost integer(30) NOT NULL,
    availability varchar(30) NOT NULL,
    name varchar(30) NOT NULL)''')
conn.commit()
conn.close()

def insertTousers (username,password,wallet) :
    try :
        conn = sqlite3.connect(r"D:\\Anurakbodin_python\\guitest.db")
        c = conn.cursor()

        sql = '''INSERT INTO user (username,password,wallet) VALUES (?,?,?)'''
        data = (username,password,wallet)
        c.execute(sql,data)
        conn.commit()
        c.close()
    except sqlite3.Error as e:
        print('Failed to insert : ',e)
    finally :
        if conn :
            conn.close()
insertTousers("anurak","1234","500")
insertTousers("temakorn","5678","1000")

def insertTousers (category,cost,availability,name) :
    try :
        conn = sqlite3.connect(r"D:\\Anurakbodin_python\\guitest.db")
        c = conn.cursor()

        sql = '''INSERT INTO room (category,cost,availability,name) VALUES (?,?,?,?)'''
        data = (category,cost,availability,name)
        c.execute(sql,data)
        conn.commit()
        c.close()
    except sqlite3.Error as e:
        print('Failed to insert : ',e)
    finally :

        if conn :
            conn.close()
insertTousers("normal","500","Free","")
insertTousers("normal","500","Busy","David")
insertTousers("normal","500","Free","")
insertTousers("normal","500","Free","")
insertTousers("normal","500","Busy","Joey")
insertTousers("special","1000","Busy","Mark")
insertTousers("special","1000","Busy","Addie")
insertTousers("special","1000","Free","")
insertTousers("special","1000","Free","")
insertTousers("special","1000","Free","")
"""

from tkinter import * 
from tkinter import messagebox
from tkinter.ttk import *
import sqlite3
Menu = Tk()
Menu.geometry("210x200")
Menu.title('Menu')
Menu.iconbitmap('D:\Anurakbodin_python\ico\list.ico')

def login():
    login = Toplevel(Menu)
    login.geometry("250x200")
    login.title("Login")
    login.iconbitmap('D:\Anurakbodin_python\ico\login.ico')
    ##########################################################################

    user = StringVar()
    pass_w = StringVar()

    Label(login,text=("="*10,"-"*4)).grid(row=0, column=0)
    Label(login,text=('         Login        ')).grid(row=1, column=0)
    Label(login,text=("-"*4,"="*10)).grid(row=2, column=0)

    Label(login, text="Username : ").grid(row=3, column=0)
    Entry(login, textvariable=user).grid(row=3, column=1)
    Label(login, text="Password : ").grid(row=4, column=0)
    Entry(login, textvariable=pass_w).grid(row=4, column=1)
    
    def submit_login():
        user_name = str(user.get())
        pass_word = str(pass_w.get())

        nologin = 0
        try :
            conn = sqlite3.connect(r"D:\\Anurakbodin_python\\guitest.db")
            c = conn.cursor()
            data = (user_name,pass_word)
            c.execute('select No FROM user WHERE username =? and password =?',data)
            result = c.fetchall()
            for x in result:
                nologin = x[0] #ให้ตัวแปรมีค่าเท่ากับตัวที่อยู่ในตาราง ตามเงื่อนไข
            conn.commit()
            conn.close()
        except sqlite3.Error as e:
            print('Failed to insert : ',e)
        finally :
            if conn :
                conn.close()
        if nologin > 0 :
            Menu.withdraw()
            login.destroy()
            messagebox.showinfo("Success","Login Success.")
            #login แล้ว
            Menu2 = Toplevel(Menu)
            Menu2.geometry("260x240")
            Menu2.title('Menu (LOG IN)')
            Menu2.iconbitmap('D:\Anurakbodin_python\ico\list.ico')
            
            def profile():
                profile = Toplevel(Menu2)
                profile.geometry("210x230")
                profile.title("Profile")
                profile.iconbitmap('D:\Anurakbodin_python\ico\\profile.ico')
                Label(profile,text=("="*25)).pack(side=TOP)
                Label(profile,text=("--- Profile ---")).pack(side=TOP) 
                Label(profile,text=("="*25)).pack(side=TOP) 

                Label(profile,text=("="*15)).pack(side=TOP) 
                Label(profile,text=("USERNAME--WALLET")).pack(side=TOP)
                Label(profile,text=("="*15)).pack(side=TOP)

                conn = sqlite3.connect(r"D:\\Anurakbodin_python\\guitest.db")
                c = conn.cursor()
                data = user_name,
                c.execute('SELECT username,wallet FROM user WHERE username =?',data)

                result = c.fetchall()
                for x in result :
                    Label(profile,text=(x)).pack(side=TOP)

                def top_up():
                    topup = Toplevel(profile)
                    topup.geometry("300x200")
                    topup.title("Top up")
                    topup.iconbitmap('D:\Anurakbodin_python\ico\\money.ico')

                    conn = sqlite3.connect(r"D:\\Anurakbodin_python\\guitest.db")
                    c = conn.cursor()
                    data = user_name,
                    c.execute('select wallet FROM user WHERE username = ?',data)
                    result = c.fetchall()
                    for x in result:
                        oldmoney = x[0] #ให้ตัวแปรมีค่าเท่ากับตัวที่อยู่ในตาราง ตามเงื่อนไข

                    def up():
                        newmoney = int(nt.get()) 

                        conn = sqlite3.connect(r"D:\\Anurakbodin_python\\guitest.db")
                        c = conn.cursor()
                        try:
                            sum = int(newmoney) + int(oldmoney)
                            data = (sum,user_name)
                            c.execute('UPDATE user set wallet =? WHERE username =?',data)
                            conn.commit()
                            conn.close()
                            
                        except sqlite3.Error as e:
                            print('Failed to insert : ',e)
                        finally :
                            if conn :
                                conn.close()
                        messagebox.showinfo("Success","Top Up Success.")

                    t = Label(topup, text ='Top Up', font = "100")  
                    t.pack()
                    Label(topup, text ='(500 - 10,000)', font = "50") 
                    
                    nt = Spinbox(topup, from_= 500, to = 10000) 
                    nt.pack()

                    Button(topup, width=15, text="ENTER", command= up).pack(side=TOP )
                    Button(topup, width=15, text="Back", command= topup.destroy).pack(side=TOP )
                    topup.mainloop()  

                def newpassword():
                    newpass = Toplevel(profile)
                    newpass.geometry("300x160")
                    newpass.iconbitmap('D:\Anurakbodin_python\ico\\new.ico')
                    newpass.title("Change password")
                    cs = StringVar()
                    ns = StringVar()
                    def newpass2():
                        conpass = str(cs.get())
                        newpass = str(ns.get())
                        if conpass == oldpass :
                            conn = sqlite3.connect(r"D:\\Anurakbodin_python\\hotel.db")
                            c = conn.cursor()
                            data =(newpass,user_name,conpass)
                            c.execute('Update user Set password =? where username =? and password=?',data)
                            conn.commit ()
                            c.close()
                            messagebox.showinfo("Complete","Password changed successfully.")
                            newpass.destroy()

                        else :
                            messagebox.showinfo("Incomplete","Invalid password.")


                    conn = sqlite3.connect(r"D:\\Anurakbodin_python\\guitest.db")
                    c = conn.cursor()
                    data = user_name,
                    c.execute('select password FROM user WHERE username = ?',data)
                    result = c.fetchall()
                    for x in result:
                        oldpass = str(x).strip("(',)") #ให้ตัวแปรมีค่าเท่ากับตัวที่อยู่ในตาราง ตามเงื่อนไข
                    Label(newpass, text="Reset password").grid(row=1, column=0)
                    Label(newpass, text="="*20).grid(row=2, column=0)
                    Label(newpass, text="Confirm your password : ").grid(row=3, column=0)
                    Entry(newpass, textvariable=cs).grid(row=3, column=1)
                    Label(newpass, text="New password : ").grid(row=4, column=0)
                    Entry(newpass, textvariable=ns).grid(row=4, column=1)
                    Button(newpass, text = "ENTER",width=15,command = newpass2).grid(row=5, column=0)
                    Button(newpass, text = "CANCEL",width=15,command = newpass.destroy).grid(row=6, column=0)

                Label(profile,text=("="*15)).pack(side=TOP)
                B1 = Button(profile, text = "Top up (+)",width=15,command = top_up).pack(anchor=CENTER)
                B2 = Button(profile, text = "Change password",width=15,command = newpassword).pack(anchor=CENTER)
                B3 = Button(profile, text = "Back",width=15,command = profile.destroy).pack(anchor=CENTER)

                profile.mainloop()
    ##########################################################################          
            def book_room():
                book = Toplevel(Menu2)
                book.geometry("270x300")
                book.title("Booking")
                book.iconbitmap('D:\Anurakbodin_python\ico\\booking.ico')
                Label(book, text=("="*30)).pack(side=TOP)
                Label(book, text="No--category--availability").pack(side=TOP)
                Label(book, text=("="*30)).pack(side=TOP)

                conn = sqlite3.connect(r"D:\\Anurakbodin_python\\guitest.db")
                c = conn.cursor()
                c.execute('SELECT No,category,availability FROM room WHERE availability = "Free" ')
                result = c.fetchall()
                for x in result :
                    Label(book, text=(x)).pack(side=TOP)
                Label(book, text=("-"*30)).pack(side=TOP)
    ##########################################################################
                def normal():
                    book.withdraw()
                    normal = Toplevel(book)
                    normal.geometry("270x250")
                    normal.title("Normal Room")
                    normal.iconbitmap('D:\Anurakbodin_python\ico\\booking.ico')

                    Label(normal, text=("="*30)).pack(side=TOP)
                    Label(normal, text="No--category--availability").pack(side=TOP)
                    Label(normal, text=("="*30)).pack(side=TOP)
                    conn = sqlite3.connect(r"D:\\Anurakbodin_python\\guitest.db")
                    c = conn.cursor()
                    c.execute('SELECT No,category,availability FROM room WHERE category = "normal" and availability = "Free" ')
                    result = c.fetchall()
                    for x in result :
                        Label(normal, text=(x)).pack(side=TOP)
                    Label(normal, text=("-"*30)).pack(side=TOP)
                    def room_book():
                        no_room = int(nn.get())
                        conn = sqlite3.connect(r"D:\\Anurakbodin_python\\guitest.db")
                        c = conn.cursor()
                        data = no_room,
                        c.execute('select availability FROM room WHERE No =?',data)
                        result = c.fetchall()
                        for x in result :
                            avail_room = str(x).strip("(',)")
                        if avail_room == "Free":
                            normal.withdraw()
                            normal_book = Toplevel(normal)
                            normal_book.geometry("280x250")
                            normal_book.title("Normal Room Book")
                            na = StringVar()
                            day = IntVar()
                            Label(normal_book,text=("="*25)).pack(side=TOP)
                            Label(normal_book,text=("--- Booking room program ---")).pack(side=TOP)
                            Label(normal_book,text=("="*25)).pack(side=TOP)

                            Label(normal_book, text="Your Name : ").pack()
                            Entry(normal_book, textvariable=na).pack()  
                            Label(normal_book, text="How many nights do you want to book? : ").pack()
                            Entry(normal_book, textvariable=day).pack() 

                            def submit_nb():         
                                submit = Toplevel(normal_book)
                                submit.geometry("400x150")
                                submit.title("Confirm")
                                submit.iconbitmap('D:\Anurakbodin_python\ico\\ok.ico')
                                name_b = str(na.get())
                                day_book = int(day.get())
                                total = day_book*500 

                                def confirm_book():
                                    conn = sqlite3.connect(r"D:\\Anurakbodin_python\\guitest.db")
                                    c = conn.cursor()
                                    username = user_name,
                                    c.execute('select wallet FROM user WHERE username =?',username)
                                    result = c.fetchall()
                                    for x in result:
                                        money = x[0]
                                    conn.commit()
                                    conn.close()
                                    if money >= total : #ถ้าเงินพอ

                                        conn = sqlite3.connect(r"D:\\Anurakbodin_python\\guitest.db")
                                        c = conn.cursor()
                                        try:
                                            data = ("normal",int(total),"Busy",name_b,no_room)
                                            c.execute('''UPDATE room SET category =?,cost =?,availability =?,name =? WHERE No =?''',data)
                                            decrease = int(money) - int(total)
                                            data = (decrease,user_name)
                                            c.execute('UPDATE user SET wallet=? WHERE username=?',data)
                                            conn.commit()
                                            conn.close()
                                            
                                        except sqlite3.Error as e:
                                            print('Failed to insert : ',e)
                                        finally :
                                            if conn :
                                                conn.close()
                                        messagebox.showinfo("Completed",("Your wallet - ",total))
                                        book.deiconify()
                                        submit.destroy()

                                    elif money < total : #เงินไม่พอ
                                        messagebox.showinfo("Your money is not enough","Please top up and try again.")
                                        submit.deiconify()

                                Label(submit,text=("==Total==")).pack(side=TOP)
                                Label(submit,text=(total)).pack(side=TOP)
                                Label(submit,text=("If you cancel booking, 5 percent of the total rental price will be charged.")).pack(side=TOP)
                                Button(submit, width=15, text="ENTER", command= confirm_book).pack()
                                Button(submit, width=15, text="Cancel", command= submit.destroy).pack()                                       
                                submit.mainloop()

                            def back():
                                normal_book.destroy()
                                normal.deiconify()
                            Button(normal_book, width=15, text="ENTER", command= submit_nb).pack()
                            Button(normal_book, text = "Cancel",width=15,command = back).pack(anchor=CENTER) 

                            normal_book.mainloop()
                            
                        else:
                            messagebox.showinfo("The room is busy","Please select a Free room.")
                            normal.deiconify()
                            no_room = 0 

                    n = Label(normal, text ='Number Room')
                    n.pack()

                    nn = Spinbox(normal, from_= 1, to = 5)
                    nn.pack()
                    def back():
                        normal.destroy()
                        book.deiconify()
                    Button(normal, width=15, text="ENTER", command= room_book).pack(side=TOP )
                    Button(normal, text = "Cancel",width=15,command = back).pack(anchor=CENTER)
                    normal.mainloop()
    ##########################################################################  
                def special():

                    book.withdraw()
                    special = Toplevel(book)
                    special.geometry("270x250")
                    special.title("Special Room")
                    special.iconbitmap('D:\Anurakbodin_python\ico\\booking.ico')

                    Label(special, text=("="*30)).pack(side=TOP)
                    Label(special, text="No--category--availability").pack(side=TOP)
                    Label(special, text=("="*30)).pack(side=TOP)
                    conn = sqlite3.connect(r"D:\\Anurakbodin_python\\guitest.db")
                    c = conn.cursor()
                    c.execute('SELECT No,category,availability FROM room WHERE category = "special" and availability = "Free" ')
                    result = c.fetchall()
                    for x in result :
                        Label(special, text=(x)).pack(side=TOP)
                    Label(special, text=("-"*30)).pack(side=TOP)
                    def room_book():
                        no_room = int(ns.get())
                        conn = sqlite3.connect(r"D:\\Anurakbodin_python\\guitest.db")
                        c = conn.cursor()
                        data = no_room,
                        c.execute('select availability FROM room WHERE No =?',data)
                        result = c.fetchall()
                        for x in result :
                            avail_room = str(x).strip("(',)")
                        if avail_room == "Free":
                            special.withdraw()
                            special_book = Toplevel(special)
                            special_book.geometry("280x250")
                            special_book.title("Special Room Book")
                            na = StringVar()
                            day = IntVar()
                            Label(special_book,text=("="*25)).pack(side=TOP)
                            Label(special_book,text=("--- Booking room program ---")).pack(side=TOP)
                            Label(special_book,text=("="*25)).pack(side=TOP)

                            Label(special_book, text="Your Name : ").pack()
                            Entry(special_book, textvariable=na).pack()  
                            Label(special_book, text="How many nights do you want to book? : ").pack()
                            Entry(special_book, textvariable=day).pack() 

                            def submit_sb():         
                                submit = Toplevel(special_book)
                                submit.geometry("400x150")
                                submit.title("Confirm")
                                submit.iconbitmap('D:\Anurakbodin_python\ico\\ok.ico')
                                name_b = str(na.get())
                                day_book = int(day.get())
                                total = day_book*1000 

                                def confirm_book():
                                    conn = sqlite3.connect(r"D:\\Anurakbodin_python\\guitest.db")
                                    c = conn.cursor()
                                    username = user_name,
                                    c.execute('select wallet FROM user WHERE username =?',username)
                                    result = c.fetchall()
                                    for x in result:
                                        money = x[0]
                                    conn.commit()
                                    conn.close()
                                    if money >= total : #ถ้าเงินพอ

                                        conn = sqlite3.connect(r"D:\\Anurakbodin_python\\guitest.db")
                                        c = conn.cursor()
                                        try:
                                            data = ("special",int(total),"Busy",name_b,no_room)
                                            c.execute('''UPDATE room SET category =?,cost =?,availability =?,name =? WHERE No =?''',data)
                                            decrease = int(money) - int(total)
                                            data = (decrease,user_name)
                                            c.execute('UPDATE user SET wallet=? WHERE username=?',data)
                                            conn.commit()
                                            conn.close()
                                            
                                        except sqlite3.Error as e:
                                            print('Failed to insert : ',e)
                                        finally :
                                            if conn :
                                                conn.close()
                                        messagebox.showinfo("Completed",("Your wallet - ",total))
                                        book.deiconify()
                                        submit.destroy()

                                    elif money < total : #เงินไม่พอ
                                        messagebox.showinfo("Your money is not enough","Please top up and try again.")
                                        submit.deiconify()

                                Label(submit,text=("==Total==")).pack(side=TOP)
                                Label(submit,text=(total)).pack(side=TOP)
                                Label(submit,text=("If you cancel booking, 5 percent of the total rental price will be charged.")).pack(side=TOP)
                                Button(submit, width=15, text="ENTER", command= confirm_book).pack()
                                Button(submit, width=15, text="Cancel", command= submit.destroy).pack()                                       
                                submit.mainloop()

                            def back():
                                special_book.destroy()
                                special.deiconify()
                            Button(special_book, width=15, text="ENTER", command= submit_sb).pack()
                            Button(special_book, text = "Cancel",width=15,command = back).pack(anchor=CENTER) 

                            special_book.mainloop()
                            
                        else:
                            messagebox.showinfo("The room is busy","Please select a Free room.")
                            special.deiconify()
                            no_room = 0 

                    n = Label(special, text ='Number Room')
                    n.pack()

                    ns = Spinbox(special, from_= 6, to = 10)
                    ns.pack()
                    def back():
                        special.destroy()
                        book.deiconify()
                    Button(special, width=15, text="ENTER", command= room_book).pack(side=TOP )
                    Button(special, text = "Cancel",width=15,command = back).pack(anchor=CENTER)
                    special.mainloop()
    ##########################################################################                 
                C1 = Button(book, text = "Normal Room",width=15,command =normal).pack(anchor=CENTER)
                C2 = Button(book, text = "Special Room",width=15,command=special).pack(anchor=CENTER)
                C3 = Button(book, text = "Back",width=15,command = book.destroy).pack(anchor=CENTER)
                book.mainloop()
    ##########################################################################
            def show():
                show = Toplevel(Menu2)
                show.geometry("320x330")
                show.title("Show")
                show.iconbitmap('D:\Anurakbodin_python\ico\\room.ico')
                Label(show,text=("="*30)).pack(side=TOP)
                Label(show,text=("No--category--availability")).pack(side=TOP)
                Label(show,text=("="*30)).pack(side=TOP) 

                conn = sqlite3.connect(r"D:\\Anurakbodin_python\\guitest.db")
                c = conn.cursor()
                c.execute('SELECT No,category,availability FROM room')

                result = c.fetchall()
                for x in result :
                    Label(show,text=(x)).pack(side=TOP)
                Label(show,text=("-"*30)).pack(side=TOP)
                Button(show, text = "Back",width=15,command =show.destroy).pack(anchor=CENTER)
                show.mainloop()
    ##########################################################################
            def cancel_book():
                cancel = Toplevel(Menu2)
                cancel.geometry("380x350")
                cancel.title("Cancel Book")
                cancel.iconbitmap('D:\Anurakbodin_python\ico\\cancel.ico')
                Label(cancel,text=("="*11)).pack(side=TOP)
                Label(cancel,text=("Cancel Booking")).pack(side=TOP)
                Label(cancel,text=("="*11)).pack(side=TOP)
                Label(cancel,text=("="*30)).pack(side=TOP)
                Label(cancel,text=("No--category--availability")).pack(side=TOP)
                Label(cancel,text=("="*30)).pack(side=TOP)

                conn = sqlite3.connect(r"D:\\Anurakbodin_python\\guitest.db")
                c = conn.cursor()
                c.execute('SELECT No,category,availability FROM room WHERE availability = "Busy"')
                result = c.fetchall()
                for x in result :
                    Label(cancel,text=(x)).pack(side=TOP)
                Label(cancel,text=("-"*40)).pack(side=TOP)
                conn.commit()
                conn.close()
                def submit_cancel():
                    cancel_confirm = Toplevel(cancel)
                    cancel_confirm.geometry("380x350")
                    cancel_confirm.title("Confirm Cancel Book")
                    cancel_confirm.iconbitmap('D:\Anurakbodin_python\ico\\cancel.ico')
                    name = str(nam.get())
                    print(name)
                    conn = sqlite3.connect(r"D:\\Anurakbodin_python\\guitest.db")
                    c = conn.cursor()
                    nocancel = 0
                    try:
                        data = name,
                        c.execute('select No FROM room WHERE name=?',data)
                        result = c.fetchall()
                        for x in result:
                            nocancel = x[0] #ให้ตัวแปรมีค่าเท่ากับตัวที่อยู่ในตาราง ตามเงื่อนไข
                        conn.commit()
                        conn.close()
                    except sqlite3.Error as e:
                        print('Failed to insert : ',e)
                    finally :
                        if conn :
                            conn.close()
                    if nocancel > 0 :
                        Label(cancel_confirm,text=("="*30)).pack(side=TOP)
                        Label(cancel_confirm,text=("No--category--cost--availability--name")).pack(side=TOP)
                        Label(cancel_confirm,text=("="*30)).pack(side=TOP)

                        conn = sqlite3.connect(r"D:\\Anurakbodin_python\\guitest.db")
                        c = conn.cursor()
                        data = str(name),
                        c.execute('SELECT * FROM room WHERE name = ?',data)
                        result = c.fetchall()
                        for x in result :
                            Label(cancel_confirm,text=(x)).pack(side=TOP)
                        Label(cancel_confirm,text=("-"*30)).pack(side=TOP)
                        conn.commit()
                        conn.close()
                        def confirm():

                            conn = sqlite3.connect(r"D:\\Anurakbodin_python\\guitest.db")
                            c = conn.cursor()
                            try:
                                data = str(name),
                                c.execute('select cost FROM room WHERE name =?',data)
                                result = c.fetchall()
                                for x in result:
                                    oldcost = x[0] #ให้ตัวแปรมีค่าเท่ากับตัวที่อยู่ในตาราง ตามเงื่อนไข
                                servicecharge = oldcost*5/100
                                refund = oldcost - int(servicecharge)
                                data = int(refund),user_name,
                                c.execute('UPDATE user set wallet =? WHERE username=?',data)
                                data = ("",0,"Free",str(name))
                                c.execute('UPDATE room set name =?,cost =?,availability =? WHERE name =?',data)
                                conn.commit()
                                conn.close()

                            except sqlite3.Error as e:
                                print('Failed to insert : ',e)
                            finally :
                                if conn :
                                    conn.close()
                            messagebox.showinfo("Completed",("Your wallet + ",refund))
                            cancel.destroy
                        Label(cancel_confirm,text=("Confirm Cancel")).pack(side=TOP)
                        Button(cancel_confirm, width=15, text="Yes", command= confirm).pack()
                        Button(cancel_confirm, width=15, text="No", command= cancel_confirm.destroy).pack()

                    else:
                        Label(cancel_confirm,text=("Did not find your name on the booking")).pack(side=TOP)
                        Label(cancel_confirm,text=("Please try again")).pack(side=TOP)
                        Button(cancel_confirm, width=15, text="ENTER", command= cancel_confirm.destroy).pack()
                        
                    cancel_confirm.mainloop()
                nam = StringVar()
                Label(cancel,text=("If you cancel booking, 5 percent of the total rental price will be charged")).pack(side=TOP)
                Label(cancel, text="Please type your Name : ").pack(side=TOP)
                Entry(cancel, textvariable=nam).pack(side=TOP)
                Button(cancel, width=15, text="ENTER", command= submit_cancel).pack()  
                Button(cancel, width=15, text="Cancel", command= cancel.destroy).pack()

                cancel.mainloop()
    ##########################################################################
            def log_out():
                log_out = Toplevel(Menu2)
                log_out.geometry("220x100")
                log_out.iconbitmap('D:\Anurakbodin_python\ico\logout.ico')
                log_out.title("LOG OUT")
                def out():
                    messagebox.showinfo("Success","Log out Success.")
                    Menu2.destroy()
                    Menu.deiconify()

                Label(log_out,text=("--- Log Out ---")).pack(side=TOP)
                L1 = Button(log_out, text = "ENTER",width=15,command = out).pack(anchor=CENTER)
                L2 = Button(log_out, text = "Cancel",width=15,command = log_out.destroy).pack(anchor=CENTER)
                log_out.mainloop()
            ##### ปุ่มเมนูภายใน
            Label(Menu2,text=("="*25)).pack(side=TOP)
            Label(Menu2,text=("--- Hotel room reservation program ---")).pack(side=TOP) 
            Label(Menu2,text=("Log In Success")).pack(side=TOP)
            Label(Menu2,text=("="*25)).pack(side=TOP)   
            Label(Menu2,text=("--- Menu ---")).pack(side=TOP)
            M1 = Button(Menu2, text = "Profile",width=15,command = profile).pack(anchor=CENTER)
            M2 = Button(Menu2, text = "Booking room",width=15,command = book_room).pack(anchor=CENTER)
            M3 = Button(Menu2, text = "Show room",width=15,command = show).pack(anchor=CENTER)
            M4 = Button(Menu2, text = "Cancel booking",width=15,command = cancel_book).pack(anchor=CENTER)
            M5 = Button(Menu2, text = "Log out",width=15,command = log_out).pack(anchor=CENTER)
            Menu2.mainloop()

        else:
            messagebox.showinfo("Incorrect","Passwords is Incorrect.")
            user_name = ""
            pass_word = ""
    ##########################################################################
    def exit_login():
        exit_login = Toplevel(login)
        exit_login.geometry("200x100")
        exit_login.title("cancel register")
        exit_login.iconbitmap('D:\Anurakbodin_python\ico\logout.ico')
        Label(exit_login,text=("Cancel Login")).pack(side=TOP)
        exit_button = Button(exit_login, text="Yes", command= login.destroy).pack(side=TOP)
        cancel_button = Button(exit_login, text = "No",command = exit_login.destroy).pack(side=TOP)
        exit_login.mainloop()
    ##########################################################################
    Button(login, width=15, text="ENTER", command= submit_login).grid(row=6, column=0, columnspan=2, pady=10)   
    exit_button = Button(login, width=15, text="Cancel", command= exit_login).grid(row=7, column=0, columnspan=2, pady=0)

    login.mainloop()
##########################################################################
def register():
    regist = Toplevel(Menu)
    regist.geometry("250x210")
    regist.title("Register")
    regist.iconbitmap('D:\Anurakbodin_python\ico\\regist.ico')
    re_user = StringVar()
    re_pass = StringVar()
    re_conpass = StringVar()
    def submit_re():
        user_name2 = str(re_user.get())
        pass_word2 = str(re_pass.get())
        confirm_pass = str(re_conpass.get())

        conn = sqlite3.connect(r'D:\\Anurakbodin_python\\guitest.db')
        c = conn.cursor()
        try:
            noregis = 0
            data = user_name2,
            c.execute('select No FROM user WHERE username=?',data)
            result = c.fetchall()
            for x in result:
                noregis = x[0] #ให้ตัวแปรมีค่าเท่ากับตัวที่อยู่ในตาราง ตามเงื่อนไข
            conn.commit()
            conn.close()
        except sqlite3.Error as e:
            print('Failed to insert : ',e)
        finally :
            if conn :
                conn.close()
        if noregis == 0 : #ถ้า noregis = 0
            if confirm_pass == pass_word2:

                conn = sqlite3.connect(r'D:\\Anurakbodin_python\\guitest.db')
                c = conn.cursor()
                try:
                    data = (user_name2,pass_word2,0)
                    c.execute('insert into user (username,password,wallet) VALUES (?,?,?)',data)
                    conn.commit()
                    conn.close()   
                except sqlite3.Error as e:
                    print('Failed to insert : ',e)
                finally :
                    if conn :
                        conn.close()
                messagebox.showinfo("Completed","We have saved your information.")
                regist.destroy()
            else:
                messagebox.showinfo("Incorrect","Passwords do not match.")

        else: #ถ้า username ซํ้า ค่า noregis จะเปลี่ยนไป แล้วไม่เท่ากับ 0
            messagebox.showinfo("Username has already.","Please create a new username.")

    Label(regist,text=("="*10,"-"*4)).grid(row=0, column=0)
    Label(regist,text=('         Register        ')).grid(row=1, column=0)
    Label(regist,text=("-"*4,"="*10)).grid(row=2, column=0)

    Label(regist, text="Username : ").grid(row=3, column=0)
    Entry(regist, textvariable=re_user).grid(row=3, column=1)
    Label(regist, text="Password : ").grid(row=4, column=0)
    Entry(regist, textvariable=re_pass).grid(row=4, column=1)
    Label(regist, text="Confirm password : ").grid(row=5, column=0)
    Entry(regist, textvariable=re_conpass).grid(row=5, column=1)

    def exit_regist():
        exit_regist = Toplevel(regist)
        exit_regist.geometry("250x100")
        exit_regist.title("cancel register")
        exit_regist.iconbitmap('D:\Anurakbodin_python\ico\logout.ico')
        Label(exit_regist,text=("Cancel Register")).pack(side=TOP)
        exit_button = Button(exit_regist, text="Yes", command= regist.destroy).pack(side=TOP)
        cancel_button = Button(exit_regist, text = "No",command = exit_regist.destroy).pack(side=TOP)
        exit_regist.mainloop()

    Button(regist, width=15, text="ENTER", command= submit_re).grid(row=6, column=0, columnspan=2, pady=10, padx=5, ipadx=50)   
    exit_button = Button(regist, width=15, text="Cancel", command= exit_regist).grid(row=7, column=0, columnspan=2, pady=3, padx=10, ipadx=50)

    regist.mainloop()
##########################################################################
def show_detail():
    show = Toplevel(Menu)
    show.geometry("300x260")
    show.title("SHOW DETAILS")
    show.iconbitmap('D:\Anurakbodin_python\ico\\room.ico')
    Label(show,text=("="*25,"-"*15)).grid(row=0)
    Label(show,text=("Room details")).grid(row=1)
    Label(show,text=("-"*15,"="*25)).grid(row=2)
    Label(show,text=("We have 10 room")).grid(row=3)
    Label(show,text=("[Normal] 5 room. [Special] 5 rooms.")).grid(row=4)
    Label(show,text=("> Normal room [500 Bath/Night]")).grid(row=5)
    Label(show,text=("  It is a normal room. There are no special services.")).grid(row=6)
    Label(show,text=("> Special room [1000 Bath/Night]")).grid(row=7)
    Label(show,text=("  There will be a special service from the female staff.")).grid(row=8)
    Label(show,text=("  Such as oil massage etc.")).grid(row=9)
    Label(show,text=("-"*60)).grid(row=10)
    exit_button = Button(show, text="Back", command=show.destroy) 
    exit_button.grid(row=11)
    show.mainloop()
##########################################################################
def exitpro():
    exitpro = Toplevel(Menu)
    exitpro.geometry("200x100")
    exitpro.title("EXIT")
    exitpro.iconbitmap('D:\Anurakbodin_python\ico\logout.ico')
    Label(exitpro,text=("Exit the programe")).pack(side=TOP)
    exit_button = Button(exitpro, text="Yes", command= Menu.destroy).pack(side=TOP)
    cancel_button = Button(exitpro, text = "No",command = exitpro.destroy).pack(side=TOP)
    exitpro.mainloop()
##########################################################################
Label(Menu,text=("="*25)).pack(side=TOP)
Label(Menu,text=("--- Hotel room reservation program ---")).pack(side=TOP) 
Label(Menu,text=("="*25)).pack(side=TOP)   
Label(Menu,text=("--- Menu ---")).pack(side=TOP)
m1 = Button(Menu, text = "Login",command = login).pack(anchor=CENTER)
m2 = Button(Menu, text = "register",command = register).pack(anchor=CENTER)
m3 = Button(Menu, text = "showdetails",command = show_detail).pack(anchor=CENTER)
m4 = Button(Menu, text = "Exit",command = exitpro).pack(anchor=CENTER)
Menu.mainloop()
