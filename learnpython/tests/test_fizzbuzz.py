import sys
import os

sys.path.append(os.path.abspath('../learnpython'))

from learnpython import __version__
from learnpython import fizzBuzz


def test_version():
    assert __version__ == '0.1.0'

def test_if_input_list_does_not_have_3_or_5_return_the_list_unmodified():
    input = [1,2,4,6,7,8]
    result = fizzBuzz.fizzBuzz(input)
    assert result == input

def test_if_input_list_has_one_number_which_is_multiple_of_3_replace_number_with_Fizz():
    input = [1,2,4,6,7,8]
    result = fizzBuzz.fizzBuzz(input)
    assert result == [1,2,4,'fizz',7,8]

def test_if_input_list_has_multiple_numbers_which_is_multiple_of_3_replace_number_with_Fizz():
    input = [1,2,4,6,7,3,9]
    result = fizzBuzz.fizzBuzz(input)
    assert result == [1,2,4,'fizz',7,'fizz','fizz']

def test_if_input_list_has_multiple_numbers_which_is_multiple_of_5_replace_number_with_Fizz():
    input = [1,2,4,5,7,3,9]
    result = fizzBuzz.fizzBuzz(input)
    assert result == [1,2,4,'buzz',7,'fizz','fizz']

def test_if_input_list_has_multiple_numbers_which_is_multiple_of_5_and_3_replace_number_with_Fizz():
    input = [1,2,4,5,7,3,9,15,20]
    result = fizzBuzz.fizzBuzz(input)
    assert result == [1,2,4,'buzz',7,'fizz','fizz','fizzbuzz','buzz']