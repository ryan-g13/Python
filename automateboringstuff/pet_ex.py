petList = ['Sophie', 'MooMoo', 'Garfield']
print('Enter a pet\'s name: ')
name = input()
if name not in petList:
    print('The pet you have entered is not in the list')
else:
    print(name + ' is contained in the pet list.')
