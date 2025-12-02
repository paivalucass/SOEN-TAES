def is_power_of_2(num):
    return (num & (num - 1)) == 0

def is_Sum_Of_Powers_Of_Two(n):
    if not isinstance(n, int):
        return "Invalid Format"
    if n <= 0:
        return False
    while n > 0:
        if is_power_of_2(n):
            return True
        n = n & (n - 1)
    return False
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(is_Sum_Of_Powers_Of_Two(10), True)

if __name__ == '__main__':
    unittest.main()