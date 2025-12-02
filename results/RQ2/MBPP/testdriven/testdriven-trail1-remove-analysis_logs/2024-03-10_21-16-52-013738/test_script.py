def maximum(a, b):
    '''This function returns the maximum of two numbers.'''
    if isinstance(a, (int, float)) and isinstance(b, (int, float)):
        return max(a, b)
    else:
        return "Error: Invalid input types"
import unittest

class Test(unittest.TestCase):
    def test_maximum(self):
        self.assertEqual(maximum(5, 10), 10)

if __name__ == '__main__':
    unittest.main()