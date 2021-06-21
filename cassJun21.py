
import math

def drawCube(x):
    print("length = {} unit".format(x))

    corr = 0 if x%2 == 0 else 1

    top = " "*(x + int(1 - 0.5*x)) + "+" + "-"*(2*x - corr) + "+"
    isoTop = ""
    for i in range(int(x/2)):
        mid = " "*(x-(i) - int(0.5*x) - corr) + "/" + " "*(2*x) + "/" + " "*(i) + "|"
        isoTop += "\n" + mid
    topBase = "+" + "-"*(2*x) + "+" + " "*(math.ceil(x/2) - corr)  + "|"
    text = top + isoTop + "\n" + topBase

    side = ""
    for i in range(x):
        if i == x - int(x/2 + 1):
            mid = "|" + " "*(2*x) + "|" + " "*(x-int(x/2) - corr) + "+"
        elif i > int(x/2 - 1):
            mid = "|" + " "*(2*x) + "|" + " "*(x - i - 1) + "/"
        else:
            mid = "|" + " "*(2*x) + "|" + " "*(x-int(x/2) - corr) + "|"
        side += "\n" + mid
    text += side + "\n+" + "-"*(2*x) + "+"
    print("")
    print(text)

drawCube(2)
drawCube(4)
drawCube(7)
drawCube(10)
