from random import *
from maytinh2 import calculate
def generate_quiz():
    # Hint: Return [x, y, op, r]
    x = randint(0, 9)
    y = randint(0, 9)
    op = choice(["+", "-", "*", "/"])
    error = randint(-1, 1)
    r = x + y + error
    return[x, y, op, r]

def check_answer(x, y, op, r, user_choice):
    print("check_answer: ", user_choice)
    print(x,y,op,r)
    a = calculate(x,y,op)
    if r == a:
        if user_choice == True:
            print(True)
        else :
            print(False)
    elif r != a:
        if user_choice == True:
            print(False)
        else : 
            print(True)
    
    
    
