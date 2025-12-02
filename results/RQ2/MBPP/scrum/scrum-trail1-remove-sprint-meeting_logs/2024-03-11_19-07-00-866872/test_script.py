def min_k(test_list, K):
    import heapq
    result = []
    heapq.heapify(test_list)
    for i in range(K):
        result.append(heapq.heappop(test_list))
    return result
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(min_k([('Manjeet', 10), ('Akshat', 4), ('Akash', 2), ('Nikhil', 8)], 2), [('Akash', 2), ('Akshat', 4)])

if __name__ == '__main__':
    unittest.main()