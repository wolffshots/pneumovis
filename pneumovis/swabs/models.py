"""
The model of the swabs recorded at clinics
"""

from django.db import models
from datetime import datetime


class Swab(models.Model):
    """
    The swab class represents the entries in the DB
    """
    Particcipant_ID = models.CharField(max_length=10) #0
    Barcode = models.CharField(max_length=20, primary_key=True) #1
    geo_lat = models.CharField(max_length=20, null=True, blank=True) #2
    geo_long = models.CharField(max_length=20, null=True, blank=True) #3
    Week = models.IntegerField()#4
    npa_a4_growth = models.CharField(max_length=10, blank=True, null=True)#5
    datecollection = models.DateField()#6
    Presence_of_Pneumococcus = models.BooleanField(default=False,blank=True,null=True)#7
    dob = models.DateField()#8
    sex = models.CharField(max_length=6)#9
    HIVexposed = models.BooleanField(default=False, blank=True, null=True)#10
    site = models.CharField(max_length=100)#11
    BCG_given_birth = models.BooleanField(default=False, blank=True, null=True)#12
    BCG_date_birth = models.DateField(blank=True, null=True)#13
    DTaP_given_610wk = models.BooleanField(default=False, blank=True, null=True)#14
    DTaP_date_610wk = models.DateField(blank=True, null=True)#15
    PCV_given_610wk = models.BooleanField(default=False, blank=True, null=True)#16
    PCV_date_610wk = models.DateField(blank=True, null=True)#17
    DTaP_given_10wk = models.BooleanField(default=False, blank=True, null=True)#18
    DTaP_date_10wk = models.DateField(blank=True, null=True)#19
    DTaP_given_14wk = models.BooleanField(default=False, blank=True, null=True)#20
    DTaP_date_14wk = models.DateField(blank=True, null=True)#21
    PCV_given_14wk = models.BooleanField(default=False, blank=True, null=True)#22
    PCV_date_14wk = models.DateField(blank=True, null=True)#23
    PCV_given_9m = models.BooleanField(default=False, blank=True, null=True)#24
    PCV_date_9m = models.DateField(blank=True, null=True)#25
    Disease = models.BooleanField(default=False, blank=True, null=True)#26
    Serotype_autocolour = models.CharField(max_length=15, blank=True, null=True)#27
    vaccine_status_autocolour = models.CharField(max_length=5, blank=True, null=True)#28
    Sequence_Type = models.CharField(max_length=10, blank=True, null=True)#29
    education = models.CharField(max_length=20, blank=True, null=True)#30
    HHdsize = models.FloatField(blank=True, null=True)#31
    HomeType = models.CharField(max_length=28, blank=True, null=True)#32
    Paraffin_stove = models.BooleanField(blank=True, null=True)#33
    Coal_stove = models.BooleanField(blank=True, null=True)#34
    BenzeneCat = models.CharField(max_length=10, blank=True, null=True)#35
    TolueneCat = models.CharField(max_length=10, blank=True, null=True)#36
    SO2Cat = models.CharField(max_length=10, blank=True, null=True)#37
    NO2Cat = models.CharField(max_length=10, blank=True, null=True)#38
    CO_Strict = models.CharField(max_length=21, blank=True, null=True)#39
    CO_Broad = models.CharField(max_length=10, blank=True, null=True)#40
    SO2Cat_Post = models.CharField(max_length=10, blank=True, null=True)#41
    NO2Cat_Post = models.CharField(max_length=10, blank=True, null=True)#42
    BenzeneCat_post = models.CharField(max_length=10, blank=True, null=True)#43
    TolueneCat_post = models.CharField(max_length=10, blank=True, null=True)#44
    CO_Strict_post = models.CharField(max_length=21, blank=True, null=True)#45
    CO_Broad_post = models.CharField(max_length=10, blank=True, null=True)#46
    weight_birth = models.FloatField(default=-1, null=True, blank=True)#47
    mother_smoke_anytime = models.BooleanField(default=False, blank=True, null=True)#48
    total_smokers_anytime = models.CharField(max_length=10, blank=True, null=True)#49
    delivery_method = models.CharField(max_length=10, blank=True, null=True)#50
    antibio_use_1yr = models.BooleanField(default=False, blank=True, null=True)#51

    # photo = models.ImageField(upload_to='photos/%Y/%m/%d') # - can have this for serotypes

    def __str__(self):  # this is the primary field that is displayed similar to a toString
        """ Returns the barcode value for the current swap as that is the unique value for each swab """
        return str(self.Barcode)
