"""
The model of the swabs recorded at clinics
"""

from django.db import models
from datetime import datetime

# Create your models here.


class Swab(models.Model):
    """
    The swab class represents the entries in the DB
    """
    Particcipant_ID = models.CharField(max_length=10)
    Barcode = models.CharField(max_length=20, primary_key=True)
    geo_lat = models.CharField(
        max_length=20, null=True, blank=True)
    geo_long = models.CharField(
        max_length=20, null=True, blank=True)
    Week = models.IntegerField()
    npa_a4_growth = models.CharField(
        max_length=10, blank=True, null=True)  # Growth or No Growth
    datecollection = models.DateField()
    Presence_of_Pneumococcus = models.BooleanField(
        default=False, blank=True, null=True)
    dob = models.DateField()
    sex = models.CharField(max_length=6)
    HIVexposed = models.BooleanField(blank=True, null=True)
    site = models.CharField(max_length=100)
    BCG_given_birth = models.BooleanField(default=False, blank=True, null=True)
    BCG_date_birth = models.DateField(blank=True, null=True)
    DTaP_given_610wk = models.BooleanField(
        default=False, blank=True, null=True)
    DTaP_date_610wk = models.DateField(blank=True, null=True)
    PCV_given_610wk = models.BooleanField(default=False, blank=True, null=True)
    PCV_date_610wk = models.DateField(blank=True, null=True)
    DTaP_given_10wk = models.BooleanField(default=False, blank=True, null=True)
    DTaP_date_10wk = models.DateField(blank=True, null=True)
    DTaP_given_14wk = models.BooleanField(default=False, blank=True, null=True)
    DTaP_date_14wk = models.DateField(blank=True, null=True)
    PCV_given_14wk = models.BooleanField(default=False, blank=True, null=True)
    PCV_date_14wk = models.DateField(blank=True, null=True)
    PCV_given_9m = models.BooleanField(default=False, blank=True, null=True)
    PCV_date_9m = models.DateField(blank=True, null=True)
    Disease = models.BooleanField(default=False, blank=True, null=True)
    Serotype_autocolour = models.CharField(
        max_length=15, blank=True, null=True)
    vaccine_status_autocolour = models.CharField(
        max_length=5, blank=True, null=True)
    Sequence_Type = models.CharField(max_length=10, blank=True, null=True)
    education = models.CharField(max_length=20, blank=True, null=True)
    HHdsize = models.FloatField(blank=True, null=True)
    HomeType = models.CharField(max_length=28, blank=True, null=True)
    Paraffin_stove = models.BooleanField(blank=True, null=True)
    Coal_stove = models.BooleanField(blank=True, null=True)
    BenzeneCat = models.CharField(max_length=10, blank=True, null=True)
    TolueneCat = models.CharField(max_length=10, blank=True, null=True)
    SO2Cat = models.CharField(max_length=10, blank=True, null=True)
    NO2Cat = models.CharField(max_length=10, blank=True, null=True)
    CO_Strict = models.CharField(max_length=21, blank=True, null=True)
    CO_Broad = models.CharField(max_length=10, blank=True, null=True)
    SO2Cat_Post = models.CharField(max_length=10, blank=True, null=True)
    NO2Cat_Post = models.CharField(max_length=10, blank=True, null=True)
    BenzeneCat_post = models.CharField(max_length=10, blank=True, null=True)
    TolueneCat_post = models.CharField(max_length=10, blank=True, null=True)
    CO_Strict_post = models.CharField(max_length=21, blank=True, null=True)
    CO_Broad_post = models.CharField(max_length=10, blank=True, null=True)
    weight_birth = models.FloatField(default=-1, null=True, blank=True)
    mother_smoke_anytime = models.BooleanField(blank=True, null=True)
    total_smokers_anytime = models.CharField(
        max_length=10, blank=True, null=True)
    delivery_method = models.CharField(max_length=10, blank=True, null=True)
    antibio_use_1yr = models.BooleanField(blank=True, null=True)

    # photo = models.ImageField(upload_to='photos/%Y/%m/%d') # - can have this for serotypes

    def __str__(self):  # this is the primary field that is displayed similar to a toString
        """ Returns the barcode value for the current swap as that is the unique value for each swab """
        return str(self.Barcode)
