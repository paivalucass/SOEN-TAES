def upper_ctr(s):
    if type(s) != str:
        return "Error: Input is not a string."
    elif len(s) == 0:
        return "Error: Input string is empty."
    
    count = 0
    for char in s:
        if char.isupper():
            count += 1
    
    return count
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(upper_ctr('PYthon'), 2)

if __name__ == '__main__':
    unittest.main()