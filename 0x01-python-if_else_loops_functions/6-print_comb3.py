#!/usr/bin/python3
for digit1 in range(0, 10):
    for digit2 in range(digit1 + 1, 10):
        if digit1 == 8 and digit2 == 9:
            print("{}{}".format(digit1, digit2))
        else:
#!/usr/bin/python3
            print("{}{}".format(digit1, digit2), end=", ")
