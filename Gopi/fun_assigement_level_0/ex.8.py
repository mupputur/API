#8wap find the largest of two number
def largest_two_num(x,y):
    if x>y:
        return("x is the largest number")
    else:
        return("y is the largest number")
num1=int(input("enter a number:"))
num2=int(input("entrer a  number:"))
a=largest_two_num(num1,num2)
print(a)
