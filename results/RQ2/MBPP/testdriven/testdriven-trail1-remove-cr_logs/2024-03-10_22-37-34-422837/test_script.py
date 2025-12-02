def sum_div(number):
    '''
    This function takes a number as input and returns the sum of all divisors of that number.

    Parameters:
    number (int): The input number for which the sum of divisors needs to be calculated.

    Returns:
    int: The sum of all divisors of the input number.
    '''
    if number <= 0:
        return 0
    div_sum = 1
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            div_sum += i
            if i != number // i:
                div_sum += number // i
    return div_sum

import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(sum_div(8), 7)

if __name__ == '__main__':
    unittest.main()