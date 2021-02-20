#9.wap to find the largest of three numbers
def largest_of_three_num(x,y,z):
    if x>y and x>z:
        return("x is the largest number")
    elif y>z and y>x:
        return("y is the largest number")
    elif z>x and z>y:
        return("z is the largest number")
num1=int(input("enter a number:"))
num2=int(input("enter anumber:"))
num3=int(input("enter a number:"))
a=largest_of_three_num(num1,num2,num3)
print(a)
