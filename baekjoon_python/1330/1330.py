user_input = input()
a, b = map(int, user_input.split(' '))

if a < b: print('<')
if a > b: print('>')
if a == b: print('==')