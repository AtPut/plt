
class PigLatin:
    def __init__(self, phrase: str):
        self.phrase = phrase

    def get_phrase(self) -> str:
        return self.phrase

    def translate(self) -> str:
        if self.phrase == "":
            return "nil"
        else:
            # if ends to y append nay to end of phase
            if self.phrase.endswith('y'):
                phrase = self.phrase + "nay"
            else:
                return self.phrase
            return phrase