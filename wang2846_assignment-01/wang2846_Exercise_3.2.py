####################
# Header
# Jan. 17 2020
# Shizhang Wang
# 0027521360
# the uncommented part of the program should print 'spam' four times
# details in in-line comments

# There are so many formatting information/requirements scattered
# around, I registered late so I tried to include everything I read,
# but is it possible to get a template with all of it included so I/we
# can follow?

# I believe this is what was asked for to turn in, but I don't want lose
# any point over misunderstanding, I apologize for not capturing the first
# two lecture and this long note

####################


## exercise 3.2.1
#def do_twice(f):
#    f()
#    f()
#    
#    
#def print_spam():
#    print('spam')
    
# do_twice(print_spam) 

## exercise 3.2.2
#def do_twice(f, x):
#    f(x)
#    f(x)
#    
#    
#def print_spam(a):
#    print(a)
#    
#do_twice(print_spam, 'spam')

## exercise 3.2.3 & 3.2.4  do_twice
def do_twice(f, x):    # pass in two arguments, one being a function object,
    f(x)               # one being a value, a function (whichever we pass in) 
    f(x)               # would be called twice with the value we pass in
    
def print_twice(bruce):    #  function accepting one argument, and print the 
    print(bruce)           # value passed in twice
    print(bruce)
   
do_twice(print_twice, 'spam')   

## exercise 3.2.5  do_four
#def print_twice(a):
#    print(a)
#    print(a)
#    
#def do_twice(f, b):
#    f(b)
#    f(b)
#    
#def do_four(f, b):
#    do_twice(f, b)
#    do_twice(f, b)
#    
#do_four(print_twice, 'spam')


    
    
