#โปรแกรมรับค่าระยะทาง
"""
print("\nเลือกเมนูเพื่อทำรายการ \n#####################")
print("กด 1 เลือกเหมาจ่าย \nกด 2 เลือกจ่ายเพิ่ม")
m =int(input(""))
if m==1 :
    s1 =int(input("กรุณาบอกระยะทาง\n"))
    if s1 <= 25 :
        print("ค่าใช้จ่ายรวมทั้งหมด 25 บาท")
    else:
        print("ค่าใช้จ่ายรวมทั้งหมด 55 บาท")
elif m==2 :
    s2 =int(input("กรุณาบอกระยะทาง\n"))
    if s2 <= 25 :
        print("ค่าใช้จ่ายรวมทั้งหมด 25 บาท")
    else:
        print("ค่าใช้จ่ายรวมทั้งหมด 80 บาท")
"""
#Loopสูตรคูณ
"""
i = 1
z = 2
while(i<13):
    print(str(z)+"X"+str(i)+"="+str(z*i))
    i += 1
"""
#loopรวมค่าเลข
"""
n =int(input("\nกรุณากรอกจำนวนครั้งในการรับค่า\n"))
i=1
sum = 0
while(i<n+1):
    k =int(input("กรอกตัวเลข  "))
    i += 1
    sum = sum + k
print("ผลรวมค่าที่รับทั้งหมด = ",sum)
"""
#Control Statements !! break !!
"""
i = 1
z = 2
while(i<13):
    print(str(z)+"X"+str(i)+"="+str(z*i))
    if i == 5 :
        break
    i += 1
    """
#Control Statements !! continue !!
"""
i = 0
z = 2
while(i<12):
    i += 1
    if i == 5 :
        continue
    print(str(z)+"X"+str(i)+"="+str(z*i))
"""
#โปรแกรมวนรับชื่ออาหาร
"""
print("ป้อนชื่ออาหารสุดโปรดของคุณ หรือ exit เพื่อออกจากโปรแกรม ")
i=1
x=0
n=0
y=0
menu = []
while(i>0):
    a =(str(input("อาหารโปรดอันดับที่ "+str(i)+" ")))
    i = i+1
    y = y+1
    if a == "exit" :
        break
    menu.append(a)
print("อาหารสุดโปรดของคุณมีดังนี้")
while(x>=0):
    x = x+1
    print(str(x)+'.'+menu[0+n])
    n = n+1
    if x == y-1 :
        break
"""
a=[]
while True:
    b = input('---ร้านขายของออฟไลน์---\n เพิ่ม [a]\nแสดง [s]\n ออกจากระบบ [x]\n')
    b = b.lower()
    if b=='a':
        c = input('ป้อนรายการลูกค้า(รหัส:ชื่อ:จังหวัด)')
        a.append(c)
        print('\n****ข้อมูลได้เข้าสู่ระบบแล้ว****\n')
    elif b =='s':
        print('{0:-<30}'.format(""))
        print('{0:-<8}{1:-<10}{2:10}'.format("รหัส","ชื่อ","จังหวัด"))
        print('{0:-<6}{0:-<10}{0:-<10}'.format(""))
        for d in a:
            e = d.split(":")
            print('{0[0]:<6}{0[1]:<10}({0[2]:<10})'.format(e))
            continue
    elif b == 'x':
        break
print('คำสั่งทั่วไป')
    