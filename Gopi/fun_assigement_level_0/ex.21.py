#21.wap to read any day number in interger and dsiplay the number of day for month
def day_num(num):
    if num==1:
        v =" this weekday is monday "
    elif num==2:
        v=" this weekday is thrusday "
    elif num==3:
        v=" this weekday is wensday "
    elif num==4:
        v=" this weekday is thrusday "
    elif num==5:
        v="this weekday is friday "
    elif num==6:
        v("this weekday is saturday ")
    elif num==7:
        v("this weekday is sunday ")
    else:
        v("no the day ")
    return v
day=int(input("enter a day number:"))
a=day_num(day)
print(a)   
     
