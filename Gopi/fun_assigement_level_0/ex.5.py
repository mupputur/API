#5.wap to read the age of candidate and determine whether it is eligiable
#for casting his/her own vote.
def vote(x):
    if x>=18:
        return("person is eligiable for vote")
    else:
        return("person is not eligiable for vote")
x=int(input("enter a age of candate:"))
a=vote(x)
print(a)
