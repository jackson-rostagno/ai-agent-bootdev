#!/usr/bin/env python3
from functions.get_files_info import get_files_info


def main():
    print('get_files_info("calculator", "."):')
    result1 = get_files_info("calculator", ".")
    print("Result for current directory:")
    for line in result1.split("\n"):
        print(f"  {line}")
    print()
    
    print('get_files_info("calculator", "pkg"):')
    result2 = get_files_info("calculator", "pkg")
    print("Result for 'pkg' directory:")
    for line in result2.split("\n"):
        print(f"  {line}")
    print()
    
    print('get_files_info("calculator", "/bin"):')
    result3 = get_files_info("calculator", "/bin")
    print("Result for '/bin' directory:")
    for line in result3.split("\n"):
        print(f"  {line}")
    print()
    
    print('get_files_info("calculator", "../"):')
    result4 = get_files_info("calculator", "../")
    print("Result for '../' directory:")
    for line in result4.split("\n"):
        print(f"  {line}")


if __name__ == "__main__":
    main()

