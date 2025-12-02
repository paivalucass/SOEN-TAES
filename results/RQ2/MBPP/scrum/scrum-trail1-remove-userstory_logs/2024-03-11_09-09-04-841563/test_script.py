def find_Parity(inputNumber: int) -> bool:
    if not isinstance(inputNumber, int):
        raise ValueError("Input is not an integer")
    if inputNumber < 0:
        raise ValueError("Input cannot be a negative number")
    return inputNumber % 2 != 0

# Test Cases:
{
  "requirement analysis": "Identify the requirements and expected behavior of the find_Parity function",
  "test_cases": [
    {
      "Test Title": "Test for even number",
      "Input Data": "parameter1=12",
      "Expected Output": "False"
    },
    {
      "Test Title": "Test for odd number",
      "Input Data": "parameter1=15",
      "Expected Output": "True"
    },
    {
      "Test Title": "Test for zero",
      "Input Data": "parameter1=0",
      "Expected Output": "False"
    },
    {
      "Test Title": "Test for negative number",
      "Input Data": "parameter1=-5",
      "Expected Output": "True"
    },
    {
      "Test Title": "Test for largest even number",
      "Input Data": "parameter1=9223372036854775806",
      "Expected Output": "False"
    },
    {
      "Test Title": "Test for largest odd number",
      "Input Data": "parameter1=9223372036854775807",
      "Expected Output": "True"
    },
    {
      "Test Title": "Test for smallest negative number",
      "Input Data": "parameter1=-9223372036854775807",
      "Expected Output": "True"
    },
    {
      "Test Title": "Test for invalid input",
      "Input Data": "parameter1='abc'",
      "Expected Output": "Error"
    }
  ]
}
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(find_Parity(12), False)

if __name__ == '__main__':
    unittest.main()