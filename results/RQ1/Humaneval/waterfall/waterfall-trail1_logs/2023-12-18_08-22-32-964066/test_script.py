def find_largest_prime_value_sum_of_digits(lst):
    if not lst or not all(isinstance(num, int) for num in lst):
        return 0
    prime_numbers = [num for num in lst if is_prime(num)]
    if not prime_numbers:
        return 0
    largest_prime = max(prime_numbers)
    return sum(int(digit) for digit in str(largest_prime))

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

# Testing
print(find_largest_prime_value_sum_of_digits([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
print(find_largest_prime_value_sum_of_digits([]))
print(find_largest_prime_value_sum_of_digits([2, 3, 5, 7]))
print(find_largest_prime_value_sum_of_digits([4, 6, 8, 9, 10]))
print(find_largest_prime_value_sum_of_digits([1, 4, 6, 8, 9, 10]))
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(function_under_test([0,3,2,1,3,5,7,4,5,5,5,2,181,32,4,32,3,2,32,324,4,3]), 10)
        self.assertEqual(function_under_test([1,0,1,8,2,4597,2,1,3,40,1,2,1,2,4,2,5,1]), 25)
        self.assertEqual(function_under_test([1,3,1,32,5107,34,83278,109,163,23,2323,32,30,1,9,3]), 13)
        self.assertEqual(function_under_test([0,724,32,71,99,32,6,0,5,91,83,0,5,6]), 11)
        self.assertEqual(function_under_test([0,81,12,3,1,21]), 3)
        self.assertEqual(function_under_test([0,8,1,2,1,7]), 7)

if __name__ == '__main':
    unittest.main()