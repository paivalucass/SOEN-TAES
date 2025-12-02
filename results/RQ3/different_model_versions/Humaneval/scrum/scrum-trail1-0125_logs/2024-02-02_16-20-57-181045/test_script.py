def anti_shuffle(s):
    def sort_word(word):
        return ''.join(sorted(word))

    words = s.split()
    sorted_words = [sort_word(word) for word in words]
    return ' '.join(sorted_words)
import unittest


class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(anti_shuffle('Hi'), 'Hi')
        self.assertEqual(anti_shuffle('hello'), 'ehllo')
        self.assertEqual(anti_shuffle('Hello World!!!'), 'Hello !!!Wdlor')


if __name__ == '__main__':
    unittest.main()