# scanner_main.py

from sql_injection_detector import detect_sql_injection

# Example usage
user_input = input("Enter data to scan for SQL injection: ")
if detect_sql_injection(user_input):
    print("Potential SQL injection detected!")
else:
    print("No SQL injection detected.")

