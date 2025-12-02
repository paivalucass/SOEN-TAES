def sort_third(l: list):
    def quicksort(arr):
        if len(arr) <= 1:
            return arr
        else:
            pivot = arr[0]
            less = [x for x in arr[1:] if x <= pivot]
            greater = [x for x in arr[1:] if x > pivot]
            return quicksort(less) + [pivot] + quicksort(greater)
    
    l_prime = l.copy()
    divisible_by_three = [l[i] for i in range(len(l)) if i % 3 == 0]
    sorted_divisible = quicksort(divisible_by_three)
    j = 0
    for i in range(len(l)):
        if i % 3 == 0:
            l_prime[i] = sorted_divisible[j]
            j += 1
    return l_prime
import unittest

class Test(unittest.TestCase):
    def test_sort_third(self):
        self.assertEqual(sort_third([1, 2, 3]), [1, 2, 3])
        self.assertEqual(sort_third([5, 6, 3, 4, 8, 9, 2]), [2, 6, 3, 4, 8, 9, 5])

if __name__ == '__main__':
    unittest.main()