def number_ctr(input_string):
    try:
        digit_count = sum(c.isdigit() for c in input_string)
        return digit_count
    except Exception as e:
        print("Error: Invalid input. Please provide a valid input string.")

# Test cases
assert number_ctr('program2bedone') == 1
assert number_ctr('5hello3world') == 2
assert number_ctr('no_digits_here') == 0
assert number_ctr('Program2BeDone') == 1
assert number_ctr('123456789') == 9
assert number_ctr('abc') == 0
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(number_ctr('program2bedone'), 1)

if __name__ == '__main__':
    unittest.main()