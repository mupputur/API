#10.wap to check whether a character is an alphabet or digi orspecial symbol
def find_chr(ch):
    if ((ch>='a' and ch<='z') or (ch>='A' and ch<='Z')):
        return("it is alphabet")
    elif ch>='0' and ch<='9' :
        return("it is a digit")
    elif ord(ch)>=36  and ord(ch)<=47:
        retunr("it is special symbol")
ch=input("enter a character:")
a=find_chr(ch)
print(a)
