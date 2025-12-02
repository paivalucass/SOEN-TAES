def bell_Number(n):
    if n < 0:
        return "Invalid input"
    bell = [[0 for i in range(n+1)] for j in range(n+1)]
    bell[0][0] = 1
    for i in range(1, n+1):
        bell[i][0] = bell[i-1][i-1]
        for j in range(1, i+1):
            bell[i][j] = bell[i-1][j-1] + bell[i][j-1]
    return bell[n][0]

# Test Cases:
{
  "Revised Test Cases": [
    {
      "Test Title": "Test for efficiency",
      "Input Data": "parameter1=5,parameter2=10",
      "Expected Output": "55",
      "Description": "This test case aims to measure the efficiency of the bell_Number function when the input parameters are 5 and 10. Efficiency in this context refers to the time and space complexity of the function. It is important to test for efficiency to ensure that the function can handle larger input values without significant performance degradation."
    },
    {
      "Test Title": "Test for boundary value",
      "Input Data": "parameter1=0,parameter2=1",
      "Expected Output": "1",
      "Details": "The boundary values 0 and 1 are selected to test the behavior of the function at the lower and upper limits of the input range. It is important to test these boundary values as they can often lead to unexpected behavior in the function. Additional test cases should cover scenarios such as negative boundary values and maximum allowed input values."
    },
    {
      "Test Title": "Test for negative value",
      "Input Data": "parameter1=-5,parameter2=-10",
      "Expected Output": "Invalid input"
    },
    {
      "Test Title": "Test for memoization",
      "Input Data": "parameter1=3,parameter2=8",
      "Expected Output": "22"
    }
  ]
}
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(bell_Number(2), 2)

if __name__ == '__main__':
    unittest.main()