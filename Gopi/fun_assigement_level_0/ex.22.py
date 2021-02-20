#22.wap to read any month number in interger and dsiplay the number of day fro this month
def month(x):
    if x==1 or x==3 or x==5 or x==7 or x==8 or x==10 or x==12 :
        m="this month is 31 days "
    elif x==4 or x==6 or x==9 or x==11 :
        m="this month is 30 days"
    elif x==2:
        m="this moths is 28 or 29 day "
    else:
        m="invalid number"
    return m
m=int(input("enter a month number:"))
a=month(m)
print(a)
