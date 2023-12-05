import sys
import os

sys.path.append(os.path.abspath('../learnpython'))

from learnpython import __version__
from learnpython import day1

def test_case1():
    input = "1abc2"
    expected_result = 12
    result = day1.process_string(input)
    assert result == expected_result 

def test_case2():
    input = "pqr3stu8vwx"
    expected_result = 38
    result = day1.process_string(input)
    assert result == expected_result 

def test_case3():
    input = "a1b2c3d4e5f"
    expected_result = 15
    result = day1.process_string(input)
    assert result == expected_result 

def test_case4():
    input = "treb7uchet"
    expected_result = 77
    result = day1.process_string(input)
    assert result == expected_result 

def test_sum_result():
    lst_lines = ["1abc2","pqr3stu8vwx","a1b2c3d4e5f","treb7uchet"]
    expected_result = 142
    result = day1.sum_results(lst_lines)
    assert result == expected_result 
