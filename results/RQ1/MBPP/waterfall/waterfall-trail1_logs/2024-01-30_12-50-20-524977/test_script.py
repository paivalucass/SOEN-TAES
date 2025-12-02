def count_Primes_nums(n):
    '''Write a python function that takes in a non-negative number and returns the number of prime numbers less than the given non-negative number.'''
    if not isinstance(n, int) or n < 0:
        return "Invalid input"
    
    def is_prime(num):
        if num <= 1:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    count = 0
    for num in range(2, n):
        if is_prime(num):
            count += 1
    return count

# Test Cases
assert count_Primes_nums(5) == 2
assert count_Primes_nums(-5) == "Invalid input"
assert count_Primes_nums(0) == 0
assert count_Primes_nums(1000) == 168
assert count_Primes_nums(10) == 4
assert count_Primes_nums('abc') == "Invalid input"
assert count_Primes_nums('@#%') == "Invalid input"
assert count_Primes_nums(1) == 0
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(count_Primes_nums(5), 2)

if __name__ == '__main__':
    unittest.main()