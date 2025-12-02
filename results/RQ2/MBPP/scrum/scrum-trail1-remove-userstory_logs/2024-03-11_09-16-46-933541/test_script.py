def find_adverbs(text):
    words = text.split()
    for i in range(len(words)):
        if words[i].endswith('ly'):
            return f'{i}-{i+len(words[i])-1}: {words[i]}'
    return ''
import unittest

class Test(unittest.TestCase):

    def test(self):
        self.assertEqual(find_adverbs("Clearly, he has no excuse for such behavior."), '0-7: Clearly')

if __name__ == '__main__':
    unittest.main()