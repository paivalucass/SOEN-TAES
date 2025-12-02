def rearrange_bigger(n):
    if not isinstance(n, int) or n < 0:  # Step 1
        return "Error: Input is not a valid integer or is negative"

    digits = [int(d) for d in str(n)]  # Step 2

    # Steps 3-7
    for i in range(len(digits)-2, -1, -1):
        if digits[i] < digits[i+1]:
            j = next((j for j in range(len(digits)-1, i, -1) if digits[j] > digits[i]), None)
            if j is not None:
                digits[i], digits[j] = digits[j], digits[i]
                digits[i+1:] = sorted(digits[i+1:])
                return int(''.join(map(str, digits)))

    return n  # Step 4
# Test Cases:
{
  "requirement analysis": "Analysis",
  "test_cases": [
    {
      "Test Title": "Valid input",
      "Input Data": "parameter1=12",
      "Expected Output": "21"
    },
    {
      "Test Title": "Negative input",
      "Input Data": "parameter1=-12",
      "Expected Output": "Error: Input is not a valid integer or is negative"
    },
    {
      "Test Title": "Large input number",
      "Input Data": "parameter1=1234567890",
      "Expected Output": "1234567908"
    },
    {
      "Test Title": "Boundary values",
      "Input Data": "parameter1=0",
      "Expected Output": "Error: Input is not a valid integer or is negative"
    },
    {
      "Test Title": "Special characters",
      "Input Data": "parameter1=12@#$%",
      "Expected Output": "Error: Input is not a valid integer or is negative"
    },
    {
      "Test Title": "Null input",
      "Input Data": "parameter1=",
      "Expected Output": "Error: Input is not a valid integer or is negative"
    },
    {
      "Test Title": "Invalid input format",
      "Input Data": "parameter1=abc",
      "Expected Output": "Error: Input is not a valid integer or is negative"
    }
  ]
}
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(rearrange_bigger(12), 21)

if __name__ == '__main__':
    unittest.main()