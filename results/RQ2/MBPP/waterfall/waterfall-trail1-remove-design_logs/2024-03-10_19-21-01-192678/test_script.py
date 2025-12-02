def find_kth(arr1, arr2, k):
    import heapq
    if not arr1 or not arr2:
        return "Error: Empty arrays"
    if k > len(arr1) + len(arr2):
        return "Error: k out of range"

    min_heap = []
    for num in arr1:
        heapq.heappush(min_heap, num)
    for num in arr2:
        heapq.heappush(min_heap, num)
    
    kth_element = None
    for _ in range(k):
        kth_element = heapq.heappop(min_heap)
    
    return kth_element
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(find_kth([2, 3, 6, 7, 9], [1, 4, 8, 10], 5), 6)

if __name__ == '__main__':
    unittest.main()