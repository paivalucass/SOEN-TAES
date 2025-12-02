def hexagonal_num(n):
    '''
    Write a function to find the nth hexagonal number.
    assert hexagonal_num(10) == 190
    '''
    if not isinstance(n, int):
        return "Error: Input must be an integer"
    
    if n <= 0:
        return 0
    
    # Calculate the nth hexagonal number
    hex_num = n * (2 * n - 1)
    
    return hex_num

import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(hexagonal_num(10), 190)

if __name__ == '__main__':
    unittest.main()