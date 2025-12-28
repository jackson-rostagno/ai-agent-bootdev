#!/usr/bin/env python3
from functions.get_file_content import get_file_content
import config


def main():
    # Test truncation with lorem.txt
    print('get_file_content("calculator", "lorem.txt"):')
    result1 = get_file_content("calculator", "lorem.txt")
    print(f"Result length: {len(result1)} characters")
    if f'truncated at {config.MAX_CHARS} characters' in result1:
        print("✓ File was properly truncated")
        # Show last 100 characters to see truncation message
        print(f"Last 100 characters: ...{result1[-100:]}")
    else:
        print("✗ File was not truncated (unexpected)")
    print()
    
    # Test reading main.py
    print('get_file_content("calculator", "main.py"):')
    result2 = get_file_content("calculator", "main.py")
    print("Result:")
    print(result2)
    print()
    
    # Test reading pkg/calculator.py
    print('get_file_content("calculator", "pkg/calculator.py"):')
    result3 = get_file_content("calculator", "pkg/calculator.py")
    print("Result:")
    print(result3)
    print()
    
    # Test reading /bin/cat (should error)
    print('get_file_content("calculator", "/bin/cat"):')
    result4 = get_file_content("calculator", "/bin/cat")
    print("Result:")
    print(result4)
    print()
    
    # Test reading non-existent file (should error)
    print('get_file_content("calculator", "pkg/does_not_exist.py"):')
    result5 = get_file_content("calculator", "pkg/does_not_exist.py")
    print("Result:")
    print(result5)


if __name__ == "__main__":
    main()

