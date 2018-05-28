# Compile time errors and run time errors

# Syntax Errors - missing a colon , : , did not declare a variable , etc..
# Errors detected during execution are called Execptions, they are not unconditionally fatal.
#print(10*(1/0))
#print(4 + spam*3)
#print('2' + 2)

# Handling Execptions
while True:
    try:
        x = int(input("Please enter a number : "))
        break
    except ValueError:
        print('Oops! That was no valid number. Try again...')

import sys
#try:
#    i = 10
#    print(1/0)
#    f = open('myfile.txt')
#   s = f.readline()
#   i = int(s.strip())
#except OSError as err:
#    print(" OS Error : {0}".format(err))
#except ValueError:
 #   print("Could not convert data to an integer : ")
#    except:
 #   print("Unexpected error:", sys.exc_info()[0])
  #  raise

# try :
#     f  = open('workfile', 'r')
# except OSError:
#     print('cannot open')
# else:
#     print(len(f.readlines()), 'lines')
#     f.close()
#
# def this_fails():
#     x = 1/0
# try :
#     this_fails()
# except ZeroDivisionError as err:
#     print('Handling run-time error:', err)
#
# try:
#     raise NameError('Hi There')
# except NameError:
#     print('An execption flew by!')
#     raise

#try:
#    i = 10
#   raise NameError('Hi There')
# except NameError:
# raise KeyboardInterrupt
#     finally:
#         print('Goodbye, world!')

# def fin():
#     try:
#         i = 10
#         return i
#     except:
#         print("dd")
#     finally:
#         print('finally')
#
# retx = fin()
# print(retx)

def divide(x, y):
    try:
        result = x/y
    except ZeroDivisionError:
        print("Division by zero !")
    else:
        print("result is", result)
    finally:
        print("Executing finally clause")

divide(2, 1)
divide(2, 0)
divide("2", "1")



