#4.wap to find a given year is a leap year or not
def leap_year(x):
    if x%4==0 or x%400==0 or x%100==0:
        return("this {} is leap year".format(x))#string dot formating
    else:
        return("this {} is not a leap year".format(x))
x=int(input("enter a year:"))
x=leap_year(x)
print(x)

        
    
