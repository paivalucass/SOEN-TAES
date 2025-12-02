def reverse_words(s):
    words = s.split()
    left = 0
    right = len(words) - 1
    while left < right:
        words[left], words[right] = words[right], words[left]
        left += 1
        right -= 1
    return ' '.join(words)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(reverse_words('python program'), 'program python')

if __name__ == '__main__':
    unittest.main()