from django.shortcuts import render
from .models import AssurancePlan, Partenaires, Testimonial, Team


def index(request):
    context = {
        'assurances': AssurancePlan.objects.all(),
        'partenaires': Partenaires.objects.all(),
        'temoignages': Testimonial.objects.all()[:5]
    }
    return render(request, 'main/index.html', context)


def about(request):

    context = {
        "team": Team.objects.all()
    }
    return render(request, 'main/apropos.html', context)


def contact(request):

    if request.method == "POST":
        name = request.POST['name']
        return render(request, 'main/contact.html', {'name': name})

    else:
        return render(request, 'main/contact.html', None)


def plan(request, id):
    try:
        plan = AssurancePlan.objects.get(id=id)
        return render(request, 'main/plan.html', context={'plan': plan})
    except:
        return render(request, 'main/plan.html', context={'nofound': True})
