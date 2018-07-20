# Say you have a list value like this:

# spam = ['apples', 'bananas', 'tofu', 'cats']

# Write a function that takes a list value as an argument and returns a string with all the items separated by a comma and a space, with and inserted before the last item. For example, passing the previous spam list to the function would return 'apples, bananas, tofu, and cats'. But your function should be able to work with any list value passed to it. 


inputList = ['Aprilia', 'BMW', 'Triumph', 'Ducati', 'Honda', 'Kawasaki']
lastWord = len(inputList[-1])
returnList = ''
for item in inputList:
    returnList += item + ', '
    
returnList = returnList[:-2] # trim trailing comma
print(returnList[:-9] + ' and' + returnList[-9:]) # add ' and'
