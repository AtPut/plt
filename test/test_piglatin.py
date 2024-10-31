import unittest
from piglatin import PigLatin
from error import PigLatinError


class TestPigLatin(unittest.TestCase):

    def test_something(self):
        pass

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