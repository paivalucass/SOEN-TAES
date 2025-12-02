def flip_case(string: str) -> str:
    if not isinstance(string, str):
        raise ValueError("Input must be a string")

    return string.swapcase()
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(flip_case('Hello'), 'hELLO')

if __name__ == '__main__':
    unittest.main()