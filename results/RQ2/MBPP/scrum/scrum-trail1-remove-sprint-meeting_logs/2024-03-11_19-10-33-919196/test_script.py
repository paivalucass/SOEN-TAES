def odd_position(nums):
    try:
        if isinstance(nums, list):
            for i in range(len(nums)):
                if i % 2 != 0 and nums[i] % 2 == 0:
                    return False
            return True
        else:
            raise TypeError
    except TypeError:
        return False
    except IndexError:
        return False

# Updated code
def odd_position(nums):
    try:
        if isinstance(nums, list):
            for i in range(len(nums)):
                if i % 2 != 0 and nums[i] % 2 == 0:
                    return False
            return True
        else:
            raise TypeError
    except TypeError:
        return False
    except IndexError:
        return False

# Example usage
assert odd_position([2,1,4,3,6,7,6,3]) == True
# Test Cases:
{
  "requirement analysis": "Create a Python function called odd_position(nums) that takes in a list of numbers as input.",
  "test_cases": [
    {
      "Test Title": "Input with odd index containing odd numbers",
      "Input Data": "parameter1=[2,1,4,3,6,7,6,3],parameter2='123'",
      "Expected Output": "True"
    },
    {
      "Test Title": "Input with negative numbers",
      "Input Data": "parameter1=[-1,2,-3,4],parameter2='123'",
      "Expected Output": "True"
    },
    {
      "Test Title": "Input with only one number",
      "Input Data": "parameter1=[1],parameter2='123'",
      "Expected Output": "True"
    }
  ]
}
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(odd_position([2, 1, 4, 3, 6, 7, 6, 3]), True)

if __name__ == '__main__':
    unittest.main()