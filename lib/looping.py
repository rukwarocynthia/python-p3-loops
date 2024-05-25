#!/usr/bin/env python3

def happy_new_year():
    c = 10
    while (c > 0):
        print(c)
        c -= 1
    print('Happy New Year!')

def square_integers(int_list):
    return [c ** 2 for c in int_list]

def fizzbuzz():
    for c in range(1, 101):
        if not c % 15:
            print("FizzBuzz")
        elif not c % 5:
            print("Buzz")
        elif not c % 3:
            print("Fizz")
        else:
            print(c)            
    
