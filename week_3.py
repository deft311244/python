#โปรแกรมเปิดโปรแกรม
'''
import os
choice = 0
filename = ''

def menu():
    global choice
    print('Menu\n 1.Open Calculator\n 2.Open Notepad\n 3.Exit')
    choice = input('Select Menu :')

def opennotepad():
    filename = 'C:\\Windows\\system32\\notepad.exe'
    print('Memorandum writting %s' %filename)
    os.system(filename)

def opencalculator():
    filename = 'C:\\Windows\\System32\\calc.exe'
    print('Calculate Number %s' %filename)
    os.system(filename)

while True:
    menu()
    if choice == '1':
        opencalculator()
    elif choice == '2':
        opennotepad()
    else:
        break
'''
#Function
'''
def Select(x,y,z): #การประกาศฟังชัน #ชื่อฟังชัน #ตัวแปรที่จะรีเทิร์น
    statement 1
    .
    statement 2
    return result
'''

#โปรแกรมร้านค้าออนไลน์
'''
choice = 0
it = [0,0,0,0,0]
i=1

def menu():
    global choice
    print('\n           โปรแกรมร้านค้าออนไลน์ \n ----------------------------------')
    print('1.แสดงรายการสินค้า\n2.หยิบสินค้าเข้าตะกร้า\n3.แสดงรายจำนวนและราคาของสินค้าที่หยิบ\n4.หยิบสินค้าออกจากตะกร้า\n5.ปิดโปรแกรม')
    choice = input('กรุณาเลือกทำรายการ ')

def item():
    print('\n   รายการสินค้า\n---------------- \n1.ยาดม ราคา 15 บาท \n2.นํ้าเปล่า ราคา 10 บาท \n3.มาม่า ราคา 20 บาท \n4.สบู่ ราคา 30 บาท \n5.แปลงสีฟัน ราคา 25 บาท \n')

def positive():
    print('\n   รายการสินค้า\n---------------- \n1.ยาดม \n2.นํ้าเปล่า \n3.มาม่า \n4.สบู่ \n5.แปลงสีฟัน \n6.ยกเลิกการทำรายการ \n')
    while(i>0):
        ab =(int(input("เลือกหยิบสินค้าหมายเลข :")))
        if ab == 1:
            it[0] += 1
        elif ab == 2:
            it[1] += 1
        elif ab == 3:
            it[2] += 1
        elif ab == 4:
            it[3] += 1
        elif ab == 5:
            it[4] += 1
        elif ab == 6:
            break

def show():
    sum1= it[0]+it[1]+it[2]+it[3]+it[4]
    sum2= it[0]*15+it[1]*10+it[2]*20+it[3]*30+it[4]*25
    print('\n_______สินค้าที่คุณได้หยิบไปมีดังนี้__________')
    print('สินค้า.......จำนวน.........ราคา.........')
    print('ยาดม.......',it[0],'.........',it[0]*15,"..........")
    print('นํ้าเปล่า......',it[1],'.........',it[1]*10,"........")
    print('มาม่า.......',it[2],'.........',it[2]*20,".........")
    print('สบู่.........',it[3],'.........',it[3]*30,".........")
    print('แปลงสีฟัน...',it[4],'.........',it[4]*25,"...........")
    print("_______________________________________")
    print('รวม.......',sum1,'.........',sum2,"...........")

def delete():
    print('\n   รายการสินค้า\n---------------- \n1.ยาดม \n2.นํ้าเปล่า \n3.มาม่า \n4.สบู่ \n5.แปลงสีฟัน \n')
    while(i>0):
        ba =(int(input("เลือกสินค้าที่จะหยิบออก หรือพิมพ์ -1 เพื่อออก:")))
        if ba == 1:
            it[0] -= 1
        elif ba == 2:
            it[1] -= 1
        elif ba == 3:
            it[2] -= 1
        elif ba == 4:
            it[3] -= 1
        elif ba == 5:
            it[4] -= 1
        elif ba == -1:
            break

while True:
    menu()
    if choice == '1':
        item()
    elif choice == '2':
        positive()
    elif choice == '3':
        show()
    elif choice == '4':
        delete()
    else:
        o =str(input("ต้องการออกจากโปรแกรมใช่หรือไม่ (y/n) :"))
        if o == "y":
            print("ออกจากโปรแกรมเรียบร้อยแล้ว")
            break
        else:
            print("กลับเข้าสู่โปรแกรม")
'''

#keyword arguments function ตัวอย่าง
'''
def Introduce(arg1,argg2 = "com",are3 = 'ed',arg4='kku'):
    print('Hello,I am'+arg1+','+arg2+','+arg3+','+arg4+)

Introduce("Python")
Introduce(arg1="Python")
Introduce(arg1="Python",arg3="Sci")
Introduce("Python",arg4="CMU")


'''
#dictionary 5 work4.2  
'''
dictionary = []
pra = []
kum = []

def menu():
    global choice
    print('พจนานุกรม\n1) เพิ่มคำศัพท์\n2) แสดงคำศัพท์\n3) ลบคำศัพท์\n4) ออกจากโปรแกรม')
    choice = input('Input Choice: ')

def puss():
    dictionary.insert(0,input("เพิ่มคำศัพท์ "))
    pra.insert(0,input("ชนิดคำศัพท์ (n. ,v. ,adj. ,adv. :) "))
    kum.insert(0,input("ความหมาย "))
    print("เพิ่มคำศัพท์เรียบร้อยแล้ว")
def show():
    print('---------------------\nคำศัพท์มีทั้งหมด ',len(dictionary),"\n---------------------")
    print('คำศัพท์ ประเภท ความหมาย')
    x = 0
    while x < len(dictionary) :
        print(dictionary[x],' ',pra[x]," ",kum[x])
        x = x+1

def delete():
    x =str(input("พิมพ์คำศัพท์ที่ต้องการลบ: "))
    if x == dictionary[0]:
        del pra[0]
        del kum[0]
    elif x == dictionary[1]:
        del pra[1]
        del kum[1]
    elif x == dictionary[2]:
        del pra[2]
        del kum[2]
    elif x == dictionary[3]:
        del pra[3]
        del kum[3]
    elif x == dictionary[4]:
        del pra[4]
        del kum[4]
    dictionary.remove(x)

while True:
    menu()
    if choice == '1':
        puss()
    elif choice == '2':
        show()
    elif choice == '3':
        delete()
    else:
        break
'''



#dictionary work4.2  ใช้loop ตรง delete
'''
dictionary = []
pra = []
kum = []
i = 1
def menu():
    global choice
    print('พจนานุกรม\n1) เพิ่มคำศัพท์\n2) แสดงคำศัพท์\n3) ลบคำศัพท์\n4) ออกจากโปรแกรม')
    choice = input('Input Choice: ')

def puss():
    dictionary.insert(0,input("เพิ่มคำศัพท์ "))
    pra.insert(0,input("ชนิดคำศัพท์ (n. ,v. ,adj. ,adv. :) "))
    kum.insert(0,input("ความหมาย "))
    print("เพิ่มคำศัพท์เรียบร้อยแล้ว")
def show():
    print('---------------------\nคำศัพท์มีทั้งหมด ',len(dictionary),"\n---------------------")
    print('คำศัพท์ ประเภท ความหมาย')
    x = 0
    while x < len(dictionary) :
        print(dictionary[x],' ',pra[x]," ",kum[x])
        x = x+1

def delete():
    x =str(input("พิมพ์คำศัพท์ที่ต้องการลบ: "))
    z=0
    i=1
    while z < len(dictionary):
        if x == dictionary[z]:
            del pra[z]
            del kum[z]
        z = z+1
    dictionary.remove(x)

while True:
    menu()
    if choice == '1':
        puss()
    elif choice == '2':
        show()
    elif choice == '3':
        delete()
    else:
        break
'''