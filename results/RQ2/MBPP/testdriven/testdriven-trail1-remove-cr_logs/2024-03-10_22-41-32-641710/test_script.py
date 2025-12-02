def remove_odd(str1):
    new_string = str1[1::2]
    return new_string
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(remove_odd('python'), 'yhn')

if __name__ == '__main__':
    unittest.main()