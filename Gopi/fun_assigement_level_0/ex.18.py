#18.wap to check whether a triangel cn be formed ny given value for the angel
def triangle(x,y,z,a):
    if tri==180:
        return("it is a triangle")
    else:
        return("it is not a triangle")
        
a1=int(input("enter a values:"))
a2=int(input("enter a values:"))
a3=int(input("enter a values:"))
tri=a1+a2+a3
a=triangle(a1,a2,a3,tri)
print(a)
