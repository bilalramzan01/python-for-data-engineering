#Data type used to store key-value pairs
#Keys must be unique and immutable (string, number, tuple)
#Values can be of any data type and can be duplicated
#Dictionaries are defined using curly braces {} and key-value pairs are separated by commas
marks = {"Math": 90, "Science": 85, "English": 92}
print(marks)
print(type(marks))
print(marks["Math"])  # Accessing value using key