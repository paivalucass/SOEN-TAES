def find_Rotations(input_string):
    if not input_string:
        return "Error: Empty input string"
    if not input_string.isalpha():
        return "Error: Invalid input string"
    n = len(input_string)
    pattern = input_string + input_string
    for i in range(1, n+1):
        if pattern[i:i+n] == input_string:
            return i
    return n
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(find_Rotations('aaaa'), 1)

if __name__ == '__main__':
    unittest.main()