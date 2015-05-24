from bufftracker.models import Spell, Source
from django.shortcuts import render


def index(request):
    spell_list = Spell.objects.all()
    source_list = Source.objects.all()

    return render(request, "index.html", {
        "spell_list": spell_list,
        "source_list": source_list
    })
