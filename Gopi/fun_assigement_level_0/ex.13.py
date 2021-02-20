#13.wap to read temerture in centigrade and display a suitable message
#according to tempature state a below
def cal_temp(temp):
    if temp<0:
        v="freezing weather"
    elif temp>=0 and temp<10:
        v="very cold weather"
    elif temp>=10 and temp<20:
        v="cold weather"
    elif temp>=20 and temp<30:
        v="normal in temp"
    elif temp>=30 and temp<40:
        v="its hot"
    elif temp>40:
        v="it is very hot"
    return  v
temp=int(input("entera temp:"))
a=cal_temp(temp)
print(a)


