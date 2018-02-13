from random import *
from ex1 import *

def generate_quiz():
    # Hint: Return [x, y, op, result]
    x = randint(1,10)
    y = randint(1,10)
    op = choice(['+','-','*','/'])

    m = randint(-1,2)
    n = randint(-1,1)
    error_list = [0,0,0, m, m]
    error = error_list[n]
    result = eval(x,y,op) + error
    return [x,y,op,result]

def check_answer(x, y, op, result, user_choice):
    print (x, y, op, result, user_choice)
    if eval(x,y,op) == result and user_choice == True:
        return True
    elif eval(x,y,op) != result and user_choice == False:
        return True
    else:
        return False
