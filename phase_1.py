chart : dict = {
    "a" : "a",
    "b" : "b",
    "c" : "c",
    "d" : "d",
    "e" : "e",
    "f" : "f",
    "g" : "g",
    "h" : "h",
    "i" : "i",
    "j" : "j",
    "k" : "k",
    "l" : "l",
    "m" : "m",
    "n" : "n",
    "o" : "o",
    "p" : "p",
    "q" : "q",
    "r" : "r",
    "s" : "s",
    "t" : "t",
    "u" : "u",
    "v" : "v",
    "w" : "w",
    "x" : "x",
    "y" : "y",
    "z" : "z",
    "th": "th",
    "ng": "ng"
}

instr : str = ""
outstr : str = ""

instr = instr.lower()

for i in range(0 , len(instr) - 1):
    if (instr[i] == "t") and (instr[i + 1] == "h"):
        outstr = outstr + chart["th"]

    elif (instr[i] == "n") and (instr[i + 1] == "g"):
        outstr = outstr + chart["ng"]

    else:
        outstr = outstr + chart[instr[i]]