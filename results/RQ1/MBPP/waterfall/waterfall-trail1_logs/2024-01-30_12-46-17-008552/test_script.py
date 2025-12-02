def count_charac(input_string: str) -> int:
    if len(input_string) > 1000:
        raise ValueError("Input string length should not exceed 1000 characters")

    if not isinstance(input_string, str):
        raise TypeError("Input should be a string")

    char_count = sum(1 for char in input_string if char.isalnum())

    return char_count
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(count_charac('python programming'), 18)

if __name__ == '__main__':
    unittest.main()