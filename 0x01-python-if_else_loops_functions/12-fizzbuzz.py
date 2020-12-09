#!/usr/bin/python3
def fizzbuzz():
    for i in range(1, 101):
        if i % 3 == 0:
            i = "Fizz"
        if i % 5 == 0:
	    i = "Buzz"
        if i % 5 and i % 3 == 0:
            i = "FizzBuzz"
        if i == 100:
            print("{}, ".format(i), end="")
        else :
            print("{}".format(i), end="")
