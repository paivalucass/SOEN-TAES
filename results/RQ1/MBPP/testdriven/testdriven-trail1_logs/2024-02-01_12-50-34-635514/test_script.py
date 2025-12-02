def upper_ctr(input_str):
    if not isinstance(input_str, str):
        raise ValueError("Input_str must be a valid string.")
    
    count = 0
    for char in input_str:
        if char.isupper():
            count += 1
    return count
import unittest

class Test(unittest.TestCase):
    def test_upper_ctr(self):
        self.assertEqual(upper_ctr('PYthon'), 2)

if __name__ == '__main__':
    unittest.main()