
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
            # Move all leading consonants to the end
            index = 0
            while index < len(self.phrase) and self.phrase[index].lower() not in ('a', 'e', 'i', 'o', 'u'):
                index += 1
            phrase = self.phrase[index:] + self.phrase[:index]
        else:
            phrase = self.phrase

        last_char = phrase[-1].lower()
        if last_char == 'y':
            return phrase + "nay"
        elif last_char in ('a', 'e', 'i', 'o', 'u'):
            return phrase + "yay"
        else:
            return phrase + "ay"

