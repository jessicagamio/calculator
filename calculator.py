"""Calculator

    >>> calc("+ 1 2")  # 1 + 2
    3

    >>> calc("* 2 + 1 2")  # 2 * (1 + 2)
    6

    >>> calc("+ 9 * 2 3")   # 9 + (2 * 3)
    15

Let's make sure we have non-commutative operators working:

    >>> calc("- 1 2")  # 1 - 2
    -1

    >>> calc("- 9 * 2 3")  # 9 - (2 * 3)
    3

    >>> calc("/ 6 - 4 2")  # 6 / (4 - 2)
    3
"""



def calc(s):
    """Evaluate expression."""

    # create symbols string
    symbol = '*/+-'
    # convert s to list
    s_list = s.split(' ')
    # set current as a empty list
    current = []

    # while s_list has a value keep looping
    while s_list:

        # pop the last item in the list
        num = s_list.pop()

        # if not an operator append number as an int to current list
        if num not in symbol:
            current.append(int(num))
           
        # if operator is + add each element in current list
        elif num == '+':
            for i, curr in enumerate(current[::-1]):
                if i == 0:
                    calc=curr

                else:
                    calc += curr

                    if len(s_list) == 0:
                        return calc

                    else:

                        s_list.extend([str(calc)])
                        current=[]

        elif num == '-':
            for i, curr in enumerate(current[::-1]):
                if i == 0:
                    calc=curr

                else:
                    calc =  calc - curr

                    if len(s_list)==0:
                        return calc

                    else:
                        s_list.extend([str(calc)])
                        current=[]

        elif num == '*':
           
            for i, curr in enumerate(current[::-1]):
                if i == 0:
                    calc=curr

                else:
                    calc = calc * curr

                    if len(s_list)==0:
                        return calc

                    else:
                        s_list.extend([str(calc)])
                        current=[]        

        elif num == '/':
            for i, curr in enumerate(current[::-1]):
                if i == 0:
                    calc=curr

                else:
                    calc = calc // curr

                    if len(s_list)==0:
                        return calc

                    else:
                        s_list.extend([str(calc)])
                        current=[]



if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED; WELL-CALCULATED! ***\n")


