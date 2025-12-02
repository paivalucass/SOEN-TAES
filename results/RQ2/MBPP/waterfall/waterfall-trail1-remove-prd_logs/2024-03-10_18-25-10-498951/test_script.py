def differ_At_One_Bit_Pos(num1, num2):
    count = 0
    xor_result = num1 ^ num2
    while xor_result:
        count += xor_result & 1
        xor_result >>= 1
        if count > 1:
            return False
    return count == 1

def is_Power_Of_Two(x):
    power_of_two = x & (x - 1) == 0
    return power_of_two
import unittest

class Test(unittest.TestCase):
    def test_differ_At_One_Bit_Pos(self):
        self.assertEqual(differ_At_One_Bit_Pos(13, 9), True)

if __name__ == '__main__':
    unittest.main()