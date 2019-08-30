from django.contrib import admin

# Register your models here.
from .models import Swab


class SwabAdmin(admin.ModelAdmin):
    list_display = ('Barcode', 'Particcipant_ID', 'datecollection', 'Week', 'site')
    list_display_links = ('Barcode',)
    search_fields = ('Particcipant_ID', 'Barcode')
    list_per_page = 30
    empty_value_display = 'No data'
    list_filter = ('site', 'datecollection')

    fieldsets = (
        (None, {
            'fields': ('Barcode', 'Particcipant_ID', 'Week', 'npa_a4_growth', 'datecollection', 'Presence_of_Pneumococcus', 'dob', 'sex', 'HIVexposed', 'site', 'Disease', 'Serotype_autocolour', 'vaccine_status_autocolour', 'Sequence_Type')
        }),
        ('Vaccine details', {
            'classes': ('collapse',),
            'fields': ('BCG_given_birth', 'BCG_date_birth', 'DTaP_given_610wk', 'DTaP_date_610wk', 'PCV_given_610wk', 'PCV_date_610wk', 'DTaP_given_10wk', 'DTaP_date_10wk', 'DTaP_given_14wk', 'DTaP_date_14wk', 'PCV_given_14wk', 'PCV_date_14wk', 'PCV_given_9m', 'PCV_date_9m'),
        }),
    )


admin.site.register(Swab, SwabAdmin)
