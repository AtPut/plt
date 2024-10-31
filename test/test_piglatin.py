import unittest
from piglatin import PigLatin
from error import PigLatinError


class TestPigLatin(unittest.TestCase):


    def test_create_translator_and_get_phrase(self):
        piglatin = PigLatin("hello world")
        phrase = piglatin.get_phrase()
        self.assertEqual("hello world", phrase)

    def test_translate_empty_string_to_nil(self):
        piglatin = PigLatin("")
        phrase = piglatin.translate()
        self.assertEqual("nil", phrase)

    def test_phrase_ends_y_translate_append_nay(self):
        piglatin = PigLatin("any")
        phrase = piglatin.translate()
        self.assertEqual("anynay", phrase)

    def test_phrase_ends_with_vowel_translate_append_yay(self):
        piglatin = PigLatin("Apple")
        phrase = piglatin.translate()
        self.assertEqual("Appleyay", phrase)

    def test_phrase_ends_with_consonants_translate_append_ay(self):
        piglatin = PigLatin("ask")
        phrase = piglatin.translate()
        self.assertEqual("askay", phrase)

    def test_phrase_starts_with_consonants_translate_move_to_end_append_ay(self):
        piglatin = PigLatin("hello")
        phrase = piglatin.translate()
        self.assertEqual("ellohay", phrase)

    def test_phrase_starts_with_more_consonants_translate_move_to_end_append_ay(self):
        piglatin = PigLatin("known")
        phrase = piglatin.translate()
        self.assertEqual("ownknay", phrase)

    def test_translate_phrase_contains_multiple_words(self):
        piglatin = PigLatin("hello world")
        phrase = piglatin.translate()
        self.assertEqual("ellohay orldway", phrase)

    def test_translate_phrase_contains_multiple_words_separated_by_line(self):
        piglatin = PigLatin("well-being")
        phrase = piglatin.translate()
        self.assertEqual("ellway-eingbay", phrase)

    def test_phrase_contains_punctuations_translate_keeps_punctuations_inplace(self):
        piglatin = PigLatin('"hello world!"')
        phrase = piglatin.translate()
        self.assertEqual('"ellohay orldway!"', phrase)