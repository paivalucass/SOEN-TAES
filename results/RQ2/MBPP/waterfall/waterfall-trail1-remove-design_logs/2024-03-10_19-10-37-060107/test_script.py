def swap_numbers(a, b):
    if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
        raise ValueError("Input parameters must be numbers.")
    
    return (b, a)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(swap_numbers(10, 20), (20, 10))

if __name__ == '__main__':
    unittest.main()