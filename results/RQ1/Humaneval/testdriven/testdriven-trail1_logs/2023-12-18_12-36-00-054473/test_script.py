def exchange(lst1, lst2):
    even_count_lst1 = sum(1 for num in lst1 if num % 2 == 0)
    even_count_lst2 = sum(1 for num in lst2 if num % 2 == 0)
    total_even_count = even_count_lst1 + even_count_lst2
    if total_even_count == len(lst1):
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