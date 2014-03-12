# -*- coding: utf-8 -*-


class ConversionException(Exception):
    """Specialized exception for conversion errors.

    Factory methods encapsulate the creation logic for different types of
    error that can occur during conversions.

    Args:
      message (str): Human readable string describing the exception.

    """
    def __init__(self, message):
        Exception.__init__(self, message)

    @staticmethod
    def for_invalid_id_length():
        return ConversionException("Invalid product ID length")

    @staticmethod
    def for_invalid_id_type():
        return ConversionException("Invalid product ID type")


class IsbnConverter(object):
    """Product ID number to standard ISBN-10 number converter.

    If we take the Da Vinci Code as an example, the product ID is 978140007917
    and the ISBN is 1400079179. The first 3 digits of the product ID (978)
    are a prefix that can be removed. The remaining digits of the product
    ID (140007917) are the digits of the ISBN excluding the error control
    digit.

    Refer to http://www.ee.unb.ca/tervo/ee4243/isbn4243.htm for a description
    of how an ISBN number is constructed.

    """

    _PRODUCT_ID_LENGTH = 12
    _ISBN_10_LENGTH = 10

    def convert_from_product_id(self, product_id):
        """Convert product ID to ISBN-10 number.

        The conversion follows the rules::
          1) The first 3 digits of the product ID are removed;
          2) Remaining digits are ISBN-10 number without error control;
          3) Error control is computed and appended to final number.

        Args:
          product_id (str): Product ID that will be converted.

        Returns:
          str: ISBN-10 number from given product ID.

        Raises:
          ConversionException: In case of errors during conversion business
          logic as invalid product ID.

        """
        self.__validate_product_id(product_id)

        partial_isbn = product_id[3:]
        error_control = self.__compute_error_control(partial_isbn)

        return partial_isbn + error_control

    def __compute_error_control(self, partial_isbn):
        """Compute error control for ISBN-10 numbers.

        The final digit in the ISBN-10 provides an error detection
        capability. It is added once the book number is issued, and, once
        complete, the entire ten digit ISBN-10 can be checked for errors
        whenever it is transcribed.

        The error control digit is computed considering the weighted sum of the
        9 digits of the actual ISBN number and searching for the 10th digit
        satisfying::

            (weighted_sum + control) = 0 mod 11

        Note that the remainder of division by 11 could be any number
        from 0 to 10. If it works out that the value of the final digit must
        be 10, the letter 'x' is used instead to complete the ISBN.

        Args:
          partial_isbn (str): ISBN-10 with missing error control digit.

        Returns:
          str: control error digit for the provided partial ISBN number.

        """
        weighted_sum = 0
        for i, digit in enumerate(partial_isbn):
            # weighted sum of digits
            weighted_sum += (self._ISBN_10_LENGTH - i) * int(digit)

        weighted_sum_mod_11 = (weighted_sum % 11)

        if weighted_sum_mod_11 == 0:
            # not reminder so control should be zero
            control = str(weighted_sum_mod_11)
        else:
            # replace by 'x' when 10 is required as digit
            c_digit = 11 - weighted_sum_mod_11
            control = str(c_digit) if c_digit < self._ISBN_10_LENGTH else "x"

        return control

    def __validate_product_id(self, product_id):
        """Check the validity of product ID.

        The validation method checks the sanity of given product ID, as::
          1) Can be converted to an integer;
          2) Has valid length for conversion.

        Args:
          product_id (str): Product ID that will be converted.

        Raises:
          ConversionException: In case of errors during conversion business
          logic as invalid product ID.

        """
        try:
            int(product_id)
        except ValueError:
            raise ConversionException.for_invalid_id_type()

        if len(product_id) is not self._PRODUCT_ID_LENGTH:
            raise ConversionException.for_invalid_id_length()