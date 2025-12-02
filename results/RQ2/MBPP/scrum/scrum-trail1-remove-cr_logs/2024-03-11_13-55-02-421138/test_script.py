def extract_quotation(text1):
    import re
    try:
        return re.findall(r'\"(.*?)\"', text1)
    except:
        return []
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(extract_quotation('Cortex "A53" Based "multi" tasking "Processor"'), ['A53', 'multi', 'Processor'])

if __name__ == '__main__':
    unittest.main()