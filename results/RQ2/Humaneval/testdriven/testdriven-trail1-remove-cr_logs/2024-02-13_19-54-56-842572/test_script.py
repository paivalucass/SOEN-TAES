def generate_integers(a, b):
    result = []
    if not isinstance(a, int) or not isinstance(b, int) or a <= 0 or b <= 0:
        return result
    
    if a > b:
        a, b = b, a
    
    for num in range(a, b + 1):
        if num % 2 == 0:
            result.append(num)
    
    return result
import unittest

class Test(unittest.TestCase):
    def test_generate_integers(self):
        self.assertEqual(generate_integers(2, 8), [2, 4, 6, 8])
        self.assertEqual(generate_integers(8, 2), [2, 4, 6, 8])
        self.assertEqual(generate_integers(10, 14), [])

if __name__ == '__main__':
    unittest.main()