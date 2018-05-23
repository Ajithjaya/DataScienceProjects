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
for n in range(2,10):
    for x in range (2, n):
        if n % x == 0:
            print (n, 'equals',x, '*', n//x)
            break
        else:
            print (n, 'is a prime number')
            break

# Continue statement
for num in range(2, 10):
    if num % 2== 0:
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
         a, b = b, a+b
    return result
f100 = fib2(100)
print(f100)
