import pytest
import os 
import sys

if __name__ == "__main__":
    tests_path = os.path.join(os.path.dirname(__file__), "compress_numbers_tests.py")
    sys.exit(pytest.main([tests_path, "-v"]))