#!/usr/bin/env python3
from functions.write_file import write_file


def main():
    # Test overwriting lorem.txt
    print('write_file("calculator", "lorem.txt", "wait, this isn\'t lorem ipsum"):')
    result1 = write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum")
    print("Result:")
    print(result1)
    print()
    
    # Test writing to a new file in a subdirectory
    print('write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet"):')
    result2 = write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")
    print("Result:")
    print(result2)
    print()
    
    # Test writing outside working directory (should error)
    print('write_file("calculator", "/tmp/temp.txt", "this should not be allowed"):')
    result3 = write_file("calculator", "/tmp/temp.txt", "this should not be allowed")
    print("Result:")
    print(result3)


if __name__ == "__main__":
    main()

