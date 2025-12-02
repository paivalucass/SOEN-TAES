def exchange(lst1, lst2):
    odds_lst1 = [i for i in lst1 if i % 2 != 0]
    evens_lst2 = [i for i in lst2 if i % 2 == 0]

    if len(odds_lst1) <= len(evens_lst2):
        return "YES"
    else:
        return "NO"
import unittest

class Test(unittest.TestCase):
    def test_exchange(self):
        self.assertEqual(exchange([1, 2, 3, 4], [1, 2, 3, 4]), "YES")
        self.assertEqual(exchange([1, 2, 3, 4], [1, 5, 3, 4]), "NO")

if __name__ == '__main__':
    unittest.main()