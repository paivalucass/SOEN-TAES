def move_zero(num_list):
    num_list.sort(key=lambda x: x == 0)
    return num_list
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(move_zero([1,0,2,0,3,4]), [1,2,3,4,0,0])

if __name__ == '__main__':
    unittest.main()