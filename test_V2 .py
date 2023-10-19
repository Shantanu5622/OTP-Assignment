import validate_otp_V2 as otp
import pytest
import unittest
from validate_otp_V2 import validateEmail, generateOTP, send_email


class TestProgramFunctions(unittest.TestCase):

    def test_validateEmail(self):

        result = validateEmail("shantanumetkari331@gmail.com")
        expected = True
        self.assertEqual(result, expected)

        result = validateEmail("metkarishantanu2@gmail.com")
        expected = True
        self.assertEqual(result, expected)

    def test_generateOTP(self):
        otp = generateOTP()
        self.assertEqual(len(otp), 4)
        self.assertTrue(otp.isdigit())


if __name__ == '__main__':
    pytest.main()
