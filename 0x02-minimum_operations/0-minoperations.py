#!/usr/bin/python3
"""
in a text file, there is a sinle character 'H'.
Your text editor can execute only two operations in this file 'Copy All' and 'paste'.
Given a number n, write a method that calculate the fewest number of operations needed to result in exactly 'n' 'H'characters in the file.

program will return an integer.
if 'n' IS IMPOSSIBLE TO ACHIEVE, RETURN '0'
"""

def minOperations(n):
    if n <= 1:
        return 0

    print("n before loop", n)
    
    divisor = 2

    num_of_operations = 0

    while n> 1:
        if n % divisor == 0:
            print("divisor is: ", divisor)
            n = n / divisor
            print("\n = n / divisor", n)

            num_of_operations = num_of_operations += divisor
            print("\num of ops", num_of_operations)

        else:
            divisor += 1
            print("divisor after increment: ", divisor)

        return num_of_operations
    
    n = 12

    print(minoperation(n))
