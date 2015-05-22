from django.db import models


class Source(models.Model):

    short_name = models.CharField(max_length=5)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Spell(models.Model):

    name = models.CharField(max_length=100)
    source = models.ForeignKey(Source)

    real_spell = models.BooleanField(default=True)
    varies_by_cl = models.BooleanField(default=False)
    size_modifying = models.BooleanField()
