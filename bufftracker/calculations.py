__author__ = 'ernir'


FORMULAS = [
    (0, "+1"),
    (1, "+2"),
    (2, "+3"),
    (3, "+4"),
    (4, "CL"),
    (5, "CL/2"),
    (6, "CL/3"),
    (7, "CL, max 10")
]


class ScalingFunctions:

    @staticmethod
    def one():
        return 1

    @staticmethod
    def two():
        return 2

    @staticmethod
    def three():
        return 3

    @staticmethod
    def four():
        return 4

    @staticmethod
    def equal(cl):
        return cl

    @staticmethod
    def one_per_two(cl):
        return cl // 2

    @staticmethod
    def one_per_three(cl):
        return cl // 3