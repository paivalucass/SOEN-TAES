def differ_At_One_Bit_Pos(num1, num2):
    xor_result = num1 ^ num2
    return bin(xor_result).count('1') == 1

def is_Power_Of_Two(x):
    return x & (x - 1) == 0

# test report:
Test Report:

Test Script Output:
======================================================================
FAIL: test (__main__.Test)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/Users/watch/PycharmProjects/XXXX-1-LLM/workspace/2024-02-01_11-48-05-223987/test_script.py", line 14, in test
    self.assertEqual(is_Power_Of_Two(9), True)
AssertionError: False != True

----------------------------------------------------------------------
Ran 1 test in 0.000s

FAILED (failures=1)

Test Report:
The test script has failed with the following output:
- The test case for is_Power_Of_Two(9) has failed with the assertion error: False != True.

Conclusion:
Code Test Failed. 

Input and Expected Output Example:
Input: is_Power_Of_Two(9)
Expected Output: True

Please review the code to address the failed test case.
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(is_Power_Of_Two(13), False)
        self.assertEqual(is_Power_Of_Two(9), True)

if __name__ == '__main__':
    unittest.main()