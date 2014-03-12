#!/usr/bin/python
"""Product ID number to standard ISBN-10 number converter.

This module executes a simple product ID number to standard ISBN-10 number
converter capturing the input from STDIN and displaying the result on STDOUT.

Example:
    $ python main.py

    Product ID to be converted: 978155192370
    Resulting ISBN-10: 155192370x

"""
from source import conversion


PRODUCT_ID_INPUT_MESSAGE = "Enter the product ID to be converted: "
ISBN_RESULT_MESSAGE = "Resulting ISBN-10: %s"
ISBN_ERROR_MESSAGE = "An error occurred during ISBN-10 conversion: %s"


def execute_conversion():
    """Capture input from STDIN and display the conversion result on STDOUT.

    The input product ID number is converted to a ISBN-10 number. If the
    conversion does not succeed, an error message is presented on STDOUT
    explaining the reason.

    Example:
      >>> execute_conversion()
      Enter the product ID to be converted: 978155192370
      Resulting ISBN-10: 155192370x

      >>> execute_conversion()
      Enter the product ID to be converted: na
      An error occurred during ISBN-10 conversion: Invalid product ID

    """
    isbn_converter = conversion.IsbnConverter()
    product_id = raw_input(PRODUCT_ID_INPUT_MESSAGE)
    result_message = ""

    try:
        isbn = isbn_converter.convert_from_product_id(product_id)
        result_message = ISBN_RESULT_MESSAGE % isbn
    except conversion.ConversionException, e:
        result_message = ISBN_ERROR_MESSAGE % e.message

    print result_message


if __name__ == '__main__':
    execute_conversion()