#!/usr/bin/python3
for num in range(100):
    if num < 10:
        num = str(num)
        num ='0' + num
    sprt = ", "
    if num == 99:
        sprt = ""
    print("{}{}".format(num, sprt), end="")
print('\n')
