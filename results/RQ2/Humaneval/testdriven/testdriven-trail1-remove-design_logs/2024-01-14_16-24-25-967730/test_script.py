def exchange(lst1, lst2):
    set1_odd = set([x for x in lst1 if x % 2 != 0])
    set2_odd = set([x for x in lst2 if x % 2 != 0])
    if set1_odd == set2_odd:
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