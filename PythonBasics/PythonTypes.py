from typing import List

print(2 + 2)
print((50 - 5 * 6) / 4)  # follows BODMAS rule
print(8 / 5)  # division always returns a floating point number
print(17 // 3)  # floor division discards fractional part
print(17 % 3)  # the % operator returns remainder of division
print(2 ** 7)  # 2 to the power of 7

# strings
print('welcome to python')
print("doesn't")
print('Firstline\nsecond line')
print(r'c:\some\name')
print('c:\some\name')
# By using triple quotes string literals can span multiple lines
print("""\
Usage: thingy {OPTIONS]
    -h         Display this usage message
-H hostnmae  Hostname to connect to
    """)
print('un' + 3 * 'ium')
print('py' 'thon')
print('this is a test '
      'to write long strings '
      'Concatened togteher')
# can't concatenate a variable and a string literal, but (+) will work
prefix = 'py'
# print(prefix 'thon') is wrong
print(prefix + 'thon')
# strings can be indexed
word = 'python'
print(word[0])
print(word[4])
# If indices are given negative number, starts counting from the right
print(word[-1])  # last digit = -1
print(word[-2])
print(word[-6])
# Slicing allows you to obtain substring:
print(word[0:2])  # left number digit is included while right is excluded
print(word[:2] + word[2:])
# in first case left is taken as zero and in second case right is taken as last digit
print(word[-2:])  # Digits included from second last to end
# Python strings cannot be changed,they are immutable
# word[0] ='J'
# word[2:]='py'  - above two result in error
print('j' + word[1:])
print(len('python'))  # len() returns length of string

# Lists
squares = [1, 4, 9, 16, 25]
print(squares)
print(squares[0])
print(squares[-3:])  # Lists are mutable
cubes = [1, 8, 27, 65, 125]
cubes[3] = 64
print(cubes)
cubes.append(6**3) # Append adds value to the end of list
print(cubes)
cubes[2:2] = [20,40] #replace or add some values
print(cubes)
cubes[:] = [] # clears all the values with an empty list
print(len(['a','b']))
a = ['a', 'b', 'c']
n = [1,2,3]
x = [a,n]
print(x)
print(x[0])
print(x[1][0])
a,b = 0,1
while b < 1000:
    print(b, end=',')
    a,b = b,a+b
