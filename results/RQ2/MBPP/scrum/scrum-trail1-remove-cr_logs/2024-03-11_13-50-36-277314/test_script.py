def replace_spaces(string):
    return '%20'.join(string.split(' '))
# Test Cases:
{
  "RevisedTestCases": [
    {
      "TestTitle": "Empty String",
      "InputData": "parameter1='',parameter2=''",
      "ExpectedOutput": "''"
    },
    {
      "TestTitle": "String with Multiple Spaces",
      "InputData": "parameter1='My Name is Dawood',parameter2=''",
      "ExpectedOutput": "'My%20Name%20is%20Dawood'"
    },
    {
      "TestTitle": "String with Special Characters",
      "InputData": "parameter1='Special!@#String',parameter2=''",
      "ExpectedOutput": "'Special!@#String'"
    },
    {
      "TestTitle": "Empty Parameter 1",
      "InputData": "parameter1='',parameter2='abc'",
      "ExpectedOutput": "'%20abc'"
    },
    {
      "TestTitle": "Long String",
      "InputData": "parameter1='This is a very long string that exceeds normal limits',parameter2='xyz'",
      "ExpectedOutput": "'This%20is%20a%20very%20long%20string%20that%20exceeds%20normal%20limits%20xyz'"
    },
    {
      "TestTitle": "String with Special Characters Extended",
      "InputData": "parameter1='Special!@#String',parameter2='^&*()'",
      "ExpectedOutput": "'Special!@#String%20^&*()'"
    },
    {
      "TestTitle": "UTF-8 Encoding",
      "InputData": "parameter1='UTF-8 Encoding',parameter2='Test'",
      "ExpectedOutput": "'UTF-8%20Encoding%20Test'"
    },
    {
      "TestTitle": "Non-empty Parameters",
      "InputData": "parameter1='Non-empty',parameter2='Non-empty'",
      "ExpectedOutput": "'Non-empty%20Non-empty'"
    }
  ]
}
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(replace_spaces('My Name is Dawood'), 'My%20Name%20is%20Dawood')

if __name__ == '__main__':
    unittest.main()