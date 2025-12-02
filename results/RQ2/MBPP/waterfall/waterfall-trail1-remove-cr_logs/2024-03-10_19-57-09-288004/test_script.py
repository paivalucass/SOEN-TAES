def get_total_number_of_sequences(m, n):
    if m < 2 or n < 1:
        return 0
    count = 0
    for i in range(1, m+1):
        count += get_sequences_from_starting_number(i, m, n-1)
    return count

def get_sequences_from_starting_number(start, m, n):
    if n == 0:
        return 1
    count = 0
    for i in range(start*2, m+1):
        count += get_sequences_from_starting_number(i, m, n-1)
    return count

# Test Cases:
{
  "test_cases": [
    {
      "Test Title": "Minimum Input Values",
      "Input Data": "m=1, n=1",
      "Expected Output": "0"
    },
    {
      "Test Title": "Maximum Input Values",
      "Input Data": "m=1000, n=10",
      "Expected Output": "990"
    },
    {
      "Test Title": "Edge Case: m < n",
      "Input Data": "m=3, n=5",
      "Expected Output": "0"
    },
    {
      "Test Title": "Edge Case: n < 1",
      "Input Data": "m=5, n=0",
      "Expected Output": "0"
    }
  ]
}
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(get_total_number_of_sequences(10, 4), 4)

if __name__ == '__main__':
    unittest.main()