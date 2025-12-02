def sort_third(l: list):
    if not isinstance(l, list) or len(l) == 0:
        return "Invalid input"
    
    non_divisible_by_three = [l[i] for i in range(len(l)) if i % 3 != 0]
    divisible_by_three = sorted([l[i] for i in range(len(l)) if i % 3 == 0])

    result = []
    j = 0
    k = 0
    for i in range(len(l)):
        if i % 3 != 0:
            result.append(non_divisible_by_three[j])
            j += 1
        else:
            result.append(divisible_by_three[k])
            k += 1
    
    return result
import unittest

class Test(unittest.TestCase):
    def test_sort_third(self):
        self.assertEqual(sort_third([1, 2, 3]), [1, 2, 3])
        self.assertEqual(sort_third([5, 6, 3, 4, 8, 9, 2]), [2, 6, 3, 4, 8, 9, 5])

if __name__ == '__main__':
    unittest.main()