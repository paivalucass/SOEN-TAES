def prime_fib(n: int):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True
    
    def generate_fibonacci():
        fib = [0, 1]
        while True:
            next_fib = fib[-1] + fib[-2]
            fib.append(next_fib)
            if next_fib >= 10**18:  # handle large inputs
                break
        return fib
    
    fib_numbers = generate_fibonacci()
    prime_fib_numbers = [num for num in fib_numbers if is_prime(num)]
    
    if n <= 0:
        return "Input must be a positive integer"
    elif n <= len(prime_fib_numbers):
        return prime_fib_numbers[n-1]
    else:
        return "Input is too large, please input a smaller number"
import unittest

class Test(unittest.TestCase):
    def test_prime_fib(self):
        self.assertEqual(prime_fib(1), 2)
        self.assertEqual(prime_fib(2), 3)
        self.assertEqual(prime_fib(3), 5)
        self.assertEqual(prime_fib(4), 13)
        self.assertEqual(prime_fib(5), 89)

if __name__ == '__main__':
    unittest.main()