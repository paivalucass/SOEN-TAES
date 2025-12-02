def minimum(a, b):
    try:
        if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
            raise TypeError("Inputs should be numeric")
        
        if a == b:
            return a  # or b, specify which value to return when a and b are equal
        elif a < b:
            return a
        else:
            return b
    except TypeError as e:
        raise e
import unittest

class Test(unittest.TestCase):
    def test_minimum(self):
        self.assertEqual(minimum(1, 2), 1)

if __name__ == '__main__':
    unittest.main()