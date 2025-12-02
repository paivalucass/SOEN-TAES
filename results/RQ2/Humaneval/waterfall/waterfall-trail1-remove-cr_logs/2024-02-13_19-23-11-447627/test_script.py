def anti_shuffle(s):
    if not isinstance(s, str):
        raise TypeError("Input should be a string")

    if s == "":
        return ""

    words = s.split(" ")
    ordered_words = []

    for word in words:
        ordered_word = "".join(sorted(word))
        ordered_words.append(ordered_word)

    ordered_version = " ".join(ordered_words)
    return ordered_version
import unittest

class Test(unittest.TestCase):
    def test_anti_shuffle(self):
        self.assertEqual(anti_shuffle('Hi'), 'Hi')
        self.assertEqual(anti_shuffle('hello'), 'ehllo')
        self.assertEqual(anti_shuffle('Hello World!!!'), 'Hello !!!Wdlor')

if __name__ == '__main__':
    unittest.main()