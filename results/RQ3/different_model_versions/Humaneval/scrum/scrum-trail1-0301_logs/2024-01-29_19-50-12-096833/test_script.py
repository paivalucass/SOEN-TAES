from typing import List

def factorize(n: int) -> List[int]:
    
    if n <= 1:
        return []
    
    primes = []
    i = 2
    while i * i <= n:
        if n % i != 0:
            i += 1
        else:
            primes.append(i)
            n //= i
    if n > 1:
        primes.append(n)
    
    return primes

# Test Cases:

{
    "requirement analysis": "To ensure that the factorize function works correctly and returns the prime factors of a given integer in the correct order, as well as handling invalid inputs appropriately, the following test cases have been designed:",

    "test_cases": [

        {
            "Test Title": "Test for input 1",
            "Input Data": "1",
            "Expected Output": "[]"
        },

        {
            "Test Title": "Test for input 8",
            "Input Data": "8",
            "Expected Output": "[2,2,2]"
        },

        {
            "Test Title": "Test for input 25",
            "Input Data": "25",
            "Expected Output": "[5,5]"
        },

        {
            "Test Title": "Test for input 70",
            "Input Data": "70",
            "Expected Output": "[2,5,7]"
        },

        {
            "Test Title": "Test for negative input",
            "Input Data": "-10",
            "Expected Output": "Invalid input: n must be a positive integer"
        },

        {
            "Test Title": "Test for non-integer input",
            "Input Data": "3.14",
            "Expected Output": "Invalid input: n must be a positive integer"
        },

        {
            "Test Title": "Test for large input value",
            "Input Data": "100000000",
            "Expected Output": "[2,2,2,2,2,2,2,2,2,5,5,5,5,5,5,5,5,5]"
        },

        {
            "Test Title": "Test for input value that is already a prime number",
            "Input Data": "7",
            "Expected Output": "[7]"
        },

        {
            "Test Title": "Test for input value that is equal to zero",
            "Input Data": "0",
            "Expected Output": "Invalid input: n must be a positive integer"
        }

    ]

}
import unittest
from typing import List

class Test(unittest.TestCase):
    def test_factorize(self):
        self.assertEqual(factorize(8), [2, 2, 2])
        self.assertEqual(factorize(25), [5, 5])
        self.assertEqual(factorize(70), [2, 5, 7])

if __name__ == '__main__':
    unittest.main()