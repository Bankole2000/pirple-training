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
        print(f"{i} is a Prime Number")
