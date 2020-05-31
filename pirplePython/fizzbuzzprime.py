"""
File: fizzbuzzprime.py V1.0
Auth: Bankole Esan
Desc: Pirple.com Python Homework #5
Task: fizz buzz prime
"""
import time
timeout = .3  # set timeout length
Fizz = "Fizz"  # set Fizz word
Buzz = "Buzz"  # set Buzz word
Prime = "Prime"  # set Prime word


def isPrimeNumber(arg):
    if arg >= 2:
        for i in range(2, arg):
            if arg % i == 0:
                return False
    else:
        return False
    return True


for i in range(1, 101):
    if isPrimeNumber(i):
        print(Prime)
        time.sleep(timeout)
        continue
    if (i % 3 == 0) and (i % 5 == 0):
        print(Fizz + Buzz)
        time.sleep(timeout)
        continue
    if i % 3 == 0:
        print(Fizz)
        time.sleep(timeout)
        continue
    if i % 5 == 0:
        print(Buzz)
        time.sleep(timeout)
        continue
    print(i)
    time.sleep(timeout)
