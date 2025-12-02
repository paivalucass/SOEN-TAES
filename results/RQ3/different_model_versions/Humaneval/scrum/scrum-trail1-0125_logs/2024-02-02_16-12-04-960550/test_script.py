def string_sequence(n: int) -> str:
    if not isinstance(n, int) or n < 0:
        return "Invalid input"
    
    return ' '.join(str(i) for i in range(n + 1) if isinstance(i, int))

# Test Cases:
{
    "requirement analysis": "Create test cases for string_sequence function to ensure correctness and accuracy",
    "test_cases": [
        {
            "Test Title": "Test with n=0",
            "Input Data": "n=0",
            "Expected Output": "0"
        },
        {
            "Test Title": "Test with n=5",
            "Input Data": "n=5",
            "Expected Output": "0 1 2 3 4 5"
        },
        {
            "Test Title": "Test with negative number",
            "Input Data": "n=-5",
            "Expected Output": "Invalid input"
        },
        {
            "Test Title": "Test with large number",
            "Input Data": "n=1000",
            "Expected Output": "0 1 2 3 ... 999 1000"
        },
        {
            "Test Title": "Test with string input",
            "Input Data": "n='abc'",
            "Expected Output": "Invalid input"
        },
        {
            "Test Title": "Test with special characters",
            "Input Data": "n=@#$%",
            "Expected Output": "Invalid input"
        }
    ]
}
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(string_sequence(0), '0')
        self.assertEqual(string_sequence(5), '0 1 2 3 4 5')

if __name__ == '__main__':
    unittest.main()