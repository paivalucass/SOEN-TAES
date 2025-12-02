def heap_sort(iterable):
    n = len(iterable)

    for i in range(n // 2 - 1, -1, -1):
        largest = i
        l = 2 * i + 1
        r = 2 * i + 2

        if l < n and iterable[l] > iterable[largest]:
            largest = l

        if r < n and iterable[r] > iterable[largest]:
            largest = r

        if largest != i:
            iterable[i], iterable[largest] = iterable[largest], iterable[i]

    for i in range(n-1, 0, -1):
        iterable[i], iterable[0] = iterable[0], iterable[i]

        for j in range(i // 2 - 1, -1, -1):
            largest = j
            l = 2 * j + 1
            r = 2 * j + 2

            if l < i and iterable[l] > iterable[largest]:
                largest = l

            if r < i and iterable[r] > iterable[largest]:
                largest = r

            if largest != j:
                iterable[j], iterable[largest] = iterable[largest], iterable[j]

    return iterable
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(heap_sort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0]), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

if __name__ == '__main__':
    unittest.main()