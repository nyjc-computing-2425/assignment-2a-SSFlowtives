num = input('Enter a number (decimal or integer): ')
# type your code here
temp = num.strip(' ').replace('.','').lstrip('0')
sf = len(temp)
  
# do not change any code beyond this point
print('The number', num, 'has', sf, 'significant figures.')
