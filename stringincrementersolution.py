# make proper modifications to this document stating what it does doc strings, comment it properly, refactor some code, provide clearer strcuture using comments and other methods etc...
'''
increment_string(value)
type(value) is str

What the program does:
Takes a string and increments its end number (if exists) by adding 1 to it, leading zeros are considered and contribute to the length of the output
Takes a string and increments it by appending '1' to the end if no number is present.
'''
import re


def increment_string(strng):
    # use regular expression to find a match at the end of the string(use $ at the end of pattern) for digit characters
    num_match = re.search(r'\d+$', strng)
    lst = list(strng)

    counter = -1
    if num_match:
        digits = num_match.group()

       # check from right to left until hit a number that isn't zero
        for i in strng:
            counter += 1
            if i.isdigit():
                if ''.join(lst[counter:]) == '9'*len(lst[counter:]):
                    lst[counter:] = str(int(''.join(lst[counter:]))+1)
                    return ''.join(lst)

                lst[counter:] = str(int(''.join(lst[counter:]))+1)
                if len(re.search(r'\d+$', ''.join(lst)).group()) < len(num_match.group()):
                    lst[counter:] = (
                        ['0']*(len(num_match.group())-len(re.search(r'\d+$', ''.join(lst)).group())))+lst[counter:]
                    return ''.join(lst)

                if len(re.search(r'\d+$', ''.join(lst)).group()) > len(num_match.group()):
                    lst[counter:] = list(''.join(lst[counter:]).replace('0', '', len(
                        re.search(r'\d+$', ''.join(lst)).group())-len(num_match.group())))
                    # here lies the problem
                    # current logic counter-... in the below is not working
                    # counter not useful because it gives number and after it, the added 0not detected when replacing, therefore wrong output
                    return ''.join(lst)

                else:

                    return ''.join(lst)

    else:
        return strng+'1'


print(increment_string('foobar'), increment_string('foobar001'), increment_string('foobar010'), increment_string('foobar100'),
      increment_string('foobar0100'), increment_string('foobar9'), increment_string('foobar09'), increment_string('foobar009'))
