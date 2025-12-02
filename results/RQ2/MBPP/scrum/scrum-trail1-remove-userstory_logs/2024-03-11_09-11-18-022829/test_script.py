def remove_odd(str1):
    if str1 is None:
        return "Input should be a valid string"
    if not isinstance(str1, str):
        return "Input should be a valid string"
    
    return str1[1::2]
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(remove_odd('python'), 'yhn')

if __name__ == '__main__':
    unittest.main()