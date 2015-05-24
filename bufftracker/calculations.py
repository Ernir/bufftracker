from bufftracker.models import Statistic

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


def get_applicable_bonuses(cl_dictionary):

    result = {}

    selected_spell_ids = [key for key in cl_dictionary]

    statistics = Statistic.objects.all()

    for statistic in statistics:
        pass