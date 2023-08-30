"""
File: class_reviews.py
Name: Janelle Lin
-------------------------------
At the beginning of this program, the user is asked to input
the class name (either SC001 or SC101).
Attention: your input should be case-insensitive.
If the user input "-1" for class name, your program would show
the maximum, minimum, and average among all the inputs.
"""

END = '-1'


def main():
    """
    :input: the information of each student's class and corresponding scores,
    :return: get the Max, min, and average score of each class
    """

    count_001 = count_101 = total_001 = total_101 = 0

    # To set the starting values
    max_001 = float('-inf')  # as small as it can be
    min_001 = float('inf')  # as large as it can be
    max_101 = -float('inf')
    min_101 = float('inf')

    while True:
        cls = input('Which class? ').upper()
        if cls == END:
            break

        scr = int(input('Score: '))

        if cls == 'SC001':
            if scr > max_001:
                max_001 = scr
            if scr < min_001:
                min_001 = scr
            total_001 += scr
            count_001 += 1

        if cls == 'SC101':
            if scr > max_101:
                max_101 = scr
            if scr < min_101:
                min_101 = scr
            total_101 += scr
            count_101 += 1

    if total_001 == 0 and total_101 == 0:
        print('No class scores were entered')

    else:   # print out results
        print('=============SC001=============')
        if total_001 == 0:
            print('No score for SC001')
        else:
            print('Max (001): ' + str(max_001))
            print('Min (001): ' + str(min_001))
            print('Avg (001): ' + str(total_001/count_001))

        print('=============SC101=============')
        if total_101 == 0:
            print('No score for SC101')
        else:
            print('Max (101): ' + str(max_101))
            print('Min (101): ' + str(min_101))
            print('Avg (101): ' + str(total_101 / count_101))


# ---- DO NOT EDIT CODE BELOW THIS LINE ---- #

if __name__ == '__main__':
    main()
