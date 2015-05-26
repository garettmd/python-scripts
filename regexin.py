import pyperclip, re

phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?              # optional area code
    (\s|-|\.)?                      # optional separator
    (\d{3})                         # first 3 digits
    (\s|-|\.)                       # separator
    (\d{4})                         # last 4 digits
    (\s(ext|x|ext.)\s*(\d{2,5}))?   # optional extension
    )''', re.VERBOSE)

emailRegex = re.compile(r'''(
    [a-zA-Z0-9._$+-]+       # username
    @                       # At symbol
    [a-zA-Z0-9.-]+          # domain
    (\.[a-zA-Z0-9]+)          # dot-something
    )''', re.VERBOSE)

text = str(pyperclip.paste())
matches = []
for groups in phoneRegex.findall(text):
    phoneNum = '-'.join([groups[1], groups[3], groups[5]])
    if groups[8] != '':
        phoneNum += ' x' + groups[8]
    matches.append(phoneNum)
for groups in emailRegex.findall(text):
    matches.append(groups[0])

#print(phoneRegex.findall(text))
#print(emailRegex.findall(text))
#print(matches)

if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('\nCopied to clipboard:')
    print('\n'.join(matches))
else:
    print('No phone numbers or email addresses found.')
