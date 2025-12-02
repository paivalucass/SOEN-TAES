def find_Max_Num(arr):
    if not arr:
        raise ValueError("Input array is empty")
    for num in arr:
        if not isinstance(num, int):
            raise ValueError("Input array contains non-numeric values")

    def custom_sort(arr):
        if len(arr) <= 1:
            return arr
        else:
            pivot = arr[0]
            less = [x for x in arr[1:] if x <= pivot]
            greater = [x for x in arr[1:] if x > pivot]
            return custom_sort(greater) + [pivot] + custom_sort(less)

    arr = custom_sort(arr)
    largest_num_str = ''.join(map(str, arr))
    return int(largest_num_str)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(find_Max_Num([1,2,3]), 321)

if __name__ == '__main__':
    unittest.main()