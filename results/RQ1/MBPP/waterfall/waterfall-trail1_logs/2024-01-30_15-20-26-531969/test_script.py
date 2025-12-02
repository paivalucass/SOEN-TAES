def all_Bits_Set_In_The_Given_Range(number, left, right):
    if number < 0 or left < 0 or right < 0:
        raise ValueError("Inputs should be positive integers")

    if left > right:
        raise ValueError("Invalid range: 'left' should be less than or equal to 'right")

    for i in range(left, right+1):
        if number & (1 << i) == 0:
            return False
    return True
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(all_Bits_Set_In_The_Given_Range(4, 1, 2), True)

if __name__ == '__main__':
    unittest.main()