def is_Sub_Array(arr, sub_arr):
    for i in range(len(arr) - len(sub_arr) + 1):
        if arr[i:i + len(sub_arr)] == sub_arr:
            return True
    return False
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(is_Sub_Array([1,4,3,5],[1,2]), False)

if __name__ == '__main__':
    unittest.main()