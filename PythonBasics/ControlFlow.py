#  if statements
# x = int(input("Please enter an integer :  "))
x = 34
if x < 0:
    x = 0
    print('Negative replaced with zero')
elif x == 0:
    print('Zero')
elif 0 < x <= 42:
    print('Value is between 0 and 42 :' + str(x))  # print only takes strings no other variables
else:
    print(x)

#  for statement
words = ['cat', 'window', 'defenestrate']
for w in words:
    print(w, len(w))
for w in words[:]:
    if len(w) > 6:
        words.insert(0, w)  # insert(x,y) x is position where it inserts y
print(words)

# range functions
for i in range(5, 10):
    print(i)
for i in range(0, 10, 3):
    print(i)
for i in range(-10, -100, -30):
    print(i)
a = ['Mary', 'had', 'a', 'little', 'lamb']
for i in range(len(a)):
    print(i, a[i])

# Break statement
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n // x)
            break
        else:
            print(n, 'is a prime number')
            break

# Continue statement
for num in range(2, 10):
    if num % 2 == 0:
        print("Found an even number", num)
        continue
    print("Found an odd number", num)


# pass statement does nothing. it can be used when a statement is required syntactically but program requires no action
def initlog(*args):
    pass


def fib2(n):
    """ Return alist containing the Fibionacci series upto n"""
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a + b
    return result


f100 = fib2(100)
print(f100)


# Default argument values
def ask(prompt, retries=4, reminder='please try again!'):
    while True:
        ok = input(prompt)
        if ok in ('y', 'ye', 'yes'):
            return True
        if ok in ('n', 'no', 'nop', 'nope'):
            return False
        retries = retries - 1
        if retries < 0:
            raise ValueError('invalid user response')
        print(reminder)


#  ask('Do you really want to quit?', 5)
#  ask('OK to overwrite the file?', 2, 'come on, only yes or no!')

# keyword arguments
def parrot(voltage, state='a stiff'):
    print(voltage, state)


#  parrot(voltage=1000,state='dfd')
#  after a keyword argument non keyword argument throws error
parrot(1000, 'dfd')


def cheese(kind, *arguments, **keywords):  # * - list, ** - dictionary and ** must always come at last
    print(kind)
    for arg in arguments:
        print('tuple values : ', arg)
    for w in keywords:
        print('dictionary values :', keywords[w])


cheese('MY name is Ajith', "first argument in tuple", "second argument in tuple ", language="python",
       technology='Deep Learning')


# Arbitrary arguments list
def concat(*args, sep="/"):
    return sep.join(args)


print(concat("earth", "mars", "venus"))

# Unpackaging Arguments Lists
print(list(range(3, 6)))  # normal call with seperate arguments
args = [3, 6]
print(list(range(*args)))  # call with arguments unpacked from a list


# In the same fashion dictionaries can deliver keyword arguments
#  with hte **-operator:
def parrot(voltage, state='a stiff',
           action='voom'):  # in case of a method defined two types it gets overloaded i.e method with most argumets get read.
    print(state)
    print(action)
    print(voltage)


d = {"voltage": "four million", "state": "bleeding demised", "action": "VOOM"}
parrot(**d)


# Lambda Expressions
def make_incrementor(n):
    return lambda x: x + n


f = make_incrementor(42)
print(f(0))
print(f(1))

# pass a small function as an argumnent
pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
pairs.sort(key=lambda pair: pair[1])
print(pairs)

# coding style
#  https://www.python.org/dev/peps/pep-0008/   -  for styling in python code