"""
The url routes for navigating to pages in the /participants subroute
"""

from django.urls import path
from . import views
from swabs.models import Swab
from django.db.models import Count

participants = Swab.objects.order_by('Particcipant_ID').values('Particcipant_ID').annotate(
    dcount=Count('Particcipant_ID'))
urlpatterns = [
    path('', views.index, name='participants'),
    path('<slug:Particcipant_ID>', views.participant, name='participant'),
]
