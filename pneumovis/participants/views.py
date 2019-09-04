from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound
from swabs.models import Swab
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import render
from django.db.models import Count

# Create your views here.
participants = Swab.objects.order_by('Particcipant_ID').values('Particcipant_ID').annotate(
    dcount=Count('Particcipant_ID'))
hivs = Swab.objects.order_by('Particcipant_ID').values(
    'Particcipant_ID').annotate(dcount=Count('HIVexposed'))
# print(hivs)


def index(request):
    global participants
    participants = Swab.objects.order_by('Particcipant_ID').values('Particcipant_ID').annotate(
        dcount=Count('Particcipant_ID'))

    # print(participants)
    count = len(participants)
    paginator = Paginator(participants, 24)
    end = paginator.count
    page = request.GET.get('page')
    paged_participants = paginator.get_page(page)
    end = round(end/24)

    try:
        page = int(request.GET.get('page', '1'))
    except:
        page = 1

    try:
        participants = paginator.page(page)
    except(EmptyPage, InvalidPage):
        participants = paginator.page(1)

    index = participants.number - 1
    max_index = len(paginator.page_range)
    start_index = index - 3 if index >= 3 else 0
    end_index = index + 3 if index <= max_index - 3 else max_index
    page_range = list(paginator.page_range)[start_index:end_index]

    context = {
        'participants': paged_participants,
        'count': count,
        'end': end,
        'page_range': page_range,
    }
    return render(request, 'participants/participants.html', context)


def participant(request, Particcipant_ID):
    # implement custom 404 page
    global participants
    swabs = Swab.objects.order_by(
        '-Particcipant_ID').filter(Particcipant_ID=Particcipant_ID)
    participants = Swab.objects.order_by('Particcipant_ID').values('Particcipant_ID').annotate(
        dcount=Count('Particcipant_ID'))
    participant = None
    for part in participants:
        if(part['Particcipant_ID'] == Particcipant_ID):
            participant = part
            break
        # return 404
    if(participant==None):
        context={
            'not_found': 'participant'
        }
        return render(request,'404.html', context)
    context = {
        'swabs': swabs,
        'participant': participant
    }
    return render(request, 'participants/participant.html', context)
