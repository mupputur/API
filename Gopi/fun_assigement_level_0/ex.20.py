#20.wap to acept a grade and declare the equivalent description
def grades(grade):
    if grade=="E":
        value = "excellent"
    elif grade=="V":
        value ="very good"
    elif grade=="G":
        value ="good"
    elif grade=="A":
        value="avtg"
    elif grade=="F":
        value= "fail"
    else:
        value ="invalid grade"
    return value
g=input("enter a input:")
a=grades(g)
print(a)
