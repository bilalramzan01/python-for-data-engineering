#Sequence of character enclosed in Quotes, Its immuteable means cant change in existing string

#Single Line
A = "Bilal"
B = 'Bilal'
#Multi-Line

c = """Bilal is a good boy
and he is also handsome as well """

print(A,B,c)

# String Slicing
nameshort = A[0:4]
nameshort = A[:4] #It will start from 0
nameshort = A[1:] #It will end at 5
print(nameshort)
cha4=A[4]
print(cha4)
print(A[3])
print(A[-3])
print(A[-5:-1])

#Skip value concept
h="0123456789"
print(h[0:9:2])