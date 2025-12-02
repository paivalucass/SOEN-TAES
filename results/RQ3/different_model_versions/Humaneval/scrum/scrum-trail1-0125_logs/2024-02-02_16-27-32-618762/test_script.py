# Rewritten Code:

def is_positive_even_number(num):
    return num % 2 == 0 and num > 0

def get_even_numbers(n):
    return [num for num in range(2, n + 1, 2)]

def sum_even_numbers(numbers):
    return sum(numbers)

def is_equal_to_sum_even(n):
    if n < 8:
        return False
    even_numbers = get_even_numbers(n)
    for i in range(len(even_numbers)):
        for j in range(i, len(even_numbers)):
            for k in range(j, len(even_numbers)):
                for l in range(k, len(even_numbers)):
                    if even_numbers[i] + even_numbers[j] + even_numbers[k] + even_numbers[l] == n:
                        return True
    return False

# Test Cases:
{
    "test_cases": [
        {
            "Test Title": "Positive even number check",
            "Input Data": "n=4",
            "Expected Output": "False"
        },
        {
            "Test Title": "Even numbers retrieval",
            "Input Data": "n=8",
            "Expected Output": "[2, 4, 6, 8]"
        },
        {
            "Test Title": "Sum of even numbers calculation",
            "Input Data": "numbers=[2, 4, 6, 8]",
            "Expected Output": "20"
        },
        {
            "Test Title": "Negative input number",
            "Input Data": "n=-4",
            "Expected Output": "False"
        },
        {
            "Test Title": "Zero input number",
            "Input Data": "n=0",
            "Expected Output": "False"
        },
        {
            "Test Title": "Non-integer input number",
            "Input Data": "n=3.5",
            "Expected Output": "False"
        },
        {
            "Test Title": "Very large input number",
            "Input Data": "n=1000000",
            "Expected Output": "False"
        },
        {
            "Test Title": "Very small input number",
            "Input Data": "n=0.0001",
            "Expected Output": "False"
        }
    ]
}
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(is_equal_to_sum_even(4), False)
        self.assertEqual(is_equal_to_sum_even(6), False)
        self.assertEqual(is_equal_to_sum_even(8), True)

if __name__ == '__main__':
    unittest.main()