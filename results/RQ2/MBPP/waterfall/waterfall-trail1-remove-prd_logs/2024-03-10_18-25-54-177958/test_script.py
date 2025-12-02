def find_Max_Num(arr):
    if not all(str(x).isdigit() or str(x).lstrip('-').isdigit() for x in arr) or len(arr) == 0:
        return "Invalid input list"

    if all(x == 0 for x in arr):
        return 0

    sorted_arr = sorted(arr, reverse=True)
    max_number = int(''.join(map(str, sorted_arr)))
    return max_number
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(find_Max_Num([1,2,3]), 321)

if __name__ == '__main__':
    unittest.main()