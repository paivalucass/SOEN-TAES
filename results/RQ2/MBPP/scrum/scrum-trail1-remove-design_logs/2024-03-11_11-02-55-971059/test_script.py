def move_zero(num_list):
    count = 0
    n = len(num_list)
    for i in range(n):
        if num_list[i] != 0:
            num_list[count], num_list[i] = num_list[i], num_list[count]
            count += 1
    for i in range(count, n):
        num_list[i] = 0
    return num_list
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(move_zero([1,0,2,0,3,4]), [1,2,3,4,0,0])

if __name__ == '__main__':
    unittest.main()