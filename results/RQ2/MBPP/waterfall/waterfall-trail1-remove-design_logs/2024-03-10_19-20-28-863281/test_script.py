def perfect_squares(a, b):
    if not isinstance(a, int) or not isinstance(b, int) or a <= 0 or b <= 0 or a >= b:
        return "Invalid input. 'a' and 'b' should be positive integers where 'a' is less than 'b'."
    
    result = [i*i for i in range(int(a**0.5), int(b**0.5)+1)]
    return result

import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(perfect_squares(1,30), [1, 4, 9, 16, 25])

if __name__ == '__main__':
    unittest.main()