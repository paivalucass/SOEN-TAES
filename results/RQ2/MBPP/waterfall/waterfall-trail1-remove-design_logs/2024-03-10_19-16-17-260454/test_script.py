def multiple_to_single(L):
    try:
        result = int(''.join(map(str, L)))
        return result
    except (ValueError, TypeError):
        return "Error: Please provide a list of numeric values"
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(multiple_to_single([11, 33, 50]), 113350)

if __name__ == '__main__':
    unittest.main()