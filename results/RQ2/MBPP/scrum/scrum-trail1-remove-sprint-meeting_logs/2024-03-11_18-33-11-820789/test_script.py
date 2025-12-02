def even_Power_Sum(n):
    if not isinstance(n, int) or n < 1:
        return "Input must be a positive integer"

    def even_numbers_up_to_n(n):
        even_numbers = []
        num = 2
        while len(even_numbers) < n:
            even_numbers.append(num)
            num += 2
        return even_numbers

    def calculate_sum_of_even_numbers_raised_to_fifth_power(numbers):
        return sum(num**5 for num in numbers)

    return calculate_sum_of_even_numbers_raised_to_fifth_power(even_numbers_up_to_n(n))
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(even_Power_Sum(2), 1056)

if __name__ == '__main__':
    unittest.main()