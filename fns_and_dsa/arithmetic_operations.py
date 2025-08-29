# arithmetic_operations.py

def perform_operation(num1: float, num2: float, operation: str):
    """
    Performs a basic arithmetic operation on two numbers.
    
    Parameters:
        num1 (float): First number
        num2 (float): Second number
        operation (str): The operation to perform ('add', 'subtract', 'multiply', 'divide')
    
    Returns:
        float or str: The result of the operation, or an error message if invalid.
    """
    if operation == "add":
        return num1 + num2
    elif operation == "subtract":
        return num1 - num2
    elif operation == "multiply":
        return num1 * num2
    elif operation == "divide":
        if num2 == 0:
            return "Error: Division by zero is not allowed"
        return num1 / num2
    else:
        return "Error: Invalid operation"