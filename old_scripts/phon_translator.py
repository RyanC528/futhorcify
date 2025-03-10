import eng_to_ipa as p


class Translator:
    def __init__(self):
        self.hash_dec()
        self.cli()

    def cli(self) -> None:

        intro: str = """Welcome this is the basic cli for the Futhorcify project, which allows for quick translations from Egnlish text into Runes
            To use, enter one of 3 commands.
            E -> Exit
            T -> Launch translator
            F -> Translate File
            H -> Help to restate intro
        """

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
                    print(self.translate(self.to_ipa(instr)))

                else:
                    print("Error invalid characters")

            elif command == "H":
                print(intro)

            elif command == "F":
                self.file_bs()
                print("File has been translated")

            else:
                print("ERROR")
                print(
                    "This is a basic program, please only use listed commands. Anything else will throw an error"
                )

    def translate(self, instr: str) -> str:
        outstr: str = ""

        instr = instr.lower()
        i: int = 0
        lib_error: bool = False

        while i < len(instr):
            # root out dipthongs and

            if instr[i] == "*":
                lib_error = True

            if instr[i] == " ":
                lib_error = False

            if lib_error == True:
                outstr = outstr + self.e_chart[instr]

            elif lib_error == False:
                if (instr[i] == "a") and (instr[i + 1] == "ʊ"):
                    outstr = outstr + self.p_chart["aʊ"]
                    i = i + 1

                elif (instr[i] == "a") and (instr[i + 1] == "ɪ"):
                    outstr = outstr + self.p_chart["aɪ"]
                    i = i + 1

                elif (instr[i] == "e") and (instr[i + 1] == "ɪ"):
                    outstr = outstr + self.p_chart["eɪ"]
                    i = i + 1

                elif (instr[i] == "o") and (instr[i + 1] == "ʊ"):
                    outstr = outstr + self.p_chart["oʊ"]
                    i = i + 1

                elif (instr[i] == "ɔ") and (instr[i + 1] == "ɪ"):
                    outstr = outstr + self.p_chart["ɔɪ"]
                    i = i + 1

                else:
                    outstr = outstr + self.p_chart[instr[i]]

            i = i + 1

        return outstr

    def to_ipa(self, instr: str) -> str:
        return p.convert(instr)

    def valid_str(self, instr: str) -> bool:
        return instr.isalpha()

    def file_bs(self) -> None:
        f_in = open("/home/ryanc/futhorcify/text_files/input.txt", "rt")
        f_out = open("/home/ryanc/futhorcify/text_files/output.txt", "wt")

        for line in f_in:
            f_out.write(self.translate(p.convert(line)))
            f_out.write("\n")

        f_in.close()
        f_out.close()

    def hash_dec(
        self,
    ) -> None:  # completely unneeded, I just wanted to put the dict dec out of the way.
        self.p_chart: dict = {
            # ipa - output rune
            "ɑ": "ᚪ",
            "æ": "ᚫ",
            "ə": "ᛖ",
            "ʌ": "ᛟ",
            "ɔ": "ᚩ",
            "aʊ": "ᚪᚣ",
            "aɪ": "ᚪᛇ",
            "ɛ": "ᛠ",
            "eɪ": "ᛖᛇ",
            "ɪ": "ᛇ",
            "i": "ᛁ",
            "oʊ": "ᚩᚣ",
            "ɔɪ": "ᚩᛇ",
            "ʊ": "ᚣ",
            "u": "ᚢ",
            "b": "ᛒ",
            "ʧ": "ᚳᚻ",
            "d": "ᛞ",
            "ð": "ᚦ",
            "f": "ᚠ",
            "g": "ᚷ",
            "h": "ᚻ",
            "ʤ": "ᚷ",
            "k": "ᚳ",
            "l": "ᛚ",
            "m": "ᛗ",
            "n": "ᚾ",
            "ŋ": "ᛝ",
            "p": "ᛈ",
            "r": "ᚱ",
            "s": "ᛋ",
            "ʃ": "ᛋᚻ",
            "t": "ᛏ",
            "θ": "ᚦ",
            "v": "",
            "w": "ᚹ",
            "j": "ᛡ",
            "z": "ᛉ",
            "ʒ": "ᛉᚻ",
            " ": " ",
            "\n": "\n",
            ",": ",",
            ".": ".",
            "ˈ": "",
            "ˌ": "",
            "'": "'",
        }

        self.e_chart: dict = {
            "a": "ᚪ",
            "b": "ᛒ",
            "c": "ᚳ",
            "d": "ᛞ",
            "e": "ᛖ",
            "f": "ᚠ",
            "g": "ᚷ",
            "h": "ᚻ",
            "i": "ᛁ",
            "j": "ᛡ",
            "k": "ᛣ",
            "l": "ᛚ",
            "m": "ᛗ",
            "n": "ᚾ",
            "o": "ᚩ",
            "p": "ᛈ",
            "q": "ᛢ",
            "r": "ᚱ",
            "s": "ᛋ",
            "t": "ᛏ",
            "u": "ᚢ",
            "v": "ᚠ",
            "w": "ᚹ",
            "x": "ᛉ",
            "y": "ᚣ",
            "z": "ᛋ",
            "th": "ᚦ",
            "ng": "ᛝ",
            " ": " ",
            "\n": "\n",
            "*": "",
            ",": ",",
            "'": "'",
        }
