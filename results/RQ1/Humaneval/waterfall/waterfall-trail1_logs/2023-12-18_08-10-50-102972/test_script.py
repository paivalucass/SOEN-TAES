def flip_case(string: str) -> str:
    # flip the case of each character in the input string
    return string.swapcase()

import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(flip_case('Hello'), 'hELLO')

if __name__ == '__main__':
    unittest.main()