#! python3

# Password management keeper project - idea of creating a password manager

PASSWORDS = {'gmail': 'interestingValue',
             'blog': 'Bl00pers',
             'airDefenseSystem': '12345'}

import sys, pyperclip

if len(sys.argv) < 2:
    print('Usage: python.pwkeeper.py [account] - copy account password')
    sys.exit()

account = sys.argv[1] # first argument passed in CLI arg
 
if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print('Password for ' + account + ' has been copied to the clipboard')
else:
    print('There is no account associated with the name ' + account)
