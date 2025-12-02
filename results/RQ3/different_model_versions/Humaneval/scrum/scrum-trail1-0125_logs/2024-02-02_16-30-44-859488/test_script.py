def generate_integers(a, b):
    if a <= b:
        return [i for i in range(a, b+1) if i % 2 == 0]
    else:
        return 'Invalid input: a must be less than or equal to b'
import unittest

class Test(unittest.TestCase):
    def test_generate_integers(self):
        self.assertEqual(generate_integers(2, 8), [2, 4, 6, 8])
        self.assertEqual(generate_integers(8, 2), [2, 4, 6, 8])
        self.assertEqual(generate_integers(10, 14), [])

if __name__ == '__main__':
    unittest.main()