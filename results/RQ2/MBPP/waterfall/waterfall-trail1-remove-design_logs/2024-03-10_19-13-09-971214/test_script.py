def maximum(a, b):
    if type(a) not in [int, float] or type(b) not in [int, float]:
        return "Error"
    result = a if a > b else b
    return result
import unittest

class Test(unittest.TestCase):
    def test_maximum(self):
        self.assertEqual(maximum(5, 10), 10)

if __name__ == '__main__':
    unittest.main()