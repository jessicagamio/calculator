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
        # print('====== num ======',num)
        # print('====== current ======',current)
        # print('====== s_list ======',s_list)

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
                        # print('++++++  BEFORE adding calc to list+++++',s_list)
                        s_list.extend([str(calc)])
                        # print('++++++ adding calc to list+++++',s_list)
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
                        # print('popping after calc', s_list)
                        s_list.extend([str(calc)])
                        current=[]

        elif num == '*':
            # print('ready to multiply')
            for i, curr in enumerate(current[::-1]):
                if i == 0:
                    calc=curr

                else:
                    calc = calc * curr
                    # print('calc = ', calc)

                    if len(s_list)==0:
                        return calc

                    else:
                        # print('before adding calc', s_list)
                        s_list.extend([str(calc)])
                        # print('adding calc', s_list)
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
                        # print('popping after calc', s_list)
                        s_list.extend([str(calc)])
                        current=[]

# print(calc("+ 9 * 2 3"))

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED; WELL-CALCULATED! ***\n")


