# sql_injection_detector.py

import re

def detect_sql_injection(input_string):
    """
    Detect potential SQL injection in the given input string.

    Args:
    - input_string (str): The input string to be checked for SQL injection.

    Returns:
    - bool: True if potential SQL injection is detected, False otherwise.
    """
    # Regular expression to identify common SQL injection patterns
    sql_injection_pattern = re.compile(
        r'\b(union|select|insert|update|delete|from|where|order by|group by|having)\b', 
        re.IGNORECASE
    )

    # Check if the input string matches the SQL injection pattern
    if re.search(sql_injection_pattern, input_string):
        return True
    else:
        return False

