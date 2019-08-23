from django.contrib import admin

# Register your models here.
from .models import Swab


class SwabAdmin(admin.ModelAdmin):
    list_display = ('Particcipant_ID', 'Barcode')
    list_display_links = ('Barcode',)
    search_fields = ('Particcipant_ID', 'Barcode')


admin.site.register(Swab, SwabAdmin)
