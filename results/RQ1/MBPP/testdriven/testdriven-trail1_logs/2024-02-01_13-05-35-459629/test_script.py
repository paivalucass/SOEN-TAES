def reverse_words(s):
    '''
    Write a function to reverse words separated by spaces in a given string.
    assert reverse_words("python program")==("program python")
    '''
    if s is None or s.strip() == "":
        return "Invalid input"

    words = s.split()
    return ' '.join(words[::-1])
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(reverse_words('python program'), 'program python')

if __name__ == '__main__':
    unittest.main()