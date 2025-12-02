def upper_ctr(input_string):
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    
    upper_count = 0
    for char in input_string:
        if char.isupper():
            upper_count += 1
    
    return upper_count
import unittest

class Test(unittest.TestCase):
    def test_upper_ctr(self):
        self.assertEqual(upper_ctr('PYthon'), 2)

if __name__ == '__main__':
    unittest.main()