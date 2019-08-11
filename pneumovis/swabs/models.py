from django.db import models
from datetime import datetime

# Create your models here.


class Swab(models.Model):
    """
    Test docstring
    """
    # id =
    # Particcipant_ID = participent model #models.CharField(max_length=300)
    # Particcipant_ID	
    # Barcode	Week	
    # npa_a4_growth	
    # datecollection	
    # Presence_of_Pneumococcus	
    # dob	sex	HIVexposed	site	
    # BCG_given_birth	BCG_date_birth
    # DTaP_given_610wk	
    # DTaP_date_610wk	
    # PCV_given_610wk	
    # PCV_date_610wk	
    # DTaP_given_10wk	
    # DTaP_date_10wk	
    # DTaP_given_14wk	
    # DTaP_date_14wk	
    # PCV_given_14wk	
    # PCV_date_14wk	
    # PCV_given_9m	
    # PCV_date_9m	
    # Disease
    # Serotype__autocolour	
    # vaccine_status__autocolour	
    # Sequence_Type
    # Particcipant_ID	
    # Barcode	
    # Week	
    # npa_a4_growth	
    # datecollection	
    # Presence_of_Pneumococcus	
    # dob	
    # sex	
    # HIVexposed	
    # site	
    # BCG_given_birth	
    # BCG_date_birth	
    # DTaP_given_610wk	
    # DTaP_date_610wk	
    # PCV_given_610wk	
    # PCV_date_610wk	
    # DTaP_given_10wk	
    # DTaP_date_10wk	
    # DTaP_given_14wk	
    # DTaP_date_14wk	
    # PCV_given_14wk	
    # PCV_date_14wk	
    # PCV_given_9m	
    # PCV_date_9m	
    # Disease	
    # Serotype__autocolour	
    # vaccine_status__autocolour	
    # Sequence_Type

    # photo = models.ImageField(upload_to='photos/%Y/%m/%d')
    # desc = models.TextField(blank=True)
    # phone = models.CharField(max_length=20)
    # email = models.CharField(max_length=100)
    # mvp = models.BooleanField(default=False)
    # hire_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):  # this is the primary field that is displayed similar to a toString
        return self.patient
