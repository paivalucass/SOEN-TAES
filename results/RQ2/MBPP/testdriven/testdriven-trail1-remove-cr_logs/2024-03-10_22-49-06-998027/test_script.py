def heap_sort(iterable):
    if not iterable:
        return iterable
    
    def heapify(arr, n, i):
        largest = i
        l = 2 * i + 1
        r = 2 * i + 2
        if l < n and arr[i] < arr[l]:
            largest = l
        if r < n and arr[largest] < arr[r]:
            largest = r
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            heapify(arr, n, largest)
    
    n = len(iterable)
    for i in range(n//2 - 1, -1, -1):
        heapify(iterable, n, i)
    for i in range(n-1, 0, -1):
        iterable[i], iterable[0] = iterable[0], iterable[i]
        heapify(iterable, i, 0)
    
    return iterable
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(heap_sort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0]), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

if __name__ == '__main__':
    unittest.main()