def rearrange_bigger(n):
    '''Write a function to create the next bigger number by rearranging the digits of a given number.'''
    if not isinstance(n, int) or n < 0:
        return "Invalid input"  # Check if input is a valid positive integer
    digits = [int(x) for x in str(n)]  # Convert the input number into a list of its digits
    for i in range(len(digits) - 1, 0, -1):  # Loop through the digits in reverse order
        if digits[i] > digits[i - 1]:  # Find the first pair of digits where the second digit is larger than the first
            tmp = digits[i - 1]  # Swap the two digits
            digits[i - 1] = digits[i]
            digits[i] = tmp
            result = int("".join(map(str, digits)))  # Convert the rearranged digits back to a number
            return result  # Return the next bigger number
    return "No bigger number can be formed"  # If no bigger number can be formed, return this message

assert rearrange_bigger(12) == 21  # Test case: input 12 should return 21

import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(rearrange_bigger(12), 21)

if __name__ == '__main__':
    unittest.main()