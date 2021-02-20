#14.wap to find the eligibility of adimossion for a professionl course based
#on the follwing criteria
def eligible_for_adimision(x,y,z,a,b):
    if maths>=65 and total>=180:
        v="this canditate is eligible for profisinal course"
    elif maths<65 and total>=180:
        v="this canditate not eligible for course"
    elif chem>=55 and total>=180:
        v="this canditate is eligible for profisinal course"
    elif chem<55 and total>=180:
        v="this canditate not eligible for course"
    elif phy>=50 and total>=180:
        v="this canditate is eligible for profisinal course"
    elif phy<50 and total>=180:
        v="this canditate not eligible for course"
    elif total>=180  and total2>=140:
        v="this canditate is eligible for profisinal course"
    else:
        v="this canditate not eligible for course"
    return v


maths=int(input("enter a maths marks:"))
chem=int(input("enter a chem marsk:"))
phy=int(input("enter a phy marks:"))
total=maths+chem+phy
total2=maths+phy
a=eligible_for_adimision(maths,chem,phy,total,total2)
print(a)
