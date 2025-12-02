def remove_odd(str1):
    if len(str1) % 2 == 0:
        return str1[1::2]
    else:
        return "Invalid Input"
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(remove_odd('python'), 'yhn')

if __name__ == '__main__':
    unittest.main()