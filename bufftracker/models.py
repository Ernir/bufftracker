from django.db import models
from bufftracker.hardcoded_data import FORMULAS


class Source(models.Model):
    short_name = models.CharField(max_length=5)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class StatisticGroup(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def get_as_dict(self):
        """
        Returns a dictionary object representing this group.
        """
        return {
            "id": self.id,
            "name": self.name,
            "statistics": [
                stat.get_as_dict() for stat in self.statistic_set.all()
            ]
        }


class Statistic(models.Model):
    name = models.CharField(max_length=100)
    group = models.ForeignKey(StatisticGroup)

    def __str__(self):
        return self.name

    def get_as_dict(self):
        """
        Returns a dictionary object representing this statistic.
        """
        return {
            "id": self.id,
            "name": self.name
        }


class ModifierType(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class NumericalBonus(models.Model):
    bonus_value = models.IntegerField(choices=FORMULAS)
    modifier_type = models.ForeignKey(ModifierType)
    applies_to = models.ForeignKey(Statistic)

    def __str__(self):
        bonus_value = str(FORMULAS[self.bonus_value][1])
        modifier_type = self.modifier_type.name
        applies_to = self.applies_to.name
        return bonus_value + " " + modifier_type + " bonus to " + applies_to


class MiscBonus(models.Model):
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.description


class TempHPBonus(models.Model):
    die_number = models.IntegerField(choices=FORMULAS)
    die_size = models.IntegerField(default=0)
    other_bonus = models.IntegerField(choices=FORMULAS)

    def __str__(self):
        die_number = str(FORMULAS[self.die_number][1])
        die_size = str(self.die_size)
        other_bonus = str(FORMULAS[self.other_bonus][1])
        return die_number + "d" + die_size + " + " + other_bonus


class Spell(models.Model):
    name = models.CharField(max_length=100)
    source = models.ForeignKey(Source)

    numerical_bonuses = models.ManyToManyField(NumericalBonus, blank=True)
    misc_bonuses = models.ManyToManyField(MiscBonus, blank=True)
    temp_hp_bonuses = models.ManyToManyField(TempHPBonus, blank=True)

    real_spell = models.BooleanField(default=True)
    varies_by_cl = models.BooleanField(default=False)
    size_modifying = models.BooleanField(default=False)

    def __str__(self):
        return self.name