
import re
from audioop import error

from error import PigLatinError


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
        if '-' in self.phrase:
            words = self.phrase.split('-')
        else:
            words = re.split(r'(\W+)', self.phrase)  # Split by non-word characters but keep them
            separated_by_spaces = True
        
        for word in words:
            if word.isalpha():  # Process only alphabetic words
                if word[0].lower() not in 'aeiou':
                    # Move all leading consonants to the end
                    index = 0
                    word = word[0].lower() + word[1:]
                    while index < len(word) and word[index].lower() not in 'aeiou':
                        index += 1
                    translated_word = word[index:] + word[:index]
                    translated_word.capitalize()
                else:
                    translated_word = word

                if translated_word[-1].lower() == 'y':
                    if translated_word.isupper():
                        translated_words.append(translated_word + "NAY")
                    elif translated_word[1:].islower():
                        translated_words.append(translated_word + "nay")
                    else:
                        raise PigLatinError
                elif translated_word[-1].lower() in 'aeiou':
                    if translated_word.isupper():
                        translated_words.append(translated_word + "YAY")
                    elif translated_word[1:].islower():
                        translated_words.append(translated_word + "yay")
                    else:
                        raise PigLatinError
                else:
                    if translated_word.isupper():
                        translated_words.append(translated_word + "AY")
                    elif translated_word[1:].islower():
                        translated_words.append(translated_word + "ay")
                    else:
                        raise  PigLatinError
            else:
                translated_words.append(word)  # Append non-alphabetic parts unchanged

        if separated_by_spaces:
            return "".join(translated_words)  # Join everything including punctuation
        return "-".join(translated_words)

