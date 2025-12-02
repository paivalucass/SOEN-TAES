def odd_equivalent(input_string, rotation_count):
    if not all(char in '01' for char in input_string):
        return "Expected Error: Invalid characters in binary string"
    
    rotated_string = input_string[rotation_count % len(input_string):] + input_string[:rotation_count % len(input_string)]
    count = rotated_string.count('1')
    return count
import unittest

class Test(unittest.TestCase):
    def test_odd_Equivalent(self):
        self.assertEqual(odd_Equivalent("011001", 6), 3)

if __name__ == '__main__':
    unittest.main()