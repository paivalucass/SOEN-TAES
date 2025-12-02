def count_digit_frequency(n):
    digit_frequency = {}
    for digit in str(n):
        digit_frequency[digit] = digit_frequency.get(digit, 0) + 1
    return digit_frequency

def validate(n):
    if not isinstance(n, int):
        return "Invalid Input"

    digit_frequency = count_digit_frequency(abs(n))
    for digit, frequency in digit_frequency.items():
        if frequency > int(digit):
            return False
    return True

# Test Cases:
{
  "test_cases": [
    {
      "Test Title": "Positive Integer Test",
      "Input Data": "n=1234",
      "Expected Output": "True"
    },
    {
      "Test Title": "Negative Integer Test",
      "Input Data": "n=-1234",
      "Expected Output": "False"
    },
    {
      "Test Title": "Zero Test",
      "Input Data": "n=0",
      "Expected Output": "True"
    },
    {
      "Test Title": "Repeated Digit Test",
      "Input Data": "n=1221",
      "Expected Output": "False"
    },
    {
      "Test Title": "Maximum Positive Integer Test",
      "Input Data": "n=9999999999",
      "Expected Output": "False"
    },
    {
      "Test Title": "Minimum Negative Integer Test",
      "Input Data": "n=-9999999999",
      "Expected Output": "True"
    },
    {
      "Test Title": "Single Digit Test",
      "Input Data": "n=5",
      "Expected Output": "True"
    },
    {
      "Test Title": "Large Number with Multiple Repeated Digits Test",
      "Input Data": "n=1234567890123456",
      "Expected Output": "True"
    },
    {
      "Test Title": "Invalid Input Test",
      "Input Data": "n=a123",
      "Expected Output": "Invalid Input"
    },
    {
      "Test Title": "Special Character Input Test",
      "Input Data": "n=12@34",
      "Expected Output": "Invalid Input"
    }
  ]
}
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(validate(1234), True)

if __name__ == '__main__':
    unittest.main()