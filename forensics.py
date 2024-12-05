import logging
import secrets

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# General method for handling various types
def handle_method(input_param, expected_type, operation, error_message):
    """
    General handler for different types of inputs and operations.
    :param input_param: The input parameter to be processed
    :param expected_type: The expected type of input_param
    :param operation: The operation to perform on the valid input
    :param error_message: The error message to display if input validation fails
    :return: The result of the operation or raises an exception
    """
    try:
        if isinstance(input_param, expected_type):
            return operation(input_param)
        else:
            raise ValueError(error_message)
    except Exception as e:
        logging.error(f"Error with input {input_param}: {e}")
        raise

# Specific operations for different methods
def multiply_by_2(input_param):
    return input_param * 2

def convert_to_upper(input_param):
    return input_param.upper()

def sort_list(input_param):
    return sorted(input_param)

def round_float(input_param):
    return round(input_param, 2)

def invert_boolean(input_param):
    return not input_param

# Sample data for testing
sample_int = secrets.randbelow(100)+1
sample_str = "hello"
sample_list = [3, 1, 4, 1, 5, 9]
sample_float = 3.14159
sample_bool = True

# Method calls with logging
if __name__ == "__main__":
    logging.info("Starting forensics testing...")

    method_1_result = handle_method(sample_int, int, multiply_by_2, "Invalid input type for Method 1")
    logging.info(f"Method 1 result: {method_1_result}")

    method_2_result = handle_method(sample_str, str, convert_to_upper, "Invalid input type for Method 2")
    logging.info(f"Method 2 result: {method_2_result}")

    method_3_result = handle_method(sample_list, list, sort_list, "Invalid input type for Method 3")
    logging.info(f"Method 3 result: {method_3_result}")

    method_4_result = handle_method(sample_float, float, round_float, "Invalid input type for Method 4")
    logging.info(f"Method 4 result: {method_4_result}")

    method_5_result = handle_method(sample_bool, bool, invert_boolean, "Invalid input type for Method 5")
    logging.info(f"Method 5 result: {method_5_result}")

    logging.info("Forensics testing completed.")
