# ISBN-10 Control Digit
The assignment is to code an application that can convert a product ID number to a standard ISBN-10 number.If we take the Da Vinci Code as an example, the product ID is `978140007917` and the ISBN is `1400079179`. The first 3 digits of the product ID (`978`) are a prefix that can be removed. The remaining digits of the product ID (`140007917`) are the digits of the ISBN excluding the error control digit. Refer to [this](http://www.ee.unb.ca/tervo/ee4243/isbn4243.htm) for a description of how an ISBN number is constructed.
Your task is to develop an application that can accept a product ID number and generate the ISBN-10 number. You can choose how you wish to develop the application (console, windows forms or web application) but the code should be in one of Python, C, C++, C#, or Java.
The code will be reviewed for algorithm design and coding standards. Sample test cases:
| Product ID    | ISBN      
| --------------|-----------| 978155192370  | 155192370x| 978140007917  | 1400079179| 978037541457  | 0375414576| 978037428158  | 0374281580


### Solution

The proposed problems were solved using Python `v2.7.5`. The current implementation follows [Google Style Python]
(http://google-styleguide.googlecode.com/svn/trunk/pyguide.html).

#### Contents:
 - `src/converter.py`: ISBN-10 converter implementation
 - `src/test_converter.py`: ISBN-10 converter unit tests
 - `main.py`: Command line interface for ISBN-10 converter

#### Running the application
    $ python main.py

#### Running the unit tests
    $ python src/test_conversion.py