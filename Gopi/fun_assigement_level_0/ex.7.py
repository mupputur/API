#7.wap to acept the height of person in centimeter and catergorise the person accordingly
#to their geight.if th height is less then 150 display output ias "DWARF" and if the
#height is greaterthen equal to 150 and less then 165 display output as "AVERAGE HEIGHT"
#if the height gretaer than 165 display output as "TALL"

def height_of_person(x):
    if x<150:
        return("DWARF")
    elif x>=150 and x<165:
        return("AVERAGE HEIGHT")
    elif x>=165:
        return("TALL")
num=int(input("enter a person height:"))
a=height_of_person
(num)
print(a)
