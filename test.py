import unittest
import numpy
from src.scanner import get_qr_from_image

class Tester(unittest.TestCase):
    def test_empty_image(self):
        empty_image = numpy.zeros((100,100,3), dtype = numpy.uint8)
        result = get_qr_from_image(empty_image)
        self.assertIsNone(result)

    def test_phishing_keyword(self):
        trigger_keywords = ['login','verify','acount','password']

        test_url = 'http://example.com/login/verify'

        is_suspicious = any(keyword in test_url.lower() for keyword in trigger_keywords)

        self.assertTrue(is_suspicious)

    def test_safe_url(self):
        trigger_keywords = ['login','verify','acount','password']

        test_url = 'http://github.com'

        is_suspicious = any(keyword in test_url.lower() for keyword in trigger_keywords)

        self.assertFalse(is_suspicious)

    if __name__ == '__main__':
        unittest.main()
