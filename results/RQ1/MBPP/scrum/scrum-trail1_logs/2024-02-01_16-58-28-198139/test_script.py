def even_position(nums):
    if len(nums) < 2:
        return True
    
    return all(num % 2 == 0 for index, num in enumerate(nums) if index % 2 == 0)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(even_position([3,2,1]), False)

if __name__ == '__main__':
    unittest.main()