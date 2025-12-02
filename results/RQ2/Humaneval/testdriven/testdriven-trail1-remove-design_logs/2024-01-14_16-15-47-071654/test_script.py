def flip_case(string: str) -> str:
    if not isinstance(string, str):
        raise TypeError("Input must be a valid string")
    
    return string.swapcase()
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(flip_case('Hello'), 'hELLO')

if __name__ == '__main__':
    unittest.main()