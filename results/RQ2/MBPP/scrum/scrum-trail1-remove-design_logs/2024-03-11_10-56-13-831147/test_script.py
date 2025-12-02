def armstrong_number(number):
    # Check if the number is a single digit
    if number < 10:
        return True
    # Calculate the sum of the cubes of each digit in the number
    sum = 0
    temp = number
    while temp > 0:
        digit = temp % 10
        sum += digit ** 3
        temp //= 10
    # Check if the sum is equal to the original number
    return sum == number
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(armstrong_number(153), True)

if __name__ == '__main__':
    unittest.main()