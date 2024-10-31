
class PigLatin:
    def __init__(self, phrase: str):
        self.phrase = phrase

    def get_phrase(self) -> str:
        return self.phrase

    def translate(self) -> str:
        if self.phrase == "":
            return "nil"
        
        translated_words = []
        separated_by_spaces = False
        if self.phrase.__contains__('-'):
            words = self.phrase.split('-')
        else:
            words = self.phrase.split()
            separated_by_spaces = True
        for word in words:
            if word[0].lower() not in 'aeiou':
                # Move all leading consonants to the end
                index = 0
                while index < len(word) and word[index].lower() not in 'aeiou':
                    index += 1
                translated_word = word[index:] + word[:index]
            else:
                translated_word = word

            if translated_word[-1].lower() == 'y':
                translated_words.append(translated_word + "nay")
            elif translated_word[-1].lower() in 'aeiou':
                translated_words.append(translated_word + "yay")
            else:
                translated_words.append(translated_word + "ay")

        if separated_by_spaces is True:
            return " ".join(translated_words)
        return "-".join(translated_words)

