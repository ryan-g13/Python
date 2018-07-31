#! python3 
# Adds wikipedia bullet points as stars and spaces appended to the front of strings

import pyperclip
text = pyperclip.paste()

splitText = text.split('/n')
for i in range(len(splitText)):
  splitText[i] = '* ' + splitText[i]

print(splitText)
joinedText = '/n'.join(splitText)
print(joinedText)
pyperclip.copy(joinedText)