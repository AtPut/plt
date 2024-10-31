from boltons.iterutils import first


class PigLatin:
    def __init__(self, phrase: str):
        self.phrase = phrase

    def get_phrase(self) -> str:
        return self.phrase

    def translate(self) -> str:
        if self.phrase == "":
            return "nil"
        first_char = self.phrase[0].lower()
        if first_char not in ('a', 'e', 'i', 'o', 'u'):
            phrase = self.phrase[1:] + first_char
        else:
            last_char = self.phrase[-1].lower()  # Ensure case-insensitivity
            if last_char == 'y':
                return self.phrase + "nay"
            elif last_char in ('a', 'e', 'i', 'o', 'u'):
                return self.phrase + "yay"
            else:
                phrase = self.phrase

        return phrase + "ay"

