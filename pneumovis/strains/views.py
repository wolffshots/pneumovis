from django.shortcuts import render
from swabs.models import Swab
from django.db.models import Count


def index(request):
    strains = Swab.objects.order_by('Serotype_autocolour').values('Serotype_autocolour').annotate(
        dcount=Count('Serotype_autocolour'))
    context = {
        'strains': strains,
    }
    return render(request, 'strains/strains.html', context)


def strain(request, Serotype_autocolour):
    # uppercase the serotype
    # replace certain characters for '(' and '/'
    global strains
    swabs = Swab.objects.order_by(
        '-Serotype_autocolour').filter(Serotype_autocolour=Serotype_autocolour)
    strains = Swab.objects.order_by('Serotype_autocolour').values('Serotype_autocolour').annotate(
        dcount=Count('Serotype_autocolour'))

    for stra in strains:
        if(stra['Serotype_autocolour'] == Serotype_autocolour):
            strain = stra
            break
        # return 404
    context = {
        'swabs': swabs,
        'strain': strain,
        'strains': strains,
    }
    return render(request, 'strains/strain.html', context)
