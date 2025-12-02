def ascii_value(k):
    if len(k) != 1:
        raise ValueError("Input must be a single character")
    
    try:
        ascii_val = ord(k)
        return ascii_val
    except TypeError:
        raise TypeError("Input must be a single character")
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(ascii_value('A'), 65)

if __name__ == '__main__':
    unittest.main()