def anti_shuffle(s):
    if not isinstance(s, str) or s == '':
        return 'Invalid input'

    words = s.split(' ')
    ordered_words = [''.join(sorted(word)) for word in words]
    return ' '.join(ordered_words)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(anti_shuffle('Hi'), 'Hi')
        self.assertEqual(anti_shuffle('hello'), 'ehllo')
        self.assertEqual(anti_shuffle('Hello World!!!'), 'Hello !!!Wdlor')

if __name__ == '__main__':
    unittest.main()