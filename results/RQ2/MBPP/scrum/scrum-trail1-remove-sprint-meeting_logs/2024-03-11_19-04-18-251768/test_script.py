def extract_quotation(text):
    import re
    if not text:
        return []
    pattern = r"\"(.*?)\""
    return re.findall(pattern, text)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(extract_quotation('Cortex "A53" Based "multi" tasking "Processor"'), ['A53', 'multi', 'Processor'])

if __name__ == '__main__':
    unittest.main()