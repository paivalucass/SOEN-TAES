def flip_case(string: str) -> str:
    """For a given string, flip lowercase characters to uppercase and uppercase to lowercase."""
    if string is None:
        return ""

    if len(string) > 1000:
        raise ValueError("Input string length must be 1000 characters or less.")

    return string.swapcase()

import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(flip_case('Hello'), 'hELLO')
        self.assertEqual(flip_case('hElLo'), 'HeLlO')
        self.assertEqual(flip_case('123'), '123')
        self.assertEqual(flip_case(''), '')

if __name__ == '__main__':
    unittest.main()