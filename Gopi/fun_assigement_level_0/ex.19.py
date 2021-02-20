#19.wap to calculate and point the electricity bill of a given customes the
#custmore id.name and unit consumed by the user should  be taken from keyboard
#and dsiplay the total amount tp pay the customer .the charge is as below

def current_bill(x,y,z):
    if unit<=199:
        v=unit*1.20
        return("consumed charge",v)
    elif unit>=200 and unit<=400:
        v=(unit-199)*1.50+199*1.20
        return("consumed charged", v)
    elif unit>400 and unit<=600:
        v=(unit-400)*1.80+201*1.50+199*1.20
        return("consumed charged ",v)
    elif unit>600:
        v=(unit-600)*2.00+200*1.80+201*1.50+199*1.20
        return("consumed charged:",v)
    else:
        return("invalid input")
        
id=int(input("enter a id:"))
name=input("enter a name:")
unit=int(input("enter a consumed unit:"))
a=current_bill(id,name,unit)
print(a)
        

