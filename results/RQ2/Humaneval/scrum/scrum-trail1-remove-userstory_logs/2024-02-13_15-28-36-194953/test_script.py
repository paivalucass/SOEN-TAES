def specialFilter(nums):
    if not all(isinstance(x, (int, float)) for x in nums):
        return "Input is not an array of numbers"
    count = 0
    for num in nums:
        if num > 10 and int(str(num)[0]) % 2 != 0 and int(str(num)[-1]) % 2 != 0:
            count += 1
    return count
import unittest

class Test(unittest.TestCase):
    def test_specialFilter(self):
        self.assertEqual(specialFilter([15, -73, 14, -15]), 1)
        self.assertEqual(specialFilter([33, -2, -3, 45, 21, 109]), 2)

if __name__ == '__main__':
    unittest.main()