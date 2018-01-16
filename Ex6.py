'''Example 6
Ask the user for a string and print out whether this string is a palindrome or not.
(A palindrome is a string that reads the same forwards and backwards.)
'''

c = input('Please provide a string to check to see if it is a palindrome: ')
#c = str(c)    converting to a string is unnecessary
o = c[::-1] #learned this new feature reversing a string!!!!!

if c == o: #logic test to verify if forwards = backwards
    print('The word', c, 'you have provided is indeed a palindrome')
else:
    print('The word', c, 'you have provided is not a palindrome')