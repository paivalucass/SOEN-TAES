def find_Max_Num(arr):
    if not arr or any(not str(x).isdigit() for x in arr):
        return "Invalid input list"

    arr.sort(reverse=True)
    largest_number = int(''.join(map(str, arr)))
    return largest_number
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(find_Max_Num([1, 2, 3]), 321)

if __name__ == '__main__':
    unittest.main()