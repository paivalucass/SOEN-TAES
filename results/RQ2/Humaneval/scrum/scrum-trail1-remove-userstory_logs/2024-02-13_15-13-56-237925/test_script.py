def add(lst):
    total_sum = 0  
    for i in range(1, len(lst), 2):  
        if lst[i] % 2 == 0:  
            total_sum += lst[i]  
    return total_sum  

# Test Cases:
{
  "requirement analysis": "add function to cover odd indices with even elements",
  "test_cases": [
    {
      "Test Title": "empty input list",
      "Input Data": "parameter1=[],parameter2=''",
      "Expected Output": "0"
    },
    {
      "Test Title": "no even elements at odd indices",
      "Input Data": "parameter1=[1,3,5],parameter2=''",
      "Expected Output": "0"
    },
    {
      "Test Title": "both even and odd elements at odd indices",
      "Input Data": "parameter1=[1,2,3,4,5],parameter2=''",
      "Expected Output": "6"
    },
    {
      "Test Title": "input list containing negative numbers",
      "Input Data": "parameter1=[-2, 1, -4, 3, 5],parameter2=''",
      "Expected Output": "-3"
    },
    {
      "Test Title": "input list containing zero",
      "Input Data": "parameter1=[0, 1, 0, 3, 5],parameter2=''",
      "Expected Output": "1"
    },
    {
      "Test Title": "input list containing duplicate elements",
      "Input Data": "parameter1=[2, 2, 4, 3, 5],parameter2=''",
      "Expected Output": "5"
    }
  ]
}
import unittest

class Test(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add([4, 2, 6, 7]), 2)

if __name__ == '__main__':
    unittest.main()