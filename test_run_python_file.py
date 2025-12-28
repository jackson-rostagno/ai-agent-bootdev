#!/usr/bin/env python3
from functions.run_python_file import run_python_file


def main():
    # Test running main.py (should print usage)
    print('run_python_file("calculator", "main.py"):')
    result1 = run_python_file("calculator", "main.py")
    print("Result:")
    print(result1)
    print()
    
    # Test running main.py with args
    print('run_python_file("calculator", "main.py", ["3 + 5"]):')
    result2 = run_python_file("calculator", "main.py", ["3 + 5"])
    print("Result:")
    print(result2)
    print()
    
    # Test running tests.py
    print('run_python_file("calculator", "tests.py"):')
    result3 = run_python_file("calculator", "tests.py")
    print("Result:")
    print(result3)
    print()
    
    # Test running file outside working directory (should error)
    print('run_python_file("calculator", "../main.py"):')
    result4 = run_python_file("calculator", "../main.py")
    print("Result:")
    print(result4)
    print()
    
    # Test running non-existent file (should error)
    print('run_python_file("calculator", "nonexistent.py"):')
    result5 = run_python_file("calculator", "nonexistent.py")
    print("Result:")
    print(result5)
    print()
    
    # Test running non-Python file (should error)
    print('run_python_file("calculator", "lorem.txt"):')
    result6 = run_python_file("calculator", "lorem.txt")
    print("Result:")
    print(result6)


if __name__ == "__main__":
    main()

