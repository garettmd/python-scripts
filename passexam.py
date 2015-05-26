import re

lengthTest = re.compile(r'(\S{8,})')
digitTest = re.compile(r'(\d+)')
upTest = re.compile(r'[A-Z]')
loTest = re.compile(r'[a-z]')

text = 'Password1'
# text = 'Password'
# text = 'password'
# text = 'pass'
output = ''

print(len(lengthTest.findall(text)))
print(len(digitTest.findall(text)))
print(len(upTest.findall(text)))
print(len(loTest.findall(text)))

if len(lengthTest.findall(text)) > 0:
    output += '\nPassword is long enough.'

if len(digitTest.findall(text)) > 0:
    output += '\nPassword does include numbers.'

if len(upTest.findall(text)) > 0 and len(loTest.findall(text)) > 0:
    output += '\nPassword has both upper and lowercase characters.'

print(output)