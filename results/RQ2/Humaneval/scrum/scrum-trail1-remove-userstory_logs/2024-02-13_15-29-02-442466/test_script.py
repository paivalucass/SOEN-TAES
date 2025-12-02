def get_max_triples(n):
    count = 0
    for i in range(1, n+1):
        a_i = i * i - i + 1
        for j in range(i+1, n+1):
            a_j = j * j - j + 1
            for k in range(j+1, n+1):
                a_k = k * k - k + 1
                if (a_i + a_j + a_k) % 3 == 0:
                    count += 1
    return count

# Rewritten Code:
def get_max_triples(n):
    count = 0
    for i in range(1, n+1):
        a_i = i * i - i + 1
        for j in range(i+1, n+1):
            a_j = j * j - j + 1
            for k in range(j+1, n+1):
                a_k = k * k - k + 1
                if (a_i + a_j + a_k) % 3 == 0:
                    count += 1
    return count

# Test Cases:
{
  "test_cases": [
    {
      "Test Title": "Valid input - first scenario",
      "Input Data": "n = 5",
      "Expected Output": "1"
    },
    {
      "Test Title": "Edge case - minimum input - second scenario",
      "Input Data": "n = 1",
      "Expected Output": "0"
    },
    {
      "Test Title": "Large input - third scenario",
      "Input Data": "n = 1000",
      "Expected Output": "166167000"
    },
    {
      "Test Title": "Negative input",
      "Input Data": "n = -5",
      "Expected Output": "0"
    },
    {
      "Test Title": "Zero input",
      "Input Data": "n = 0",
      "Expected Output": "0"
    },
    {
      "Test Title": "Large negative input",
      "Input Data": "n = -1000",
      "Expected Output": "-166167000"
    },
    {
      "Test Title": "Prime numbers",
      "Input Data": "n = 7",
      "Expected Output": "4"
    },
    {
      "Test Title": "Even numbers",
      "Input Data": "n = 8",
      "Expected Output": "9"
    },
    {
      "Test Title": "Odd numbers",
      "Input Data": "n = 9",
      "Expected Output": "14"
    }
  ]
}
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(get_max_triples(5), 1)

if __name__ == '__main__':
    unittest.main()