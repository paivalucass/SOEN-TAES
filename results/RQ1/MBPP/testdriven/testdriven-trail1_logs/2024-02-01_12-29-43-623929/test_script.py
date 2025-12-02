def sum_div(number):
    '''Write a function to return the sum of all divisors of a number.'''
    if not isinstance(number, int) or number <= 0:
        return "Invalid input: Please enter a positive integer"

    div_sum = 1
    for i in range(2, int(number**0.5)+1):
        if number % i == 0:
            div_sum += i
            if i != number // i:
                div_sum += number // i
    return div_sum

assert sum_div(8) == 7
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(sum_div(8), 7)

if __name__ == '__main__':
    unittest.main()