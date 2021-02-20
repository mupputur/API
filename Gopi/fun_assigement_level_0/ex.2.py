#2.wap to check whether a given number is even or odd
def even_or_odd_num(x):
    if x%2==0:
        return ("{} is even number".format(x))
    else:
        return("{} is odd number".format(x))
x=int(input("enter a number:"))
a=even_or_odd_num(x)
print(a)
