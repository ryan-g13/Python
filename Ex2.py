'''Exercise 2
Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user. Hint: how does an even / odd number react differently when divided by 2?

Extras:
    If the number is a multiple of 4, print out a different message.
    Ask the user for two numbers: one number to check (call it num) and one number to divide by (check). If check divides evenly into num, tell that to the user. If not, print a different appropriate message.
'''

#1st Challenge
'''num = int(input('Please provide a number for the even or odd test: '))

if num%2 > 0:
    print("The number " + str(num) + ' is an odd number')
elif num%4 <= 0:
    print("The number " + str(num) + ' is an even number that is divisible cleanly by 4')
else:
    print("The number " + str(num) + ' is an even number')
    '''

#refactored for 2nd challenge
num = int(input('Please provide a number(numerator) for the division test: '))
check = int(input('Please provide a number(denominator) to check if it divides into your previous one: '))

if num%check > 0:
    print("The number " + str(num) + ' divided by ' + str(check) + ' is not cleanly divisible')
else:
    print("The number " + str(num) + ' is divisible cleanly by ' + str(check))
