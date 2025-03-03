class Translator():
    def __init__(self):
        self.hash_dec()
        self.cli()


    def cli(self) -> None:

        intro : str = '''Welcome this is the basic cli for the Futhorcify project, which allows for quick translations from Egnlish text into Runes
            To use, enter one of 3 commands.
            E -> Exit
            T -> Launch translator
            H -> Help to restate intro
        '''

        print(intro)
        
        while True:
            command: chr = input()

            if command == "E":
                print("Thank you for your time")
                break

            elif command == "T":
                print("Enter the word you wish translate")

                instr: str = input()

                if self.valid_str(instr):
                    self.translate(instr)

                else:
                    print("Error invalid characters")

            elif command == "H":
                print(intro)


            else:
                print("ERROR")
                print("This is a basic program, please only use listed commands. Anything else will throw an error")

    def translate(self, instr : str) -> None:
        outstr : str = ""

        instr = instr.lower()
        i : int = 0

        while i < len(instr):
            if (instr[i] == "t") and (instr[i + 1] == "h"):
                outstr = outstr + self.chart["th"]
                i = i + 1

            elif (instr[i] == "n") and (instr[i + 1] == "g"):
                outstr = outstr + self.chart["ng"]
                i = i + 1

            else:
                outstr = outstr + self.chart[instr[i]]

            i = i + 1

        print(outstr)

    def valid_str(self, instr: str) -> bool: 
        return instr.isalpha()


    def hash_dec(self) -> None: #completely unneeded, I just wanted to put the dict dec out of the way.
        self.chart :dict = {
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