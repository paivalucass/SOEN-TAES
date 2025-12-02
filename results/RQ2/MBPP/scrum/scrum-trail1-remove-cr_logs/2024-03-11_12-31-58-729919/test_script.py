def find_Max_Num(arr):
    if not all(isinstance(x, int) for x in arr):
        return ""
    if len(arr) == 0:
        return ""
    arr.sort(reverse=True)
    result = ''.join(map(str, arr))
    return int(result)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(find_Max_Num([1,2,3]), 321)

if __name__ == '__main__':
    unittest.main()