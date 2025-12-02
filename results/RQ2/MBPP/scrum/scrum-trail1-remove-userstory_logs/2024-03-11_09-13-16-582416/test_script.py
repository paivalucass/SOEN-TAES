def remove_uppercase(str1):
    result = ''
    for char in str1:
        if not char.isupper():
            result += char
    return result

# Test Cases:
{
  "test_cases": [
    {
      "Test Title": "Test with all uppercase input",
      "Input Data": "parameter1='ABCDEFGHIJKLMNOPQRSTUVWXYZ'",
      "Expected Output": ""
    },
    {
      "Test Title": "Test with mixed case input",
      "Input Data": "parameter1='cAstyoUrFavoRitETVshoWs'",
      "Expected Output": "cstyoravoitshos"
    },
    {
      "Test Title": "Test with special characters",
      "Input Data": "parameter1='!!!AbCdEfG!!!'",
      "Expected Output": "!!!"
    },
    {
      "Test Title": "Test for boundary values",
      "Input Data": "parameter1='A'",
      "Expected Output": ""
    },
    {
      "Test Title": "Test for edge cases",
      "Input Data": "parameter1=''",
      "Expected Output": ""
    },
    {
      "Test Title": "Test for negative scenario",
      "Input Data": "parameter1='123'",
      "Expected Output": "123"
    }
  ]
}
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(remove_uppercase('cAstyoUrFavoRitETVshoWs'), 'cstyoravoitshos')

if __name__ == '__main__':
    unittest.main()