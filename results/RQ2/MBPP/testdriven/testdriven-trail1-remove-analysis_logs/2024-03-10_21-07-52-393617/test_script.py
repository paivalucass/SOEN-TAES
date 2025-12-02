def find_Max_Num(arr):
    arr.sort(reverse=True)
    return int(''.join(map(str, arr)))
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(find_Max_Num([1,2,3]), 321)

if __name__ == '__main__':
    unittest.main()