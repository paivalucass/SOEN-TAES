def get_max_triples(n):
    count = 0
    arr = [i * i - i + 1 for i in range(1, n + 1)]
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                if (arr[i] + arr[j] + arr[k]) % 3 == 0:
                    count += 1
    return count
# Test Cases:
{
  "test_cases": [
    {
      "Test Title": "Valid Input",
      "Input Data": "n = 5",
      "Expected Output": "1"
    },
    {
      "Test Title": "Edge Case - Minimum Input",
      "Input Data": "n = 1",
      "Expected Output": "0"
    },
    {
      "Test Title": "Edge Case - Maximum Input",
      "Input Data": "n = 1000",
      "Expected Output": "166833"
    },
    {
      "Test Title": "Negative Numbers",
      "Input Data": "n = -5",
      "Expected Output": "5"
    },
    {
      "Test Title": "Large Prime Numbers",
      "Input Data": "n = 997",
      "Expected Output": "166167"
    },
    {
      "Test Title": "Zero Input",
      "Input Data": "n = 0",
      "Expected Output": "0"
    },
    {
      "Test Title": "Non-Numeric Input",
      "Input Data": "n = 'abc'",
      "Expected Output": "Invalid Input"
    }
  ]
}
import unittest

class Test(unittest.TestCase):
    def test_get_max_triples(self):
        self.assertEqual(get_max_triples(5), 1)

if __name__ == '__main__':
    unittest.main()