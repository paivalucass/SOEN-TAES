def tup_string(tup1):
    if not isinstance(tup1, tuple):
        raise ValueError("Input is not a tuple")
    
    if not all(isinstance(elem, str) for elem in tup1):
        raise ValueError("Tuple contains non-string elements")
    
    return ''.join(tup1)
import unittest

class Test(unittest.TestCase):
    def test_tup_string(self):
        self.assertEqual(tup_string(('e', 'x', 'e', 'r', 'c', 'i', 's', 'e', 's')), "exercises")

if __name__ == '__main__':
    unittest.main()