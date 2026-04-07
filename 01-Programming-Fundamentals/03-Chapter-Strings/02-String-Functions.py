a="bilal"
print(len(a)) #Length of string

print(a.endswith("al")) # Check End with
print(a.startswith("bl")) #Check start
print(a.capitalize())

text = "hello world"

print(text.upper())     # HELLO WORLD
print(text.lower())     # hello world
print(text.title())     # Hello World
print(text.capitalize())# Hello world
print(text.find("world"))   # 6  (index)
print(text.index("world"))  # 6 (same but gives error if not found)
print(text.startswith("he")) # True
print(text.endswith("ld"))   # True

text = "I like Python"

print(text.replace("Python", "Java"))
# I like Java

text = "apple,banana,mango"

print(text.split(","))  
# ['apple', 'banana', 'mango']

words = ["Hello", "World"]
print(" ".join(words))  
# Hello World

text = "Bilal"

print(len(text))   # length

text = "banana"

print(text.count("a"))  # count