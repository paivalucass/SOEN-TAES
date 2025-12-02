def exchange(lst1, lst2):
    even_count_lst1 = sum(1 for num in lst1 if num % 2 == 0)
    even_count_lst2 = sum(1 for num in lst2 if num % 2 == 0)
    return 'YES' if even_count_lst1 == len(lst1) or even_count_lst2 > 0 else 'NO'
import unittest

class Test(unittest.TestCase):
    def test1(self):
        self.assertEqual(exchange([1, 2, 3, 4], [1, 2, 3, 4]), "YES")

    def test2(self):
        self.assertEqual(exchange([1, 2, 3, 4], [1, 5, 3, 4]), "NO")

if __name__ == '__main__':
    unittest.main()