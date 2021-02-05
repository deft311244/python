#โปรแกรมร้านค้าออนไลน์

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