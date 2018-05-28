# Modules
#from PythonBasics.Fibo import Fibo

import Fibo

print(Fibo.fib(1000))
print(Fibo.fib2(100))
print(Fibo.__name__)

fib = Fibo.fib
print(fib(500))

from Fibo import fib, fib2
print(fib(500))

from Fibo import *
print(fib2(500))

import Fibo as xyz
print(xyz.fib(500))

from Fibo import fib as fibonacci
print(fibonacci(500))