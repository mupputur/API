#6.wap to read the given of an interger m and display the value of nis 1 when
#m is larger 0,0 when m is 0 and -1 when m is less than 0

def value(m):
    if m>0:
        return("n value is 1 ")
    elif m==0:
        return("n value is 0")
    elif m<0:
        return("n value is -1")
x=int(input("enter a m values :"))
a=value(x)
print(a)
