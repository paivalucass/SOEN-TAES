def split(word):
    result = [char for char in word if char.isalpha()]
    return result
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(split('python'), ['p','y','t','h','o','n'])

if __name__ == '__main__':
    unittest.main()