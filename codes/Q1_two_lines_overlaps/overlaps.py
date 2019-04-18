"""
Question A:
Your goal for this question is to write a program that accepts two lines (x1,x2) and (x3,x4) on the x-axis and
returns whether they overlap. As an example, (1,5) and (2,6) overlaps but not (1,5) and (6,8).
"""


def main():
    # set line_1 and line_2
    x1 = is_number(input('Please enter x1 of line_1: '))
    x2 = is_number(input('Please enter x2 of line_1: '))
    x3 = is_number(input('Please enter x3 of line_2: '))
    x4 = is_number(input('Please enter x4 of line_2: '))
    line_1 = (x1, x2)
    line_2 = (x3, x4)
    print("line_1 is " + str(line_1) + ", line_2 is " + str(line_2))

    # output result
    is_overlaps(line_1, line_2)


# check whether two lines overlap
def is_overlaps(line_1, line_2):
    try:
        if max(line_1) < min(line_2) or max(line_2) < min(line_1):
            print(str(line_1) + "and " + str(line_2) + " NOT overlaps.")
        else:
            print(str(line_1) + "and " + str(line_2) + " overlaps.")
    except TypeError:
        print("ERROR: The type of input must be int or float type.")


# verify whether the string input is a number or not
# if it is a number, return the number of float type
# if not, input again
def is_number(str):
    try:
        f = float(str)
    except ValueError:
        f = is_number(input("\'" + str + "\'" + " is not a number! Please input again:"))
    return f


if __name__ == "__main__":
    test_case = (
        ((1, 2), (7, 8)),
        ((1, 6), (6, 9)),
        ((1, 5), (4, 7)),
        ((1, 8), (3, 6)),
        ((4, 6), (2, 9)),
        ((5, 9), (2, 6)),
        ((5, 9), (1, 5)),
        ((6, 7), (3, 4)),
        ((1.5, 8.4), (3, 6.4)),
        ((1.5, 8.4), ("abc", 6.4)),
        ((0, 0), (0, 0)),
        ((-1, -9), (-3, -8)),
        ((-2, -5), (-4, -10)),
        ((-1, -4), (5, 7))
    )
    for case in test_case:
        is_overlaps(case[0], case[1])

    print("\nTest yourself :)")

    main()
