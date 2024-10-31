
class PigLatin:
    def __init__(self, phrase: str):
        self.phrase = phrase

    def get_phrase(self) -> str:
        return self.phrase

    def translate(self) -> str:
        if self.phrase == "":
            return "nil"
        elif self.phrase[-1] == 'y':
            return self.phrase + "nay"
        elif self.phrase[-1].lower() in ('a', 'e', 'i', 'o', 'u'):
            return self.phrase + "yay"
        else:
            return self.phrase + "ay"

