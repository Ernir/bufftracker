from bufftracker.calculations import get_applicable_bonuses
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


def calculate_bonuses(request):
    if request.method == "GET":
        cl_dict = request.GET
        numerical_bonuses = get_applicable_bonuses(cl_dict)

        content = {
            "numerical": numerical_bonuses,
            "misc": None
        }

        return JsonResponse({
            "content": content,
            "status": 200,
            "message": "OK"
        })
