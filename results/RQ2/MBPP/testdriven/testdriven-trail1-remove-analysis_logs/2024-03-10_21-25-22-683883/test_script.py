def largest_subset(a):
    if not a:
        return 0
    
    max_subset_size = 0
    unique_elements = set(a)
    unique_elements = sorted(unique_elements)
    n = len(unique_elements)
    max_count = 0
    for i in range(n):
        for j in range(i+1, n):
            if unique_elements[j] % unique_elements[i] == 0:
                count = 1
                k = j
                while k < n:
                    if unique_elements[k] % unique_elements[j] == 0:
                        count += 1
                    k += 1
                max_count = max(max_count, count)
    return max_count
import unittest

class Test(unittest.TestCase):
    def test_largest_subset(self):
        self.assertEqual(largest_subset([1, 3, 6, 13, 17, 18]), 4)

if __name__ == '__main__':
    unittest.main()