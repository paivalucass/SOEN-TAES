def largest_prime_sum(lst):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    def sum_of_digits(num):
        return sum(int(digit) for digit in str(num))

    prime_nums = [num for num in lst if is_prime(num)]
    if prime_nums:
        max_prime = max(prime_nums)
        return sum_of_digits(max_prime)
    else:
        return 0

# Test cases
print(largest_prime_sum([0,3,2,1,3,5,7,4,5,5,5,2,181,32,4,32,3,2,32,324,4,3])) # Output: 10
print(largest_prime_sum([1,0,1,8,2,4597,2,1,3,40,1,2,1,2,4,2,5,1])) # Output: 25
print(largest_prime_sum([1,3,1,32,5107,34,83278,109,163,23,2323,32,30,1,9,3])) # Output: 13
print(largest_prime_sum([0,724,32,71,99,32,6,0,5,91,83,0,5,6])) # Output: 11
print(largest_prime_sum([0,81,12,3,1,21])) # Output: 3
print(largest_prime_sum([0,8,1,2,1,7])) # Output: 7
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(largest_prime_sum([0,3,2,1,3,5,7,4,5,5,5,2,181,32,4,32,3,2,32,324,4,3]), 10)
        self.assertEqual(largest_prime_sum([1,0,1,8,2,4597,2,1,3,40,1,2,1,2,4,2,5,1]), 25)
        self.assertEqual(largest_prime_sum([1,3,1,32,5107,34,83278,109,163,23,2323,32,30,1,9,3]), 13)
        self.assertEqual(largest_prime_sum([0,724,32,71,99,32,6,0,5,91,83,0,5,6]), 11)
        self.assertEqual(largest_prime_sum([0,81,12,3,1,21]), 3)
        self.assertEqual(largest_prime_sum([0,8,1,2,1,7]), 7)

if __name__ == '__main__':
    unittest.main()