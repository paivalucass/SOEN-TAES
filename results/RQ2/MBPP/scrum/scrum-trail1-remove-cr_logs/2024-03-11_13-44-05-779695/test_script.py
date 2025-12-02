def armstrong_number(number):
    if not isinstance(number, int) or number < 0:
        raise ValueError("Input must be a positive integer")

    # Calculate the sum of the cubes of each digit in the number
    temp = number
    sum_of_cubes = 0
    while temp > 0:
        digit = temp % 10
        sum_of_cubes += digit ** 3
        temp //= 10

    # Compare the sum with the original number and return True if they are equal, otherwise return False
    return sum_of_cubes == number

import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(armstrong_number(153), True)

if __name__ == '__main__':
    unittest.main()