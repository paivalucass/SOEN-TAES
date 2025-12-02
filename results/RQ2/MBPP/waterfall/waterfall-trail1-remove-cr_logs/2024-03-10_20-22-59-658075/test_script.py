def find_length(binary_string):
    if not all(char in ['0', '1'] for char in binary_string):
        raise ValueError("Invalid binary string input")

    max_diff = 0
    current_diff = 0

    for char in binary_string:
        if char == '0':
            current_diff += 1
        else:
            current_diff -= 1
        
        if current_diff > max_diff:
            max_diff = current_diff
        if current_diff < 0:
            current_diff = 0

    return max_diff
import unittest

class Test(unittest.TestCase):
    def test_find_length(self):
        self.assertEqual(find_length('11000010001'), 6)

if __name__ == '__main__':
    unittest.main()