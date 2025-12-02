def reverse_words(s):
    if s is None or s.strip() == '':
        return "Invalid input"
    
    words = s.split()
    reversed_sentence = ' '.join(reversed(words))
    return reversed_sentence
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(reverse_words('python program'), 'program python')

if __name__ == '__main__':
    unittest.main()