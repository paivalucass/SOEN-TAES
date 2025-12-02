def max_product(arr):
    subsequences = []
    current_subsequence = [arr[0]]

    for i in range(1, len(arr)):
        if arr[i] > arr[i-1]:
            current_subsequence.append(arr[i])
        else:
            if len(current_subsequence) > 1:
                subsequences.append(current_subsequence)
            current_subsequence = [arr[i]]

    if len(current_subsequence) > 1:
        subsequences.append(current_subsequence)

    max_product = 0
    for subsequence in subsequences:
        product = 1
        for num in subsequence:
            product *= num
        if product > max_product:
            max_product = product

    return max_product
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(max_product([3, 100, 4, 5, 150, 6]), 3000)

if __name__ == '__main__':
    unittest.main()