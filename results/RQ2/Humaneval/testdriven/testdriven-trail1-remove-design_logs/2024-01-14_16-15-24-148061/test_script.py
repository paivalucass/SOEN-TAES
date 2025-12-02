def strlen(input_string: str) -> int:
    try:
        if input_string is None or input_string == "":
            raise ValueError("Input string is null or empty")
        return len(input_string)
    except ValueError as ve:
        print(ve)
        return 0
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(strlen(''), 0)
        self.assertEqual(strlen('abc'), 3)

if __name__ == '__main__':
    unittest.main()