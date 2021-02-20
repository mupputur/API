#15.wap to read the rool no ,namae,and marks of three subjects and calculate
#the total,percentage and division
def grade(per):
    if per>=60:
        v="the student division frist claas"
    elif per<60 and per >=48:
        v="the student division second class"
    elif per<48 and per>=36:
        v="the student division is pass"
    elif per<36:
        v="the student division is fail"
    return v
        
roll_no=int(input("enter a roll num:"))
name=input("enter a name:")
sub1=int(input("enter a marks of subject1:"))
sub2=int(input("enter a marks of subject2:"))
sub3=int(input("enter a marks of subject3:"))
total=sub1+sub2+sub3
per=total/3
a=grade(per)
print(a)  
                



