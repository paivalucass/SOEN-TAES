def find_Rotations(input_string):
    if input_string is None or not isinstance(input_string, str) or len(input_string) == 0 or not input_string.isalpha():
        return "Invalid Input"
    if len(set(input_string)) == 1:
        return len(input_string)
    return 1
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(find_Rotations('aaaa'), 1)

if __name__ == '__main__':
    unittest.main()