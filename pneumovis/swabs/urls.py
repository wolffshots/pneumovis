from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='swabs'),
    # directs user to about page when /about
    # this is how to include an id
    path('<int:Barcode>', views.swab, name='swab'),
    # path('search', views.search, name='search'),
]
