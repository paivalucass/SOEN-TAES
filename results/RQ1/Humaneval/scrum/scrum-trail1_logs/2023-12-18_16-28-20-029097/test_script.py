def simplify(x, n):
    numerator_x, denominator_x = map(int, x.split('/'))
    numerator_n, denominator_n = map(int, n.split('/'))

    result = numerator_x * numerator_n / (denominator_x * denominator_n)

    return result % 1 == 0

# Test Cases:
{
  "test_cases": [
    {
      "Test Title": "Simplify Whole Number",
      "Input Data": "parameter1=1/5,parameter2=5/1",
      "Expected Output": "True"
    },
    {
      "Test Title": "Simplify Non Whole Number",
      "Input Data": "parameter1=1/6,parameter2=2/1",
      "Expected Output": "False"
    },
    {
      "Test Title": "Simplify Mixed Fractions",
      "Input Data": "parameter1=7/10,parameter2=10/2",
      "Expected Output": "False"
    }
  ]
}
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(simplify("1/5", "5/1"), True)
        self.assertEqual(simplify("1/6", "2/1"), False)
        self.assertEqual(simplify("7/10", "10/2"), False)

if __name__ == '__main__':
    unittest.main()