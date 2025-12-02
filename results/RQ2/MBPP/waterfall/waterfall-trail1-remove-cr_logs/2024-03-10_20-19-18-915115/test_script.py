from typing import List, Tuple

def new_tuple(test_list: List[str], test_str: str) -> Tuple[str, ...]:
    if not test_list or not test_str:
        raise ValueError("Input parameters cannot be empty")

    result_tuple = tuple(test_list) + (test_str,)
    return result_tuple
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(new_tuple(["WEB", "is"], "best"), ('WEB', 'is', 'best'))

if __name__ == '__main__':
    unittest.main()