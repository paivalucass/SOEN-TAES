def swap_numbers(a, b):
    if not isinstance(a, int) or not isinstance(b, int):
        raise ValueError("Input numbers should be integers")

    # Swap the numbers using a single line expression
    (a, b) = (b, a)
    
    return (a, b) # Return the tuple with the second number followed by the first number
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(swap_numbers(10,20), (20,10))

if __name__ == '__main__':
    unittest.main()