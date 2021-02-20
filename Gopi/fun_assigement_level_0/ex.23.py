#23.wap to program in c which is a menu-driven program to perform
#a simple calculation
def menu_drive(x):
    if x==1:
        a=int(input("enter a number:"))
        b=int(input("enter a number:"))
        addition=a+b
        v="addition two number is {}".format(addition)

    elif x==2:
        a=int(input("enter a number:"))
        b=int(input("enter a number:"))
        substraction=a-b
        v="substraction two number is {}".format(substraction)
    elif x==3:
        a=int(input("enter a number:"))
        b=int(input("enter a number:"))
        multiplication=a*b
        v="multiplication two number is {}".format(multiplication)
    elif x==4:
        a=int(input("enter a number:"))
        b=int(input("enter a number:"))
        division=a//b
        v="division two number is {}".format(division)
    else:
        v="enter a valid mumber"
    return v
        
m=int(input("enter a menu_drive number:"))
a=menu_drive(m)
print(a)



