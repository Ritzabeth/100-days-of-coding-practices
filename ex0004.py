n = input('Write something:')
print('the type is', type(n))
print('Is {} Numeric?'.format(n), n.isnumeric())
print('Is {} Alphabetic?'.format(n), n.isalpha())
print('Is {} Upper Case only?'.format(n), n.isupper())
print('Is {} Alphanumeric?'.format(n), n.isalnum())
print('Is {} Space?'.format(n), n.isspace())
print('Is {} ALL lower case?'.format(n), n.islower())
print('Does {} ONLY have one upper case?'.format(n), n.istitle())
print('Does {} have ONLY digits?'.format(n), n.isdigit())
print('Does {} have ASCII characters?'.format(n), n.isascii())
print('Is {} only space?'.format(n), n.isspace())
print('Is {} a decimal number?'.format(n), n.isdecimal())
print('Is {} a valid Python identifier?'.format(n), n.isidentifier())
