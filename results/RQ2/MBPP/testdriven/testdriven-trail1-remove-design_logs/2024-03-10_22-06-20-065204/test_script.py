def median_numbers(a, b, c):
    num_list = [a, b, c]
    num_list.sort()
    if len(num_list) % 2 == 0:
        return (num_list[len(num_list)//2 - 1] + num_list[len(num_list)//2]) / 2.0
    else:
        return num_list[len(num_list)//2]
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(median_numbers(25, 55, 65), 55.0)

if __name__ == '__main__':
    unittest.main()