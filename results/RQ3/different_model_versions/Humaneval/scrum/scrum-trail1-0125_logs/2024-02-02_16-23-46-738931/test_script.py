def exchange(lst1, lst2):
    sum1 = sum(x % 2 for x in lst1)
    sum2 = sum(x % 2 for x in lst2)
    return 'YES' if sum1 <= sum2 else 'NO'
import unittest

class Test(unittest.TestCase):
    def test_exchange(self):
        self.assertEqual(exchange([1, 2, 3, 4], [1, 2, 3, 4]), "YES")
        self.assertEqual(exchange([1, 2, 3, 4], [1, 5, 3, 4]), "NO")

if __name__ == '__main__':
    unittest.main()