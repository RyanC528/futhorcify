import eng_to_ipa as p


class Translator:
    def __init__(self):
        self.instr = "hold"
        self.outstr = "ᚻᚩᚣᛞ"

    def translate(self, instr: str) -> None:
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
        hold: str = ""
        outstr: str = ""

        hold = p.convert(instr)

        for line in hold:
            for word in line:
                outstr.append("*" + word.remove("*", ""))

        return outstr

    def valid_str(self, instr: str) -> bool:
        return instr.isalpha()

    def set_instr(self, instr: str) -> None:
        self.instr = instr

    def get_outstr(self) -> str:
        return self.outstr

    def hash_decs(self) -> None:
        # hash for successful translation
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

        # hash for failed translation
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
