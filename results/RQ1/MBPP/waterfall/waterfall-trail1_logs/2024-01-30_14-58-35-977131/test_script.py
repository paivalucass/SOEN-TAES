def multiply_elements(test_tup):
    if not isinstance(test_tup, tuple):
        return "Error: Input is not a tuple of numbers"
    if len(test_tup) < 2:
        return "Error: Input tuple should have at least 2 elements"
    
    result = (test_tup[i] * test_tup[i+1] for i in range(len(test_tup)-1))
    return tuple(result)
import unittest

class Test(unittest.TestCase):
    def test_multiply_elements(self):
        self.assertEqual(multiply_elements((1, 5, 7, 8, 10)), (5, 35, 56, 80))

if __name__ == '__main__':
    unittest.main()