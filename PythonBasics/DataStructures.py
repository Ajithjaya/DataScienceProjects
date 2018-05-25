fruits =['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
print(fruits.count('apple'))   #   total number of apples in list
print(fruits.index('banana'))   #  Position of banana
print(fruits.index('banana', 4))  #  Find next banana starting with position 4
fruits.reverse()
print(fruits)
fruits.append('grape')
print(fruits)
fruits.sort()
print(fruits)
print(fruits.pop()) #  last allocated memory and removes

#  Using lists as Stacks
# The List methods make it very easy to use list  as a stack, where the last element added ios the first element \
#  retrieved ("last0in, first out"). To add an item to the top of the stack, use append(). To retrieve an item from
#  top of stack use pop() without an explicit index.
stack = [3, 4, 5]
stack.append(6)
stack.append(7)
print(stack)
print(stack.pop())
print(stack)

#  Using lists as queues , however Lists are not efficient for this purpose (because all other elements have to shifted one by one)

from collections import deque

queue = deque(["Eric", "John", "Michael"])
queue.append("Terry")
print(queue)
print(queue.popleft())  #  The first to arrive now leaves
print(queue.popleft())  #  the second to arrive now leaves
print(queue)  # Remaining queue in order of arrival

#  List comprehensions , it provides  aconcise way to create lists, common applications are used to make new lists of
# where each element is the result of some operations applied to each member of another sequence or iterable or to
#  create a subsequence of those elements that satisfy a cerain condition

squares = []
for x in range(10):
    squares.append(x**2)
print(squares)

squares = list(map(lambda x : x**2, range(10)))
print (squares)

squares  = [x ** 2 for x in range(10)]
print(squares)

#  this list combines the elemts of two lists if they are not equal
print([(x, y) for x in [1,2,3] for y in [3,1,4] if x!=y])

combs = []
for x in [1,2,3]:
    for y in [3,1,4]:
        if x != y :
            combs.append((x,y))
print(combs)

#  A tuple is a sequence like list execpt that it is immutable, and tuples use (), while lists use []

vec = [-4, -2, 0 ,2, 4]
print ([x*2 for x in vec])
print([x for x in vec if x>=0])
print([abs(x) for x in vec])

freshfruit = [' banana', ' loganberry ', 'passion fruit ' ]
print([fruit.strip() for fruit in freshfruit])

print([(x,x**2) for x in range(6)])
vec = [[1,2,3], [4,5,6], [7,8,9]]
print ([num for elem in vec for num in elem])  #  flatten a list using a listcomp with two 'for'

from math import pi
print([str(round(pi,i)) for i in range(1,6)])

# Nested List Comprehensions
matrix = [
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
]
  # The following list comprehension will trnaspose rows and coloumns:
print([[row[i] for row in matrix] for i in range(4)])

transposed = []
for i in range(4):
     transposed.append([row[i] for row in matrix])
print(transposed)

print(list(zip(*matrix)))

# The del statement can remove slices from the list or clear the entire list

a = [-1, 1, 66.25, 333, 333, 1234.5]
del a[0]
print (a)
del a[2:4]
print (a)
del a[:]
print(a)

t = 12345, 54321, 'hello!'
print(t[0])
print(t)
# tuples may be saved
u = t, (1,2,3,4,5)
print(u)
# Tuples are immutable:
# t[0] = 88888 # gives error as tuples are immutable
# but tuples can contain mutable objects
v = ([1,2,3], [3,2,1])
print(v)

empty = ()
singleton = 'hello',  #  constructing one item by following with a comma makes it immutable
print(len(empty))
print(len(singleton))
print(singleton)
