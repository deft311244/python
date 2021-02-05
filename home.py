n =int(input("Please enter student: "))
print("--------------------------")
i=0
a1 =[]
a2 =[]
a3 =[]
a4 =[]
a5 =[]
a6 =[]
while(i<n):
    z = int(input('Please enter score : '))
    if z>=90 :
        a1.append(z)
    elif z>=80 :
        a2.append(z)
    elif z>=70 :
        a3.append(z)
    elif z>=60 :
        a4.append(z)
    elif z>=50 :
        a5.append(z)
    elif z>=0 :
        a6.append(z)
    i = i+1
print("90-100: ",len(a1)*"*")
print("80-89: ",len(a2)*"*")
print("70-79: ",len(a3)*"*")
print("60-69: ",len(a4)*"*")
print("50-59: ",len(a5)*"*")
print(" 0-49: ",len(a6)*"*")

