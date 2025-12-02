def odd_Equivalent(binary_string, rotate_times):
    '''Write a python function to find the number of numbers with an odd value when rotating a binary string the given number of times.
    assert odd_Equivalent("011001", 6) == 3'''
    if not all(char in '01' for char in binary_string) or rotate_times < 0:
        return "Invalid input"
    count = 0
    integer_val = int(binary_string, 2)
    for _ in range(rotate_times):
        integer_val = (integer_val << 1) | (integer_val >> (len(binary_string) - 1))
        if integer_val % 2 != 0:
            count += 1
    return count
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(odd_Equivalent("011001", 6), 3)

if __name__ == '__main__':
    unittest.main()