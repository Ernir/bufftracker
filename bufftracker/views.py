from bufftracker.models import Spell, Source, StatisticGroup
from django.http import JsonResponse
from django.shortcuts import render


def index(request):
    spell_list = Spell.objects.all()
    source_list = Source.objects.all()

    return render(request, "index.html", {
        "spell_list": spell_list,
        "source_list": source_list
    })


def get_statistics(request):

    groups_query = StatisticGroup.objects
    return_dict = {}
    groups = [group.get_as_dict() for group in groups_query.all()]
    return_dict["groups"] = groups

    return JsonResponse(return_dict)