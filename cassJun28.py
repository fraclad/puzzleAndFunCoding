
def drawPrideFlag(n = 20):
    colors = [
    "255;0;24",
    "255;165;44",
    "255;255;65",
    "0;128;24",
    "0;0;249",
    "134;0;125"]

    for cols in colors:
        spacer = " "*n
        print("\033[38;2;{0};48;2;{1}m{2}".format(cols, cols, spacer))

drawPrideFlag()