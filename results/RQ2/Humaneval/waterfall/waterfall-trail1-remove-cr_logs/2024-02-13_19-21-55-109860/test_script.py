def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def is_multiply_prime(a):
    if a <= 0 or a >= 100:
        return False
    
    prime_count = 0
    for i in range(2, a):
        if is_prime(i) and a % i == 0:
            prime_count += 1
            if prime_count > 3:
                return False
    
    return prime_count == 3

# Test cases
print(is_multiply_prime(30)) # Output: True
print(is_multiply_prime(24)) # Output: False
print(is_multiply_prime(0))  # Output: False
print(is_multiply_prime(101)) # Output: False

# Test Cases:
{
  "test_cases": [
    {
      "Test Title": "Input number is the multiplication of 3 prime numbers",
      "Input Data": "parameter1=30",
      "Expected Output": "True"
    },
    {
      "Test Title": "Input number is not the multiplication of 3 prime numbers",
      "Input Data": "parameter1=25",
      "Expected Output": "False"
    },
    {
      "Test Title": "Input number is a prime number",
      "Input Data": "parameter1=7",
      "Expected Output": "False"
    },
    {
      "Test Title": "Input number is 0",
      "Input Data": "parameter1=0",
      "Expected Output": "False"
    },
    {
      "Test Title": "Input number is negative",
      "Input Data": "parameter1=-10",
      "Expected Output": "False"
    },
    {
      "Test Title": "Boundary value analysis - Very large prime numbers",
      "Input Data": "parameter1=97",
      "Expected Output": "False"
    },
    {
      "Test Title": "Boundary value analysis - Input numbers close to data type limits",
      "Input Data": "parameter1=99",
      "Expected Output": "False"
    }
  ]
}
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(is_multiply_prime(30), True)

if __name__ == '__main__':
    unittest.main()