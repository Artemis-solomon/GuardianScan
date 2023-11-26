import unittest
from sql_injection_detector import detect_sql_injection

class TestSQLInjectionDetector(unittest.TestCase):
    def test_detect_sql_injection(self):
        # Test for potential SQL injection
        sql_injection_input = "SELECT * FROM users WHERE username = 'admin' OR '1' = '1';"
        self.assertTrue(detect_sql_injection(sql_injection_input))

        # Test for non-SQL injection
        non_sql_injection_input = "SELECT * FROM users WHERE username = 'john.doe';"
        self.assertFalse(detect_sql_injection(non_sql_injection_input))

if __name__ == '__main__':
    unittest.main()

