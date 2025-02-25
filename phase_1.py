chart : dict = {
    "a" : "ᚪ",
    "b" : "ᛒ",
    "c" : "ᚳ",
    "d" : "ᛞ",
    "e" : "ᛖ",
    "f" : "ᚠ",
    "g" : "ᚷ",
    "h" : "ᚻ",
    "i" : "ᛁ",
    "j" : "ᛡ",
    "k" : "ᛣ",
    "l" : "ᛚ",
    "m" : "ᛗ",
    "n" : "ᚾ",
    "o" : "ᚩ",
    "p" : "ᛈ",
    "q" : "ᛢ",
    "r" : "ᚱ",
    "s" : "ᛋ",
    "t" : "ᛏ",
    "u" : "ᚢ",
    "v" : "ᚠ",
    "w" : "ᚹ",
    "x" : "ᛉ",
    "y" : "ᚣ",
    "z" : "ᛋ",
    "th": "ᚦ",
    "ng": "ᛝ",
    " " : " "
}

instr : str = "running"
outstr : str = ""

instr = instr.lower()
i : int = 0

while i < len(instr):
    if (instr[i] == "t") and (instr[i + 1] == "h"):
        outstr = outstr + chart["th"]
        i = i + 1

    elif (instr[i] == "n") and (instr[i + 1] == "g"):
        outstr = outstr + chart["ng"]
        i = i + 1

    else:
        outstr = outstr + chart[instr[i]]

    i = i + 1

print(outstr)