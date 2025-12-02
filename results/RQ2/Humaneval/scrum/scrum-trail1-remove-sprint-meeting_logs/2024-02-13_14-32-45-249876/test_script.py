def is_prime(num: int) -> bool:
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def prime_fib(n: int) -> int:
    if not isinstance(n, int) or n < 1:
        raise ValueError("Input must be a positive integer")
    
    fib_numbers = [0, 1]
    prime_fibs = []

    for i in range(2, n * 5):  # Generate Fibonacci numbers up to a limit
        next_num = fib_numbers[-1] + fib_numbers[-2]
        fib_numbers.append(next_num)
    
    for num in fib_numbers:
        if is_prime(num):
            prime_fibs.append(num)
        if len(prime_fibs) == n:
            break

    return prime_fibs[-1]  # Return the nth prime Fibonacci number

# Test cases
if __name__ == "__main__":
    import doctest
    doctest.testmod()

# Test Cases:
{
  "requirement analysis": "design and implement a function called prime_fib that takes an integer n as input and returns the n-th number that is both a Fibonacci number and a prime number",
  "test_cases": [
    {
      "Test Title": "Valid Input",
      "Input Data": "n=1",
      "Expected Output": "2"
    },
    {
      "Test Title": "Valid Input",
      "Input Data": "n=3",
      "Expected Output": "5"
    },
    {
      "Test Title": "Valid Input",
      "Input Data": "n=5",
      "Expected Output": "89"
    },
    {
      "Test Title": "Edge Case",
      "Input Data": "n=0",
      "Expected Output": "Error: Invalid input"
    },
    {
      "Test Title": "Edge Case",
      "Input Data": "n=2",
      "Expected Output": "3"
    }
  ]
}
import unittest

class Test(unittest.TestCase):
    def test_prime_fib_1(self):
        self.assertEqual(prime_fib(1), 2)

    def test_prime_fib_2(self):
        self.assertEqual(prime_fib(2), 3)

    def test_prime_fib_3(self):
        self.assertEqual(prime_fib(3), 5)

    def test_prime_fib_4(self):
        self.assertEqual(prime_fib(4), 13)

    def test_prime_fib_5(self):
        self.assertEqual(prime_fib(5), 89)

if __name__ == '__main__':
    unittest.main()