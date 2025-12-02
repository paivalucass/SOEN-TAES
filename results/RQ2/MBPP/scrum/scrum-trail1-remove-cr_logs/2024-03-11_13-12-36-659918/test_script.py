def minimum(a, b):
    try:
        if type(a) not in [int, float] or type(b) not in [int, float]:
            raise TypeError("Input parameters must be numbers")
        
        return min(a, b)
    except Exception as e:
        return f"Error: {e}"
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(minimum(1, 2), 1)

if __name__ == '__main__':
    unittest.main()