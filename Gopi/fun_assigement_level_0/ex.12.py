#12.wap to calculate profit and loss on a transaction from the given cost price
#and selling price 
def cal_profit(cp,sp):
    if cp>sp:
        loss=(cp-sp)
        v="{} is loss ".format(lo
    elif cp<sp:
        profit=(sp-cp)
        return("{} is profit ".format(profit))
    else:
        return("no profit and no loss {}".format(cp,sp))
cp=int(input("enter a cost price:"))
sp=int(input("enter a selling price:"))
a=cal_profit(cp,sp)
print(a)
