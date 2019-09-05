"""
Routing handler methods for the swabs subsite
"""

from django.shortcuts import render, get_object_or_404
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

from .models import Swab


def index(request):
    """
    Renders a page of all of the current swabs paginated
    """
    swabs = Swab.objects.order_by('-Particcipant_ID')
    # select distinct
    count = len(swabs)
    paginator = Paginator(swabs, 24)
    end = paginator.count
    page = request.GET.get('page')
    paged_swabs = paginator.get_page(page)
    # ints = {1, 2, 3, 4, 5, 6, 7, 8, 9}
    end = round(end/24)

    try:
        page = int(request.GET.get('page', '1'))
    except:
        page = 1

    try:
        swabs = paginator.page(page)
    except(EmptyPage, InvalidPage):
        swabs = paginator.page(1)

    index = swabs.number - 1
    max_index = len(paginator.page_range)
    start_index = index - 3 if index >= 3 else 0
    end_index = index + 3 if index <= max_index - 3 else max_index
    page_range = list(paginator.page_range)[start_index:end_index]

    context = {
        'swabs': paged_swabs,
        'count': count,
        'end': end,
        'page_range': page_range,
    }
    return render(request, 'swabs/swabs.html', context)


def swab(request, Barcode):
    """
    Function to lookup and render a specific swab
    """
    try:
        swab = Swab.objects.get(pk=Barcode)
        context = {
            'swab': swab
        }
    except Swab.DoesNotExist:
        context={
            'not_found': 'swab'
        }
        return render(request,'404.html', context)
    
    return render(request, 'swabs/swab.html', context)
