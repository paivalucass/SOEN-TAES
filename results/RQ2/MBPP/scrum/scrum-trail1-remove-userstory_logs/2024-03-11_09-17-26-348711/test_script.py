def is_perfect_square(n):
    if n < 0:
        return False
    root = n ** 0.5
    return int(root) ** 2 == n

def perfect_squares(a, b):
    if not isinstance(a, int) or not isinstance(b, int) or a < 0 or b < 0:
        return "Invalid input: Both 'a' and 'b' must be positive integers"
    
    result = []
    for num in range(a, b+1):
        if is_perfect_square(num):
            result.append(num)
    return result
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(perfect_squares(1,30), [1, 4, 9, 16, 25])

if __name__ == '__main__':
    unittest.main()