def right_insertion(a, x):
    """
    Write a function to locate the right insertion point for a specified value in sorted order.
    assert right_insertion([1,2,4,5],6)==4
    """
    if not all(a[i] <= a[i + 1] for i in range(len(a) - 1)):
        return -1

    low = 0
    high = len(a)

    while low < high:
        middle = (low + high) // 2
        if a[middle] <= x:
            low = middle + 1
        else:
            high = middle

    return low
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(right_insertion([1,2,4,5],6), 4)

if __name__ == '__main__':
    unittest.main()