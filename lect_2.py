
x = 'hello world'
print(x)

print('')

x = int(raw_input('enter a number'))

if x%2 == 0:
    print('even')
elif x%3 == 0 and x/3 == 1:
    print('ok then') 
else: 
    print('I dunno')