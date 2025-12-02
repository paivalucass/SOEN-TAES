def triples_sum_to_zero(arr: list) -> bool:
    if len(arr) < 3:
        return False

    arr.sort()  # sort the array

    # loop through the array to find triplets summing to zero
    for i in range(len(arr) - 2):
        if i > 0 and arr[i] == arr[i-1]:  # skip over duplicate elements
            continue
        left = i + 1
        right = len(arr) - 1
        while left < right:
            total = arr[i] + arr[left] + arr[right]
            if total == 0:
                return True
            elif total < 0:
                left += 1
            else:
                right -= 1

    return False
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(triples_sum_to_zero([1, 3, 5, 0]), False)
        self.assertEqual(triples_sum_to_zero([1, 3, -2, 1]), True)
        self.assertEqual(triples_sum_to_zero([1, 2, 3, 7]), False)
        self.assertEqual(triples_sum_to_zero([2, 4, -5, 3, 9, 7]), True)
        self.assertEqual(triples_sum_to_zero([1]), False)

if __name__ == '__main__':
    unittest.main()