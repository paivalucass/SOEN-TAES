def even_position(nums):
    for index, num in enumerate(nums):
        if index % 2 == 0 and num % 2 != 0:
            return False
    return True
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(even_position([3,2,1]), False)

if __name__ == '__main__':
    unittest.main()