#11.wap to check whether an alphabet is vowel or consonant
def check_vowel_or_alphabet(x):
    y="AEIOU" or "aeiou"
    if x.upper() in y:
        return("{} is vowel ".format(x))
    else:
        return("{} is of consonent".format(x))

z=input("entr a alphabet:")
a=check_vowel_or_alphabet(z)
print(a)
