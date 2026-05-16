# If languages of two friends are same; what will happen to the program in problem 6?
s = {}
name = input("Enter name:")
lang = input("Enter Language:")
s.update({name: lang})
name = input("Enter name:")
lang = input("Enter Language:")
s.update({name: lang})
print(s)