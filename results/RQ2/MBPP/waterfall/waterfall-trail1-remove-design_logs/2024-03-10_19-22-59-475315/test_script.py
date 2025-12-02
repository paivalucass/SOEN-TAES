def noprofit_noloss(actual_cost, sale_amount):
    return actual_cost == sale_amount

import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(noprofit_noloss(1500, 1200), False)

if __name__ == '__main__':
    unittest.main()