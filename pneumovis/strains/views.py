from django.shortcuts import render
from swabs.models import Swab
from django.db.models import Count
strains = Swab.objects.order_by('Serotype_autocolour').values('Serotype_autocolour').annotate(
        dcount=Count('Serotype_autocolour'))

def index(request):
    strains = Swab.objects.order_by('Serotype_autocolour').values('Serotype_autocolour').annotate(
        dcount=Count('Serotype_autocolour'))
    context = {
        'strains': strains,
    }
    return render(request, 'strains/strains.html', context)


def strain(request, Serotype_autocolour):

    Serotype_autocolour = Serotype_autocolour.replace("_", "/")
    Serotype_autocolour = Serotype_autocolour.replace("-", "(")
    Serotype_autocolour = Serotype_autocolour.replace("z", ")")

    global strains
    swabs = Swab.objects.order_by(
        '-Serotype_autocolour').filter(Serotype_autocolour=Serotype_autocolour)
    strains = Swab.objects.order_by('Serotype_autocolour').values('Serotype_autocolour').annotate(
        dcount=Count('Serotype_autocolour'))
    strain=None
    mess="No data on this strain"
    for stra in strains:
        if(stra['Serotype_autocolour'] == Serotype_autocolour):
            strain = stra
            mess = "This serotype combination appears in "+str(stra['dcount']) +" swabs"
            break
    # if(strain==None):
    #     context={
    #         'not_found': 'strain',
    #         'swabs': swabs,
    #         'Serotype_autocolour':Serotype_autocolour,
    #         'mess':mess,
    #         'strain': strain,
    #         'strains': strains,
    #     }
    #     return render(request,'pages/404.html', context)
    context = {
        'swabs': swabs,
        'Serotype_autocolour':Serotype_autocolour,
        'mess':mess,
        'strain': strain,
        'strains': strains,
    }
    return render(request, 'strains/strain.html', context)
