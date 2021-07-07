def translateShift(txt):
    validCharsList = [i for i in r"`1234567890-=qwertyuiop[]\asdfghjkl;'zxcvbnm,./"]
    decoded = ""
    for i in txt:
        if len(i.strip()) != 0:
            oriIndex = validCharsList.index(i)
            decodedIndex = oriIndex - 1
            decoded += validCharsList[decodedIndex]
        else:
            decoded += " "
    print(decoded)

translateShift(";p; epe")
translateShift("vtsmnrttu")
translateShift("urry")
translateShift("lrr[ sidyom eortf")