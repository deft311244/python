#5.1
class nisit : 
    def __init__(self,name,id,sax,year,subject,province,school) : 
        self.name = name      
        self.id = id                               
        self.sax = sax                            
        self.year = year            
        self.subject = subject                   
        self.province = province                   
        self.school = school  

    def shownisit(self) :  
        print("-------เเนะนำตัว---------")
        print("ชื่อ-นามสกุล :",self.name)
        print("รหัสนักศึกษา :",self.id)
        print("เพศ :",self.sax)
        print("ชั้นปีการศึกษา :",self.year)
        print("คณะ,สาขาวิชา:",self.subject)
        print("จังหวัด :",self.province)
        print("โรงเรียนเดิม :",self.school)

x = nisit("อนุรักษ์บดินทร์ พิทักษ์","633050349-7","ชาย","ปี 1","คอมพิวเตอร์ศึกษา","มหาสารคาม","โรงเรียนพยัคฆภูมิวิทยาคาร")
x.shownisit()

#5.2
def menu():
    global choice
    print("\n","*"*10,"ร้านค้า","*"*10)
    print('แสดงรายการสินค้า [s]\nเพิ่มรายการสินค้า [a]\nออกจากระบบ [x]\n')
    choice = input('กรุณาเลือกคำสั่ง : ')
name = []
mon = []
def show():
    class shop:
        def __init__(self,name1,money1,name2,money2,name3,money3,name4,money4) :
            self.name1 = name1
            self.money1 = money1
            self.name2 = name2
            self.money2 = money2
            self.name3 = name3
            self.money3 = money3
            self.name4 = name4
            self.money4 = money4
        def shows(self) :
            print("รายการสินค้ามีดังนี้\n")
            print("1.",self.name1,self.money1,"บาท")
            print("2.",self.name2,self.money2,"บาท")
            print("3.",self.name3,self.money3,"บาท")
            print("4.",self.name4,self.money4,"บาท")
            n = 5
            m = 0
            while m < len(name) :
                print(n,".",name[m]," ",mon[m],"บาท")
                m = m+1
                n = n+1
            print("\n")
    x = shop("มาม่า","12","ลาบ","60","ส้มตำ","40","ข้าวแกง","25")
    x.shows()

def add():
    class puss:
        while 1>0 :
            q = str(input("\nเพิ่มรายการสินค้าหากต้องการยกเลิก กรอก exit \nเพิ่มชื่อสินค้า "))
            if q == "exit" :
                print("\n")
                break
            w = input("เพิ่มราคาของ "+q+" :")
            name.append(q)
            mon.append(w)
            print("เพิ่มรายการเสร็จสิ้น")
            e = input("ต้องการเพิ่มสินค้าอีกหรือไม่ (y/n):")
            if e == "n":
                break

while True:
    menu()
    if choice == 's':
        show()
    elif choice == 'a':
        add()
    elif choice == 'x':
        o =str(input("ต้องการออกจากโปรแกรมใช่หรือไม่ (y/n) :"))
        if o == "y":
            print("ออกจากโปรแกรมเรียบร้อยแล้ว")
            break
        else:
            print("กลับเข้าสู่โปรแกรม")