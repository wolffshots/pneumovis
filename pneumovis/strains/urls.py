"""
Routing paths for the strains subsite
"""

from django.urls import path
from . import views
from swabs.models import Swab
from django.db.models import Count

# participants = Swab.objects.order_by('Particcipant_ID').values('Particcipant_ID').annotate(
#     dcount=Count('Particcipant_ID'))
urlpatterns = [
    path('', views.index, name='strains'),
    path('<slug:Serotype_autocolour>', views.strain, name='strain'),
]
