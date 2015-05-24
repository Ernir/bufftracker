from bufftracker.hardcoded_data import CALL_MAP
from bufftracker.models import Statistic, NumericalBonus, ModifierType


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


def parse(value_id, cl):
    scaling_function = getattr(ScalingFunctions, CALL_MAP[value_id])
    return scaling_function(cl)


def get_applicable_bonuses(cl_dict):
    result = {}

    selected_spell_ids = [key for key in cl_dict]

    statistics = Statistic.objects.all()

    for statistic in statistics:
        # Getting those bonuses that actually apply to the current stat
        applicable = NumericalBonus.objects.filter(statistic=statistic)

        # The results must be broken down by modifier types.
        mod_type_dict = {}

        for bonus in applicable.all():
            for spell in bonus.spell_set:
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