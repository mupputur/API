#16.write a program to acept a coordinate point xy coordinate system and
#determine in which quadrant the coordinate point less.
def quardinate(x,y):
    if x>0 and y>0:
        v="1st quardinate"
    elif x<0 and y>0:
        v="2nd quardinate"
    elif x<0 and y<0:
        v="3rd quardinate"
    elif x>0 and y<0:
        v="4th quardinate"
    else:
        v="point is on the origin"
    return v
x=int(input("enter the first value:"))
y=int(input("enter the second value:"))
a=quardinate(x,y)
print(a)
