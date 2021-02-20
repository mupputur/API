#17.wap to check whether a triangel is equilateral ,isosceles,or scalene
def check_triangles(a,b,c,t):
    if a==b==c and t==180 :
        return("EQUILATERAL TRAIANGLE")
    elif a!=b!=c and t==180:
        return("SCALENE TRIANGLE")
    elif a==b or b==c or c==a and t==180:
        return("ISOCELES TRIANGLE")
    else:
        return("triangle is not formed")
        
a=int(input("enter the a value"))
b=int(input("enter the b value"))
c=int(input("enter the c value"))
t=a+b+c
a=check_triangles(a,b,c,t)
print(a)

    

