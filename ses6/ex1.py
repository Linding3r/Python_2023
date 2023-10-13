
import time
import os

os.chdir("ses6")



def logging(func):
    def wrapper(*args):
        f = open('log.txt', "a")
        f.write(time.asctime() + "\n")
        f.write("Function name: " + func.__name__ + "\n")
        f.write("Arguments: " + str(args) + "\n")
        f.write("Result: " + str(func(*args)) + "\n\n")
        return func(*args)
    return wrapper


@logging
def add(*args):
    return sum(args)

@logging
def printer(text):
    return text

#add = logging(add)
#printer = logging(printer)

add(12,44)
printer("Hello World")





