#1.wap to acept two integers and check whether they are equal or not
def equal_or_not(x,y):
    if x==y:
        return ("this number is equal ")
    else:
        return ("this number isnot equal")
x=int(input("enter a number:"))
y=int(input("enter a number:"))
a=equal_or_not(x,y)
print(a)

