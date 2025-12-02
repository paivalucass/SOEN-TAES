def count_occurrences_of_std(input_string):
    count = 0
    for i in range(len(input_string) - 2):
        if input_string[i:i+3] == 'std':
            count += 1
    return count
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(count_occurance("letstdlenstdporstd"), 3)

if __name__ == '__main__':
    unittest.main()