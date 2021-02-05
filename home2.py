n =int(input("Please enter student: "))
print("--------------------------")
i=0
a=b=c=d=e=f=0
while(i<n):
    z = int(input('Please enter score : '))
    if z>=90 :
        a = a+1
    elif z>=80 :
        b = b+1
    elif z>=70 :
        c = c+1
    elif z>=60 :
        d = d+1
    elif z>=50 :
        e = e+1
    elif z>=0 :
        f = f+1
    i = i+1
print("90-100: ","*"*int(a))
print("80-89: ","*"*int(b))
print("70-79: ","*"*int(c))
print("60-69: ","*"*int(d))
print("50-59: ","*"*int(e))
print(" 0-49: ","*"*int(f))

