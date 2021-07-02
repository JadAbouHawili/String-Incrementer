'''increment_string function definition'''


import re


def increment_string(strng):
    '''
    increment_string(value)
    type(value) is str

    What the function does:
    The breif logic of the two algorithms the function chooses from which are based under the first if, else statement respectively:
    Takes a string and increments its end number (if exists) by adding 1 to it and returns the resultant as string ( leading zeros are considered and contribute to the length of the output
    Takes a string and increments it by appending '1' to the end if no number is present and returns the resultant string
    '''
    num_match = re.search(r'\d+$', strng)
    lst = list(strng)
    # keep count of current index in strng
    counter = -1
    # the first algorithm
    if num_match:
        original_num_slice = num_match.group()

        # check from right to left
        for i in strng:

            # keep count of current index in strng
            counter += 1

            # until hit first digit of number (number is at end of string)
            if i.isdigit():

                # check if end of string is a bunch of nines
                if ''.join(lst[counter:]) == '9'*len(lst[counter:]):
                    lst[counter:] = str(int(''.join(lst[counter:]))+1)
                    return ''.join(lst)

                # incrementing the number part at the end of the string by 1
                lst[counter:] = str(int(''.join(lst[counter:]))+1)
                incremented_num_slice = re.search(
                    r'\d+$', ''.join(lst)).group()

                # checking length of original and incremented num_slice and adjusting the '0' count accordingly

                if len(incremented_num_slice) < len(original_num_slice):
                    lst[counter:] = (
                        ['0']*(len(original_num_slice)-len(incremented_num_slice)))+lst[counter:]
                    return ''.join(lst)
                if len(incremented_num_slice) > len(original_num_slice):
                    lst[counter:] = list(''.join(lst[counter:]).replace('0', '', len(
                        incremented_num_slice)-len(original_num_slice)))
                    return ''.join(lst)

                # no need for changes in '0' count
                else:

                    return ''.join(lst)

    # The Second Algorithm
    # There are no digits at the end of strng
    else:
        return strng+'1'


# tests to verify algorithm works as described ( in github description )
print('foobar: '+increment_string('foobar'), 'foobar001 :'+increment_string('foobar001'), 'foobar010: '+increment_string('foobar010'), 'foobar100: '+increment_string('foobar100'),
      'foobar0100: '+increment_string('foobar0100'), 'foobar9: '+increment_string('foobar9'), 'foobar09: '+increment_string('foobar09'), 'foobar009: '+increment_string('foobar009'), sep='\n')
