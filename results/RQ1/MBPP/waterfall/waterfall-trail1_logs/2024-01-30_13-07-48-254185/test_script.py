from typing import Union

def minimum(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
        raise ValueError("Input parameters should be of numeric data types (int, float, etc.)")
    
    if a == b:
        raise ValueError("Both numbers are the same")

    return min(a, b)
import unittest

class Test(unittest.TestCase):
    def test_minimum(self):
        self.assertEqual(minimum(1, 2), 1)

if __name__ == '__main__':
    unittest.main()