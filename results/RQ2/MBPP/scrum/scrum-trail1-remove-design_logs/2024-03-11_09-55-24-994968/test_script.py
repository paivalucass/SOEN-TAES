def find_Max_Num(arr):
    if len(arr) == 0:
        return 0
    if all(num < 0 for num in arr):
        return "Error or null"
    arr = [str(num) for num in arr]
    arr.sort(key=lambda x: x*3, reverse=True)
    return int(''.join(arr))
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(find_Max_Num([1,2,3]), 321)

if __name__ == '__main__':
    unittest.main()