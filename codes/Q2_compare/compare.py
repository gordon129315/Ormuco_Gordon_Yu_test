"""
Question B:
The goal of this question is to write a software library that accepts 2 version string as input and
returns whether one is greater than, equal, or less than the other. As an example: “1.2” is greater than “1.1”.
Please provide all test cases you could think of.
"""

class comparison:
    def __init__(self, input_1, input_2):
        try:
            self.input_1 = input_1
            self.input_2 = input_2
            self.value_1 = float(input_1)
            self.value_2 = float(input_2)
        except ValueError:
            print("ERROR: Input is illegal, both inputs have to be number.")
            exit(-1)

    def compare(self):
        if self.value_1 < self.value_2:
            print("\"%s\" is lower than \"%s\"" % (self.input_1, self.input_2))
        elif self.value_1 > self.value_2:
            print("\"%s\" is greater than \"%s\"" % (self.input_1, self.input_2))
        else:
            print("\"%s\" is equal to \"%s\"" % (self.input_1, self.input_2))


# test
if __name__ == "__main__":
    test_case = (
        ("1.2", "1.1"),
        ("1.1", "1.2"),
        ("1.1", "1.1"),
        ("4", "4.0"),
        ("abc", "2")
    )
    for case in test_case:
        c = comparison(case[0], case[1])
        c.compare()
