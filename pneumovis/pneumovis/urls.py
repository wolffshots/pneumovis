"""
The url routing patterns for the lowest level of pages of the site from the root
"""
from django.contrib import admin
from django.urls import path, include   # include is necessary to be added

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pages.urls')),
    path('swabs/', include('swabs.urls')),
    path('participants/', include('participants.urls')),
    path('strains/', include('strains.urls')),
    path('django_plotly_dash/', include('django_plotly_dash.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  # this allows the urls to register the media files
