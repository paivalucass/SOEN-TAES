def simplify(x: str, n: str) -> bool:
    x_num, x_den = map(int, x.split('/'))
    n_num, n_den = map(int, n.split('/'))
    result = (x_num * n_num) % (x_den * n_den)
    return result == 0

# Test Cases:
{
  "test_cases": [
    {
      "Test Title": "Valid Fractions",
      "Input Data": "parameter1='1/5', parameter2='5/1'",
      "Expected Output": "True"
    },
    {
      "Test Title": "Invalid Fractions",
      "Input Data": "parameter1='1/6', parameter2='2/1'",
      "Expected Output": "False"
    },
    {
      "Test Title": "Edge Case - Same Numerator",
      "Input Data": "parameter1='2/3', parameter2='2/5'",
      "Expected Output": "False"
    },
    {
      "Test Title": "Edge Case - Same Denominator",
      "Input Data": "parameter1='3/4', parameter2='2/4'",
      "Expected Output": "True"
    },
    {
      "Test Title": "Non-numeric Input Data",
      "Input Data": "parameter1='1/a', parameter2='b/1'",
      "Expected Output": "False"
    },
    {
      "Test Title": "Empty Input Data",
      "Input Data": "parameter1='', parameter2='5/1'",
      "Expected Output": "False"
    },
    {
      "Test Title": "Input Data with Larger Numbers",
      "Input Data": "parameter1='10/5', parameter2='100/20'",
      "Expected Output": "True"
    },
    {
      "Test Title": "Special Character Input Data",
      "Input Data": "parameter1='1/@', parameter2='5/$'",
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