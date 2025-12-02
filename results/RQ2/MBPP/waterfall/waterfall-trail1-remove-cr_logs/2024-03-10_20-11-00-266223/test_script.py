def min_swaps(str1, str2):
    arr1 = [int(i) for i in str1]
    arr2 = [int(i) for i in str2]

    swaps = 0
    for i in range(len(arr1)):
        if arr1[i] != arr2[i]:
            for j in range(i+1, len(arr1)):
                if arr1[j] != arr2[j] and arr1[i] == arr2[j] and arr1[j] == arr2[i]:
                    arr1[i], arr1[j] = arr1[j], arr1[i]
                    swaps += 1
                    break
    return swaps
import unittest

class Test(unittest.TestCase):
    def test_min_Swaps(self):
        self.assertEqual(min_Swaps("1101", "1110"), 1)

if __name__ == '__main__':
    unittest.main()