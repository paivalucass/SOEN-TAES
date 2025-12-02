def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def x_or_y(n, x, y):
    try:
        if not isinstance(n, int) or not isinstance(x, int) or not isinstance(y, int):
            raise ValueError("Input values must be integers")
        
        if n <= 0:
            raise ValueError("n must be a positive integer")

        if is_prime(n):
            return x
        else:
            return y
    except ValueError as ve:
        return str(ve)

# Testing the code with sample inputs
print(x_or_y(7, 34, 12))  # Output: 34
print(x_or_y(15, 8, 5))   # Output: 5

# Test Cases:
{
  "test_cases": [
    {
      "Test Title": "Prime Number Input",
      "Input Data": "n=7, x=34, y=12",
      "Expected Output": "34"
    },
    {
      "Test Title": "Non-Prime Number Input",
      "Input Data": "n=15, x=8, y=5",
      "Expected Output": "5"
    },
    {
      "Test Title": "Negative Number Input",
      "Input Data": "n=-5, x=3, y=9",
      "Expected Output": "9"
    },
    {
      "Test Title": "Zero Input",
      "Input Data": "n=0, x=2, y=6",
      "Expected Output": "6"
    },
    {
      "Test Title": "Prime Number with Multiple Factors",
      "Input Data": "n=77, x=15, y=30",
      "Expected Output": "30"
    },
    {
      "Test Title": "Large Input Number",
      "Input Data": "n=999999, x=100, y=200",
      "Expected Output": "200"
    },
    {
      "Test Title": "Input Number Close to Prime",
      "Input Data": "n=11, x=40, y=50",
      "Expected Output": "40"
    },
    {
      "Test Title": "One as Prime Number",
      "Input Data": "n=1, x=60, y=70",
      "Expected Output": "70"
    },
    {
      "Test Title": "Negative Prime Number",
      "Input Data": "n=-2, x=80, y=90",
      "Expected Output": "80"
    }
  ]
}
import unittest

class Test(unittest.TestCase):
    def test1(self):
        self.assertEqual(x_or_y(7, 34, 12), 34)

    def test2(self):
        self.assertEqual(x_or_y(15, 8, 5), 5)

if __name__ == '__main__':
    unittest.main()