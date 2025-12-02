def hexagonal_num(n):
    '''Write a function to find the nth hexagonal number.'''
    try:
        if not isinstance(n, int):
            raise ValueError("Input must be a valid integer")
        
        if n <= 0:
            raise ValueError("Input must be a positive integer")
        
        result = n * (2 * n - 1)
        return result
    except ValueError as ve:
        print(ve)
        return None
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(hexagonal_num(10), 190)

if __name__ == '__main__':
    unittest.main()