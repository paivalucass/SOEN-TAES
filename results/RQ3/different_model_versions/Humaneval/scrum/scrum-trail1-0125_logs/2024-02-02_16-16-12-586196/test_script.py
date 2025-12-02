def modp(n: int, p: int):
    if not isinstance(n, int) or not isinstance(p, int) or n < 0 or p < 0:
        raise ValueError("Inputs must be positive integers")
    
    if n == 0:
        return 1
    if p == 1:
        return 0
    
    result = 1
    base = 2
    n = n % (p - 1)  # Optimization for large n
    
    while n > 0:
        if n % 2 == 1:
            result = (result * base) % p
        base = (base * base) % p
        n //= 2
    
    return result

# Test Cases:
{
    "requirement analysis": "Conduct thorough testing on modp function with various input values",
    "test_cases": [
        {
            "Test Title": "Modulo of positive numbers",
            "Input Data": "parameter1=3,parameter2=5",
            "Expected Output": "3"
        },
        {
            "Test Title": "Modulo of large numbers",
            "Input Data": "parameter1=1101,parameter2=101",
            "Expected Output": "2"
        },
        {
            "Test Title": "Modulo of zero",
            "Input Data": "parameter1=0,parameter2=101",
            "Expected Output": "1"
        },
        {
            "Test Title": "Modulo of numbers with different bases",
            "Input Data": "parameter1=3,parameter2=11",
            "Expected Output": "8"
        },
        {
            "Test Title": "Modulo of numbers with close values",
            "Input Data": "parameter1=100,parameter2=101",
            "Expected Output": "1"
        },
        {
            "Test Title": "Modulo of negative numbers",
            "Input Data": "parameter1=-3,parameter2=5",
            "Expected Output": "2"
        },
        {
            "Test Title": "Modulo of edge cases",
            "Input Data": "parameter1=2147483647,parameter2=2",
            "Expected Output": "1"
        },
        {
            "Test Title": "Modulo of invalid input",
            "Input Data": "parameter1='abc',parameter2=5",
            "Expected Output": "ValueError"
        }
    ]
}
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(modp(3, 5), 3)
        self.assertEqual(modp(1101, 101), 2)
        self.assertEqual(modp(0, 101), 1)
        self.assertEqual(modp(3, 11), 8)
        self.assertEqual(modp(100, 101), 1)

if __name__ == '__main__':
    unittest.main()