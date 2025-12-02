def remove_odd(str1):
    '''Write a function to remove odd characters in a string.'''
    return str1[1::2]
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(remove_odd('python'), 'yhn')

if __name__ == '__main__':
    unittest.main()