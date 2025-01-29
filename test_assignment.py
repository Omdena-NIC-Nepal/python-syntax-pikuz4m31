import pytest
from assignment import *

def test_format_string():
    # assert format_string("John", 25) == "My name is John and I am 25 years old"
    # assert format_string("Alice", 30) == "My name is Alice and I am 30 years old"
    assert format_string("John", 25) == "John is 25 years old."
    assert format_string("Alice", 30) == "Alice is 30 years old."

def test_conditional_check():
    assert conditional_check(15) == "Greater"
    assert conditional_check(5) == "Lesser"
    assert conditional_check(10) == "Equal"

def test_loop_sum():
    assert loop_sum(5) == 15
    assert loop_sum(3) == 6
    assert loop_sum(1) == 1

def test_list_operations():
    assert list_operations([1, 2, 3, 4, 5]) == (15, 5, 1)
    assert list_operations([10, 20, 30]) == (60, 30, 10)

def test_dict_operations():
    students = {
        "John": 85,
        "Alice": 90,
        "Bob": 75,
        "Eve": 95
    }
    result = dict_operations(students)
    assert set(result) == {"John", "Alice", "Eve"}

def test_set_operations():
    assert set_operations([1, 2, 3], [2, 3, 4]) == {2, 3}
    assert set_operations([1, 2], [3, 4]) == set()

def test_arithmetic_ops():
    result = arithmetic_ops(10, 5)
    assert result["sum"] == 15
    assert result["difference"] == 5
    assert result["product"] == 50
    assert result["quotient"] == 2.0

def test_logical_ops():
    result = logical_ops(True, False)
    assert result["and"] == False
    assert result["or"] == True
    assert result["not_x"] == False

def test_bitwise_ops():
    result = bitwise_ops(12, 10)
    assert result["and"] == 8
    assert result["or"] == 14
    assert result["xor"] == 6

if __name__ == "__main__":
    print(format_string("John", 25)) #format string 1 test
    print(format_string("Alice", 30)) #format string 2 test
    print(conditional_check(15)) #Check if a number is greater, lesser, or equal to 10.
    print(conditional_check(5)) #Check if a number is greater, lesser, or equal to 10.
    print(conditional_check(10)) #Check if a number is greater, lesser, or equal to 10.
    print(loop_sum(5)) #summing of loop to the number 5 
    print(loop_sum(3)) #summing of loop to the number 3
    print(loop_sum(1)) #summing of loop to the number 1
    print (list_operations([1, 2, 3, 4, 5])) #finding sum of elements, max element and smaller element in the list
    print(list_operations([10, 20, 30]))  #addition of all elements in the list, max element and smaller element in the list
    students = {
        "John": 85,
        "Alice": 90,
        "Bob": 75,
        "Eve": 95
    }
    print(dict_operations(students)) #Names of students with scores > 80
    print(set_operations([1, 2, 3], [2, 3, 4]))  #finding Common elements
    print(set_operations([1, 2], [3, 4]))      #Common elements if not found default is set  
    print(arithmetic_ops(10,5))        #Results of arithemetic operations         
    print(logical_ops(True, False)) #Results of logical operations
    print(bitwise_ops(12, 10)) #Results of bitwise operations