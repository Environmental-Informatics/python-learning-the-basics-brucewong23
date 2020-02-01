####################
# Header
# Jan. 17 2020
# Shizhang Wang
# 0027521360
# the commented parts are different trials
# trial 1: 2 mins, trial 2: 8 mins, trial 3: more than I want to admit..
# more details in in-line comments


##########  Trial 3 ############   
def print_twice(x):
    print(x, end=' ')
    print(x, end=' ')

# left side of horizontal component(+----), effectively do_twice from 
#last exercise
def h_left(f, x):
    print('+', end=' ')
    f(x)           
    f(x)

# combine two h_left, effectively do_four
def unit_one(f, x):
    h_left(f, x)
    h_left(f, x)
    print('+')  # automatively advance to next line w/o end=' '

# left side of the first repetitive segment of vertical component, do_twice
def v_left(f, x):
    print('|', end=' ')
    f(x)
    f(x)
    
# combine two v_left, do_four
def unit_two(f, x):
    v_left(f, x)
    v_left(f, x)
    print('|')

# newly defined do_twice calls function f1 twice, passing in two other
# variables f2 (indicating another function) and x
def do_twice(f1, f2, x):
    f1(f2, x)
    f1(f2, x)
 
# newly defined do_four, do_twice was called twice and the variables needed
# for do_twice is passing in through do_four here
def do_four(f1, f2, x):
    do_twice(f1, f2, x)
    do_twice(f1, f2, x)

# combination of unit_one and repetition of unit_two w/ do_four
def draw_figure(f1, f2, x1, x2):
    unit_one(f2, x2)    
    do_four(f1, f2, x1)
    unit_one(f2, x2)
    do_four(f1, f2, x1)
    unit_one(f2, x2)
 
draw_figure(unit_two, print_twice, ' ', '-')
# variable passed in is highly dependent on the require the shape, a more 
# generalized program probably exist
        

########   trial 2    ################

#def plus():
#    print('+', end=' ')
#    
#def minus():
#    print('-', end=' ')
#    
#def vertical_line():
#    print('|', end=' ')
#    
#def space():
#    print(' ', end=' ')
#
#def do_twice(f, x):
#    f(x)
#    f(x)
#    
#def print_twice(x):
#    print(x, end=' ')
#    print(x, end=' ')
#    
#def draw_horizontal(f, x):
#    plus()
#    do_twice(f, x)
#    plus()
#    do_twice(f, x)
#    plus()
#    print('')
#
#def draw_vertical(f, x):
#    vertical_line()
#    do_twice(f, x)
#    vertical_line()
#    do_twice(f, x)
#    vertical_line()
#    print('')
#    
#def draw_figure():
#    draw_horizontal(print_twice, '-')
#    draw_vertical(print_twice, ' ')
#    draw_vertical(print_twice, ' ')
#    draw_vertical(print_twice, ' ')
#    draw_vertical(print_twice, ' ')
#    draw_horizontal(print_twice, '-')
#    draw_vertical(print_twice, ' ')
#    draw_vertical(print_twice, ' ')
#    draw_vertical(print_twice, ' ')
#    draw_vertical(print_twice, ' ')
#    draw_horizontal(print_twice, '-')

# draw_figure()
    
##############    trial 1   #######################

#def draw_figure():
#    print('+','-','-','-','-','+','-','-','-','-','+')
#    print('|',' ',' ',' ',' ','|',' ',' ',' ',' ','|')
#    print('|',' ',' ',' ',' ','|',' ',' ',' ',' ','|')
#    print('|',' ',' ',' ',' ','|',' ',' ',' ',' ','|')
#    print('|',' ',' ',' ',' ','|',' ',' ',' ',' ','|')
#    print('+','-','-','-','-','+','-','-','-','-','+')
#    print('|',' ',' ',' ',' ','|',' ',' ',' ',' ','|')
#    print('|',' ',' ',' ',' ','|',' ',' ',' ',' ','|')
#    print('|',' ',' ',' ',' ','|',' ',' ',' ',' ','|')
#    print('|',' ',' ',' ',' ','|',' ',' ',' ',' ','|')
#    print('+','-','-','-','-','+','-','-','-','-','+')

# draw_figure()