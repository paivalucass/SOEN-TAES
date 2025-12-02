def exchange(lst1, lst2):
    total_sum = sum(lst1) + sum(lst2)
    if total_sum % 2 == 0:
        return "YES"
    else:
        return "NO"
import unittest

class Test(unittest.TestCase):
    def test1(self):
        self.assertEqual(exchange([1, 2, 3, 4], [1, 2, 3, 4]), "YES")

    def test2(self):
        self.assertEqual(exchange([1, 2, 3, 4], [1, 5, 3, 4]), "NO")

if __name__ == '__main__':
    unittest.main()