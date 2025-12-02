def is_polite(n):
    '''Write a function to find nth polite number. geeksforgeeks.org/n-th-polite-number/
    assert is_polite(7) == 11'''
    def get_prime_factors(num):
        prime_factors = []
        divisor = 2
        while num > 1:
            while num % divisor == 0:
                prime_factors.append(divisor)
                num = num / divisor
            divisor += 1
        return prime_factors
    
    def count_divisors(prime_factors):
        divisor_count = 1
        current_count = 1
        for i in range(1, len(prime_factors)):
            if prime_factors[i] == prime_factors[i-1]:
                current_count += 1
            else:
                divisor_count *= (current_count + 1)
                current_count = 1
        divisor_count *= (current_count + 1)
        return divisor_count

    def is_polite_number(num):
        prime_factors = get_prime_factors(num)
        divisor_count = count_divisors(prime_factors)
        if divisor_count == n:
            return True
        else:
            return False

    if not isinstance(n, int) or n <= 0:
        raise ValueError("InputError")

    polite_count = 0
    nth_polite_number = 1
    while polite_count < n:
        nth_polite_number += 1
        if is_polite_number(nth_polite_number):
            polite_count += 1

    return nth_polite_number
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(is_polite(7), 11)

if __name__ == '__main__':
    unittest.main()