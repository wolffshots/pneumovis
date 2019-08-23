from django.shortcuts import render, get_object_or_404
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
# from .choices import price_choices, bedroom_choices, state_choices

from .models import Swab


def index(request):
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
    # print(Barcode)
    swab = get_object_or_404(Swab, pk=Barcode)
    context = {
        'swab': swab
    }
    return render(request, 'swabs/swab.html', context)
