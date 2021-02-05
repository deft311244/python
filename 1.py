import time
name = []
pts = []
timees = []
factor = []
def times_():
    timeis = time.localtime()
    a = time.strftime("%d %B %Y, %H:%M:%S", timeis)
    print(a)
n = int(input("จำนวนผู้ซ้อมยิงปืน : "))
for i in range(n):
    print("ข้มูลคนที่ ",i+1)
    nam = input("ชื่อ : ")
    pt = float(input("คะแนน : "))
    tim = float(input("ระยะเวลา : "))
    name.append(nam)
    pts.append(pt)
    timees.append(tim)
    factor.append(pt/tim)
for i in range(n):
    j = i
    for j in range(n):
        if factor[i] > factor[j]:50
            a,b,c,d = factor[i],name[i],pts[i],timees[i]
            factor[i],name[i],pts[i],timees[i] = factor[j],name[j],pts[j],timees[j]
            factor[j],name[j],pts[j],timees[j] = a,b,c,d
timeis = time.localtime()
a = time.strftime("%A",timeis)
b = time.strftime("%Y",timeis)
print("Shotgun "+a+" Training",b," \nCondtion : 1")
print("-"*77)
print("{0:-<6}{1:-<6}{2:-<8}{3:-<17}{4:-<12}{5:-<15}{6}".format("NO.","PTS","TIME","COMETITOR#Name","HIT FACTOR","STATE POINTS","STATE PERCENT"))
print("-"*77)
times_()
for i in range(n):
    stawe_po = (factor[i]/factor[0])*50
    stawe_pe = (stawe_po/(factor[0]/factor[0]*50))*100
    print("{0:<6}{1:<6}{2:<8}{3:<17}{4:<12}{5:<15}{6}".format(i+1,int(pts[i]),"%.2f"%timees[i],name[i],"%.4f"%factor[i],"%.4f"%stawe_po,"%.2f"%stawe_pe))

