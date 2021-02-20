#3.wap to check whether a given number is positive or negative
def pos_or_neg_num(x):
    if x>=0:
        return("this  {} number is positive number".format(x))
    else:
        return("this {} number is negative number".format(x))
x=int(input("enter a number:"))
a=pos_or_neg_num(x)
print(a)
