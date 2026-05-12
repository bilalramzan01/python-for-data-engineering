#sets is a collection of unique and non repetitive elements
marks = {90, 80, 70, 60, 50, 40, 30, 20, "Bilal"}
marks2 = {90, 80,  "Bilal"} #duplicate element will be ignored
empty= set() #empty set
print(marks)
marks.add(100) #add an element to the set
print(marks)
print(marks.union(marks2)) #union of two sets
print(marks.intersection(marks2)) #intersection of two sets