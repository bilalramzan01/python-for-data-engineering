#Write a python program to print the contents of a directory using the os module. Search online for the function which does that.
#Label the program written in problem 4 with comments.


import os

# specify the directory path (use '.' for current directory)
path = "D:/Repositories/python-for-data-engineering/01-Programming-Fundamentals/01-Chapter/Practice"

# get the list of contents
contents = os.listdir(path)

# print each item
for item in contents:
    print(item)