'''Write a Python Program to Check if a String is a Palindrome or Not?'''

input_str = "nitin"
new_str = ''
for c in input_str:
    new_str += c

print(f'new str is {new_str}')
if new_str == input_str:
    print(f'{input_str} is a PALINDROME')
else:
    print(f'{input_str} is not a PALINDROME')

