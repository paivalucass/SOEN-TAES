def maximum(a, b):
    if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
        raise TypeError("Inputs should be numeric")
    if a == b:
        return a  # or b, depending on the desired behavior for equal inputs
    return max(a, b)
import unittest

class Test(unittest.TestCase):
    def test_maximum(self):
        self.assertEqual(maximum(5, 10), 10)

if __name__ == '__main__':
    unittest.main()