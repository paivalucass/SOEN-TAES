def find_kth(arr1, arr2, k):
    def merge(arr1, arr2):
        result = []
        i = 0
        j = 0
        while i < len(arr1) and j < len(arr2):
            if arr1[i] < arr2[j]:
                result.append(arr1[i])
                i += 1
            else:
                result.append(arr2[j])
                j += 1
        result += arr1[i:]
        result += arr2[j:]
        return result

    def find_kth_element(arr1, arr2, k):
        merged = merge(arr1, arr2)
        if k < 1 or k > len(merged):
            return "Invalid input"
        return merged[k-1]

    return find_kth_element(arr1, arr2, k)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(find_kth([2, 3, 6, 7, 9], [1, 4, 8, 10], 5), 6)

if __name__ == '__main__':
    unittest.main()