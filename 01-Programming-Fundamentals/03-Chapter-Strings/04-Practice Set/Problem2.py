# Write a program to fill in a letter template given below with name and date.
# letter = '''
#     Dear <|Name|>,
#     You are selected!
#     <|Date|>
# '''

letter = '''
Dear <|Name|>,
You are selected!
<|Date|>
'''
print(letter.replace("<|Name|>","Bilal").replace("<|Date|>","7 april 2026"))