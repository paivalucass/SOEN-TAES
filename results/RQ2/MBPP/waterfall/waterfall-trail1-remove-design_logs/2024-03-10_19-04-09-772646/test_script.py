def find_Max_Num(arr):
    if not arr:
        return "Invalid input"
    if all(num < 0 for num in arr):
        return int(''.join(map(str, arr)))
    max_num = max(arr)
    return int(''.join(map(str, sorted(arr, reverse=True)))) if max_num >= 0 else int(str(max_num) + ''.join(map(str, sorted(filter(lambda x: x != max_num, arr), reverse=True))))
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(find_Max_Num([1,2,3]), 321)

if __name__ == '__main__':
    unittest.main()