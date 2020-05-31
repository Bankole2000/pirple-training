def compare(a, b, c):
    a, b, c = int(a), int(b), int(c)
    if a == b:
        return True
    elif a == c:
        return True
    elif b == c:
        return True
    else:
        return False


print(compare(6, 5, "5"))
