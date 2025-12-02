def triples_sum_to_zero(l: list):
    if len(l) < 3:
        return False

    l.sort()
    n = len(l)
    for i in range(n-2):
        if i > 0 and l[i] == l[i-1]:
            continue
        left = i + 1
        right = n - 1
        while left < right:
            total = l[i] + l[left] + l[right]
            if total == 0:
                return True
            elif total < 0:
                left += 1
            else:
                right -= 1

    return False
import unittest

class Test(unittest.TestCase):
    def test1(self):
        self.assertEqual(triples_sum_to_zero([1, 3, 5, 0]), False)

    def test2(self):
        self.assertEqual(triples_sum_to_zero([1, 3, -2, 1]), True)

    def test3(self):
        self.assertEqual(triples_sum_to_zero([1, 2, 3, 7]), False)

    def test4(self):
        self.assertEqual(triples_sum_to_zero([2, 4, -5, 3, 9, 7]), True)

    def test5(self):
        self.assertEqual(triples_sum_to_zero([1]), False)

if __name__ == '__main__':
    unittest.main()