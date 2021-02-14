
# ข้อความสีเขียวคือ text บอกตัวเองให้รู้ว่ามันคืออะไร

#โปรแกรม เปรียบเทียบ ค่าตัวเลข    
n1 = input("Input First Number:\n")
n2 = input("Input Second Number:\n")
print(n1,"=",n2,':',n1==n2)
print(n1,">",n2,':',n1>n2)
print(n1,"<",n2,':',n1<n2)

#ตัวอย่างผลลัพธ์
"""
Input First Number:
1
Input Second Number:
2
1 = 2 : False
1 > 2 : False
1 = 2 : True
"""

#โปรแกรมแปลง วัน เป็น ชม นาที วินาที
print("Day Converter Program")
d = input("Input number of Days -->\n")
a = int(d)
x = a*24
y = a*1440
z = a*86400
print(a,"Days -->","Hour",x,"Hours")
print(a,"Days -->","Minutes",y,"Minutes")
print(a,"Days -->","Seconds",z,"Seconds")



# list !!!!!!!!!!!!!!!!!!!!

#สมาชิกจะเริ่มตั้งแต่ 0 1 2 3 ...
#ตำแหน่งของสมาชิกจะเริ่มจาก [0,1,2,3,4,...]
friends = ["jan","cream","phu","bam","aom","pee","bas","kong","da","james"]
friends[9] ="may" #เปลี่ยนชื่อสมาชิก
friends[3] ="boat"
friends.append("dome") #เพิ่มสมาชิกต่อท้าย
friends.append("poondang")
friends.insert(1,"csa") #แทรกสมาชิกระหว่าง ไล่1ไป2 แล้วเพิ่มลง1แทน
friends.insert(8,"ped")
friends.remove("aom") #ลบสมาชิกโดย ระบุชื่อ
friends.pop() #ลบสมาชิกคน สุดท้าย ออกไป
friends.pop(3) #ลบสมาชิกโดยระบุตำแหน่ง

del friends[7] #ลบสมาชิกโดยระบุตำแหน่ง
del friends #ลบlist
friends.clear() #ล้างข้อมูลทั้งหมด

print(friends)
print(friends[3:8]) #แสดงช่วง
print(friends[-3]) #แสดงเฉพาะตำแหน่ง นับจากขวา เริ่มตั้งแต่ -1

#Ex
animal={"cat","dog","rat","pig","ant"}
animal.add("monkey")
animal.update(["python","capibara","spider","wombat","penguin","crocodie"])
print(animal)


#โปรแกรมหยิบสินค้าใส่ตะกร้า !!!!!!!!!!!!!!!!!!!!!!
#shop = ["สบู่","ยาสีฟัน","ลูกอม","นํ้าเปล่า","มาม่า"]
#โดยจะให้ผู้ใช้ พิมพ์ชื่อสินค้า เป็นข้อความ แล้วจัดเก็บบันทึกไว้ใน list
print("+++++++++++++++++++++++++++\n   โปรแกรมหยิบสินค้าใส่ตะกร้า   \n+++++++++++++++++++++++++++")
shop = [] # list shop
shop.append(input("หยิบสินค้าชิ้นที่ 1 \n")) #คือการเพิ่มสมาชิกเข้าไปใน list shop
shop.append(input("หยิบสินค้าชิ้นที่ 2 \n"))
shop.append(input("หยิบสินค้าชิ้นที่ 3 \n"))
shop.append(input("หยิบสินค้าชิ้นที่ 4 \n"))
shop.append(input("หยิบสินค้าชิ้นที่ 5 \n"))
print("สินค้าที่หยิบใส่ตะกร้ามีดังนี้")
print("1.",shop[0])
print("2.",shop[1])
print("3.",shop[2])
print("4.",shop[3])
print("5.",shop[4])



#โปรแกรมค่าผ่านทางรถ บนมอเตอร์เวย์ !!!!!!!!!!!!!!!!!!!!!!!!!!
car1 = ["25","30","45","55","60","80","100","105"] # list car1
car2 = ["45","45","75","90","100","130","160","170"] # list car2
car3 = ["60","70","110","130","140","190","235","245"] # list car3
print("------------------------------\n  โปรแกรมคำนวนค่าผ่านทางมอเตอร์เวย์  \n------------------------------")
print("รถยนต์ 4 ล้อ       กด 1")
print("รถยนต์ 6 ล้อ       กด 2")
print("รถยนต์มากกว่า 6 ล้อ กด 3")
c =int(input("\nเลือกประเภทยานพาหนะ :"))
if c == 1:                                          #ถ้า เลือก1 จะแสดงค่าผ่านทางของรถยนต์ 4 ล้อ
    print("\nค่าบริการรถยนต์ 4 ล้อ \n")
    print("ลาดกระบัง-->บางบ่อ.....",car1[0],"...บาท")
    print("ลาดกระบัง-->บางประกง..",car1[1],"...บาท")
    print("ลาดกระบัง-->พนัสนิคม....",car1[2],"...บาท")
    print("ลาดกระบัง-->บ้านบึง.....",car1[3],"...บาท")
    print("ลาดกระบัง-->บางพระ....",car1[4],"...บาท")
elif c == 2:                                        #ถ้า เลือก2 จะแสดงค่าผ่านทางของรถยนต์ 6 ล้อ
    print("\nค่าบริการรถยนต์ 6 ล้อ \n")
    print("ลาดกระบัง-->บางบ่อ.....",car2[0],"...บาท")
    print("ลาดกระบัง-->บางประกง..",car2[1],"...บาท")
    print("ลาดกระบัง-->พนัสนิคม....",car2[2],"...บาท")
    print("ลาดกระบัง-->บ้านบึง.....",car2[3],"...บาท")
    print("ลาดกระบัง-->บางพระ....",car2[4],"...บาท")
elif c == 3:                                        #ถ้า เลือก3 จะแสดงค่าผ่านทางของรถยนต์มากกว่า 6 ล้อ
    print("\nค่าบริการรถยนต์มากกว่า 6 ล้อ \n")
    print("ลาดกระบัง-->บางบ่อ.....",car3[0],"...บาท") #car3[0] คือ การแสดงข้อมูลที่อยู่ใน list car3 ตำแหน่งที่ 0
    print("ลาดกระบัง-->บางประกง..",car3[1],"...บาท")
    print("ลาดกระบัง-->พนัสนิคม....",car3[2],"...บาท")
    print("ลาดกระบัง-->บ้านบึง.....",car3[3],"...บาท")
    print("ลาดกระบัง-->บางพระ....",car3[4],"...บาท")
