def find_first_occurrence(A, x):
    if not A or not isinstance(A, list) or not all(isinstance(i, int) for i in A):
        return -1

    if A != sorted(A):
        return -1

    left_index, right_index = 0, len(A) - 1
    result = -1

    while left_index <= right_index:
        middle_index = (left_index + right_index) // 2
        if A[middle_index] == x:
            result = middle_index
            right_index = middle_index - 1
        elif A[middle_index] < x:
            left_index = middle_index + 1
        else:
            right_index = middle_index - 1
    
    return result
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(find_first_occurrence([2, 5, 5, 5, 6, 6, 8, 9, 9, 9], 5), 1)

if __name__ == '__main__':
    unittest.main()