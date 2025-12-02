def upper_ctr(input_string):
    if not isinstance(input_string, str):
        raise ValueError("Invalid input: input should be a string")
    else:
        return sum(1 for char in input_string if char.isupper())
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(upper_ctr('PYthon'), 1)

if __name__ == '__main__':
    unittest.main()