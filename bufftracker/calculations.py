from bufftracker.hardcoded_data import CALL_MAP
from bufftracker.models import Statistic, NumericalBonus, MiscBonus


class ScalingFunctions:
    @staticmethod
    def one(cl):
        return 1

    @staticmethod
    def two(cl):
        return 2

    @staticmethod
    def three(cl):
        return 3

    @staticmethod
    def four(cl):
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

    @staticmethod
    def two_plus_one_per_three_above_three_max_5(cl):
        return min(2 + max((cl - 3) // 3, 0), 5)

    @staticmethod
    def twenty_five(cl):
        return 25

    @staticmethod
    def one_per_three_min_1_max_3(cl):
        return max(1, min(cl // 3, 3))

    @staticmethod
    def minus_two(cl):
        return -2

    @staticmethod
    def minus_one(cl):
        return -1

def parse(value_id, cl):
    scaling_function = getattr(ScalingFunctions, CALL_MAP[value_id])
    return scaling_function(cl)


def get_applicable_bonuses(cl_dict):
    """

    Calculates the total bonuses given by all selected spells, accounting for
    stacking rules.

    :param cl_dict: A dictionary with selected spell IDs as keys,
    and the CLs of each spell as values.
    :return: A dictionary with statistic IDs as keys,
    and the calculated bonuses as values.
    """
    result = {}

    selected_spell_ids = [key for key in cl_dict]

    statistics = Statistic.objects.all()

    for statistic in statistics:
        # Getting those bonuses that actually apply to the current stat
        applicable = NumericalBonus.objects.filter(applies_to=statistic)

        # The results must be broken down by modifier types.
        mod_type_dict = {}

        for bonus in applicable.all():
            for spell in bonus.spell_set.all():
                if spell.id in selected_spell_ids:
                    value = parse(bonus.bonus_value, cl_dict[spell.id])
                    type_id = bonus.modifier_type.id
                    if type_id in mod_type_dict:
                        mod_type_dict[type_id] = max(
                            mod_type_dict[type_id], value
                        )
                    else:
                        mod_type_dict[type_id] = value

        result[statistic.id] = sum(mod_type_dict.values())

    return result


def get_misc_bonuses(cl_dict):
    """

    Lists the total non-numerical bonuses given by all selected spells.

    :param cl_dict: A dictionary with selected spell IDs as keys,
    and the CLs of each spell as values.
    :return: A list of the descriptions of the spells' non-numerical bonuses.

    """

    result = set()  # Set guarantees uniqueness.

    selected_spell_ids = [key for key in cl_dict]

    bonuses = MiscBonus.objects.filter(spell__in=selected_spell_ids)

    for bonus in bonuses.all():
        result.add(bonus.description)

    return list(result)