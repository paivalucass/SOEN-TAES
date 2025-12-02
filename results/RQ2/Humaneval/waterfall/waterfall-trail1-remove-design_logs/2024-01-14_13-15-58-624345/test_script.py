def filter_and_sort(arr):
    if not arr:
        return []

    valid_digits = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    arr = [x for x in arr if x in valid_digits]
    arr.sort()
    arr.reverse()
    return arr

def by_length(arr):
    filtered_and_sorted_arr = filter_and_sort(arr)

    digit_names = ["One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
    result = [digit_names[x-1] for x in filtered_and_sorted_arr]
    
    return result
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(by_length([2, 1, 1, 4, 5, 8, 2, 3]), ["Eight", "Five", "Four", "Three", "Two", "Two", "One", "One"])
        self.assertEqual(by_length([]), [])
        self.assertEqual(by_length([1, -1, 55]), ['One'])

if __name__ == '__main__':
    unittest.main()