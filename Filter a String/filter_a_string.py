"""
Create a function which takes a string txt and returns a list of numbers with count of uppercase letters, lowercase letters, numbers and special characters.

Examples:
filter_string("*$(#Mu12bas43hiR%@*!") ➞ [2, 6, 4, 8]
//2 uppercase letters
//6 lowercase letters
//4 numbers
//8 special characters

filter_string("^^Edabit^^%$#12379") ➞ [1, 5, 5, 7]
filter_string("**Airforce1**") ➞ [1, 7, 1, 4]
"""

import re


def filter_string(txt):
    # print(re.findall(r'[^\d\W]', txt))
    uppercase = len(re.findall(r'[A-Z]', txt))
    lowercase = len(re.findall(r'[a-z]', txt))
    digits = len(re.findall(r'\d', txt))
    special = len(re.findall(r'[^\w]', txt))

    return [uppercase, lowercase, digits, special]


if __name__ == '__main__':
    filter_string("^^Edabit^^%$#12379")
