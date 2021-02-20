#24.wap which is a menu-driven program to compute the area of the various geomentrical
#
def menu_driven_geomentrical_shapes(x):
    if x==1:
        length=int(input("enter a length:"))
        width=int(input("enter a width:"))
        rect=length*width
        v=areaofrectangle 

    elif x==2:
        r=int(input("entr a radius:"))
        a=3.14*(r**2)
        v=areaofcircle 
    
    elif x==3:
        base=int(input("enter  a base :"))
        height=int(input("ente a height:"))
        area=0.5*base*height
        v=area
    else:
        v="please enter a number valid number"
    return v

m=int(input("enter a number:"))
a=menu_driven_geomentrical_shapes(m)
print(a)

