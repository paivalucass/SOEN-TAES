def extract_quotation(text1):
    import re

    if not isinstance(text1, str):
        raise ValueError("Input text must be a string")

    extracted_values = re.findall(r'\"(.*?)\"', text1)
    return extracted_values
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(extract_quotation('Cortex "A53" Based "multi" tasking "Processor"'), ['A53', 'multi', 'Processor'])

if __name__ == '__main__':
    unittest.main()