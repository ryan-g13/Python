'''Create a program that asks the user for a number and then prints out a list of all the divisors of that number.
(If you don’t know what a divisor is, it is a number that divides evenly into another number.
For example, 13 is a divisor of 26 because 26 / 13 has no remainder.)'''

int = int(input('Provide a number to find the divisors: '))
list = range(1 , int + 1) #my original solution didn't include the number itself *added +1
divisors = []

for i in list:
    if int%i == 0:
        divisors.append(i)

print('The divisors of your number are ' + str(divisors))