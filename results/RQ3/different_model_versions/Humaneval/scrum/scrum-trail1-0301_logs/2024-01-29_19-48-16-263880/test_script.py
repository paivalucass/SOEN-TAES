def greatest_common_divisor(a: int, b: int) -> int:
    """ Return a greatest common divisor of two integers a and b
    >>> greatest_common_divisor(10, 15)
    5
    """
    if a == 0:
        return "Invalid input. parameter1 must be a non-zero integer value."
    while b != 0:
        a, b = b, a % b
    return abs(a)

# Test Cases:
{
    "requirement analysis": "test cases for greatest_common_divisor function",
    "test_cases": [
        {
            "Test Title": "Positive integers test case",
            "Input Data": "parameter1=10,parameter2=15",
            "Expected Output": "5"
        },
        {
            "Test Title": "Zero input test case",
            "Input Data": "parameter1=0,parameter2=20",
            "Expected Output": "Invalid input. parameter1 must be a non-zero integer value."
        },
        {
            "Test Title": "Negative integers test case",
            "Input Data": "parameter1=-8,parameter2=-12",
            "Expected Output": "4"
        },
        {
            "Test Title": "Non-integer input test case",
            "Input Data": "parameter1=5.5,parameter2=10",
            "Expected Output": "Invalid input. parameter1 must be a non-zero integer value."
        },
        {
            "Test Title": "Large input test case",
            "Input Data": "parameter1=1000000,parameter2=2500000",
            "Expected Output": "500000"
        },
        {
            "Test Title": "Edge case: smallest possible input values",
            "Input Data": "parameter1=-2147483648,parameter2=1",
            "Expected Output": "1"
        },
        {
            "Test Title": "Edge case: largest possible input values",
            "Input Data": "parameter1=2147483647,parameter2=2147483647",
            "Expected Output": "2147483647"
        },
        {
            "Test Title": "Edge case: one input as 0 and the other as a non-zero integer",
            "Input Data": "parameter1=0,parameter2=12345678",
            "Expected Output": "Invalid input. parameter1 must be a non-zero integer value."
        },
        {
            "Test Title": "Edge case: very large numbers to test performance",
            "Input Data": "parameter1=9999999,parameter2=99999999",
            "Expected Output": "9"
        },
        {
            "Test Title": "Edge case: prime numbers",
            "Input Data": "parameter1=17,parameter2=19",
            "Expected Output": "1"
        }
    ]
}
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(greatest_common_divisor(3, 5), 1)
        self.assertEqual(greatest_common_divisor(25, 15), 5)

if __name__ == '__main__':
    unittest.main()