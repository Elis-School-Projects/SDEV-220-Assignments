# Name: Eli Walters
# File Name: __init__.py
# Description: Module that provides a basic function to add together an interable list

def sum(arg):
    total = 0
    for val in arg:
        total += val
    return total