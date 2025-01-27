def format_string(name, age):
    """
    Create a formatted string using f-strings.
    Args:
        name (str): Person's name
        age (int): Person's age
    Returns:
        str: Formatted string
    """
    return f"{name} is {age} years old."

def conditional_check(number):
    """
    Check if a number is greater, lesser, or equal to 10.
    Args:
        number (int): Number to check
    Returns:
        str: "Greater", "Lesser", or "Equal"
    """
    if number > 10:
        return "Greater"
    elif number < 10:
        return "Lesser"
    else:
        return "Equal"

def loop_sum(n):
    """
    Calculate sum of numbers from 1 to n using a loop.
    Args:
        n (int): Upper limit
    Returns:
        int: Sum of numbers
    """
    total = 0
    for i in range(1, n+1):
        total += i
    return total

def list_operations(numbers):
    """
    Perform operations on a list of numbers.
    Args:
        numbers (list): List of numbers
    Returns:
        tuple: (sum, max, min)
    """
    return (sum(numbers), max(numbers), min(numbers))

def dict_operations(students_dict):
    """
    Find students with scores above 80.
    Args:
        students_dict (dict): Dictionary of student names and scores
    Returns:
        list: Names of students with scores > 80
    """
    return [name for name, score in students_dict.items() if score > 80]

def set_operations(list1, list2):
    """
    Find common elements between two lists.
    Args:
        list1 (list): First list
        list2 (list): Second list
    Returns:
        set: Common elements
    """
    return set(list1) & set(list2)

def arithmetic_ops(a, b):
    """
    Perform arithmetic operations.
    Args:
        a (float): First number
        b (float): Second number
    Returns:
        dict: Results of arithmetic operations
    """
    return {
        "addition": a + b,
        "subtraction": a - b,
        "multiplication": a * b,
        "division": a / b if b != 0 else "undefined"
    }

def logical_ops(x, y):
    """
    Perform logical operations.
    Args:
        x (bool): First boolean
        y (bool): Second boolean
    Returns:
        dict: Results of logical operations
    """
    return {
        "AND": x and y,
        "OR": x or y,
        "NOT x": not x,
        "NOT y": not y
    }

def bitwise_ops(a, b):
    """
    Perform bitwise operations.
    Args:
        a (int): First integer
        b (int): Second integer
    Returns:
        dict: Results of bitwise operations
    """
    return {
        "AND": a & b,
        "OR": a | b,
        "XOR": a ^ b,
        "NOT a": ~a,
        "NOT b": ~b,
        "Left Shift a by 1": a << 1,
        "Right Shift b by 1": b >> 1
    }


if __name__ == "__main__":
    print(format_string("John", 25))
    print(format_string("Alice", 30))
    print(conditional_check(15))
    print(conditional_check(5))
    print(conditional_check(10))
    print(loop_sum(5))
    print(loop_sum(3))
    print(loop_sum(1))
    print (list_operations([1, 2, 3, 4, 5]))
    print(list_operations([10, 20, 30]))
    students = {
        "John": 85,
        "Alice": 90,
        "Bob": 75,
        "Eve": 95
    }
    print(dict_operations(students))
    print(set_operations([1, 2, 3], [2, 3, 4]))  
    print(set_operations([1, 2], [3, 4]))        
    print(arithmetic_ops(10,5))                 
    print(logical_ops(True, False))
    print(bitwise_ops(12, 10))
