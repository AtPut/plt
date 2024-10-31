vowel = ('a', 'e', 'i', 'o', 'u')
class PigLatin:
    def __init__(self, phrase: str):
        self.phrase = phrase

    def get_phrase(self) -> str:
        return self.phrase

    def translate(self) -> str:
        if self.phrase == "":
            return "nil"
        elif self.phrase.endswith('y'):
            return self.phrase + "nay"
        elif self.phrase.endswith(vowel):
            return  self.phrase + "yay"
        else:
            return self.phrase

