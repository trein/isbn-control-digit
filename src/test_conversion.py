import unittest
from conversion import IsbnConverter
from conversion import ConversionException


class IsbnConverterTests(unittest.TestCase):
    """
    Test case for IsbnConverter class.
    """

    def setUp(self):
        """
        Setup converter that will be subjected to the tests.
        """
        self.subject = IsbnConverter()

    def test_invalid_id_type(self):
        """
        Test if invalid product ID type is correctly identified.
        """
        invalid_id_as_string = "na"
        self.assertRaises(ConversionException,
                          self.subject.convert_from_product_id,
                          invalid_id_as_string)

        invalid_id_as_float = "9781551.9237"
        self.assertRaises(ConversionException,
                          self.subject.convert_from_product_id,
                          invalid_id_as_float)

        invalid_id_blended_int = "97815519237a"
        self.assertRaises(ConversionException,
                          self.subject.convert_from_product_id,
                          invalid_id_blended_int)

    def test_invalid_id_length(self):
        """
        Test if invalid product ID length is correctly identified.
        """
        oversized_id = "9781551923709"
        self.assertRaises(ConversionException,
                          self.subject.convert_from_product_id,
                          oversized_id)

        undersized_id = "978155192"
        self.assertRaises(ConversionException,
                          self.subject.convert_from_product_id,
                          undersized_id)

    def test_isbn_conversion_with_error_control_over_10(self):
        """
        Test if valid product ID is correctly converted to ISBN-10 when
        computed error control is over 10.
        """
        product_id_1 = "978155192370"
        expected_isbn_1 = "155192370x"
        self.assertEqual(self.subject.convert_from_product_id(product_id_1),
                         expected_isbn_1)

        product_id_2 = "978007007013"
        expected_isbn_2 = "007007013x"
        self.assertEqual(self.subject.convert_from_product_id(product_id_2),
                         expected_isbn_2)

    def test_isbn_conversion_with_error_control_under_10(self):
        """
        Test if valid product ID is correctly converted to ISBN-10 when
        computed error control is under 10.
        """
        product_id_1 = "978140007917"
        expected_isbn_1 = "1400079179"
        self.assertEqual(self.subject.convert_from_product_id(product_id_1),
                         expected_isbn_1)

        product_id_2 = "978037541457"
        expected_isbn_2 = "0375414576"
        self.assertEqual(self.subject.convert_from_product_id(product_id_2),
                         expected_isbn_2)

        product_id_3 = "978037428158"
        expected_isbn_3 = "0374281580"
        self.assertEqual(self.subject.convert_from_product_id(product_id_3),
                         expected_isbn_3)

        product_id_4 = "978155512010"
        expected_isbn_4 = "1555120105"
        self.assertEqual(self.subject.convert_from_product_id(product_id_4),
                         expected_isbn_4)


if __name__ == '__main__':
    unittest.main()