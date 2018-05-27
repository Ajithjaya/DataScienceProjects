s = 'Hello World'
print(str(s))
print(repr(s))
print(str(1/7))
x = 10 * 3.25
y = 200*200
s = 'The value of x is ' + repr(x) + ', and y is ' + repr(y) + ' this'
print(s)

#  the repr() of a string adds string qoutes and backlashes:
hello = 'hello, world\n'
hellos = repr(hello)
print(hellos)

for x in range(1,11):
    print('{0:2d} {1:3d} {2:4d}'.format(x,x*x,x*x*x))

print('We are the {} who say "{}!"'.format('knights', 'Ni'))

print('{0} and {1}'.format('spam', 'eggs'))
print('{1} and {0}'.format('spam', 'eggs'))
print('This {food} is {adjective}.'.format(food='spam', adjective='absolutely horrible'))
print('The story of {0}, {1}, and {other}.'.format('Bill', 'Manfred', other = 'George'))\

contents = 'eels'
print('My hovercraft is full of {}.'.format(contents))
print('My hovercraft is full of {!r}.'.format(contents))  # !r = repr(r),  !s = str()

import math
print('The value of PI is approximately {0:.4f}.'.format(math.pi))
table = {'sjoerd': 4127, 'Jack': 4098, 'Decab': 7678}
for name, phone in table.items():
    print('{0:10} ==> {1:10d}'.format(name, phone))

table = {'Sjoerd': 4127, 'Jack': 4098, 'Decab': 8637678}
print('Jack: {0[Jack]:d}; Sjoerd: {0[Sjoerd]:d};Decab: {0[Decab]:d}'.format(table))

with open('workfile') as f:
    read_data = f.read()

print((read_data))
print(f.closed)

