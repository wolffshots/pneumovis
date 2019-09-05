"""
A helper file to process files (especially the csv file for upload). This process happens in parallel.
"""
from swabs.models import Swab
from django.http import HttpResponse
from django.shortcuts import render, redirect

from django.contrib import messages, auth
from django.contrib.auth.models import User

from django.db.models import Count

from django.conf import settings
from django.core.files.storage import FileSystemStorage

successes = 0
failures = 0
delimiter = ''

<<<<<<< HEAD
def process_csv(filename,header,d):
=======
def process_csv(filename,header,delim):
>>>>>>> 4c30aa1ff8914ccd784cef1fa1f9ff014cb47837
    global failures
    global successes
    global delimiter
    print("Processing file: ", filename)
    print("Header status: ", header)
    print("Using delimiter: ", delim)
    delimiter = delim
    provided_file = open(filename, "r")
    # lines = provided_file.read()
    if delimiter == 'comma':
        delimiter=','
    elif delimiter == 'space':
        delimiter=' '
    elif delimiter == 'semicolon':
        delimiter=';'
    for line in provided_file: 
        if(not header):
            line_list = [part.strip() for part in line.split(delimiter)]
            add_swab_line(line_list)
        else:
            header = False
    result = {'s': successes,
              'f': failures}

    provided_file.close() 
    messages.info(request, 'Successfully made ' + str(result['s'])+' new entries and failed to make '+str(result['f'])+' entries')
    context = {'uploaded_file_url': uploaded_file_url}
    # return result
    return render(request, 'pages/upload.html',context)

# def test():
#     return True

def add_swab(Particcipant_ID,Barcode,Week,npa_a4_growth,datecollection,
Presence_of_Pneumococcus,dob,sex,HIVexposed,site,BCG_given_birth,BCG_date_birth,DTaP_given_610wk,DTaP_date_610wk,PCV_given_610wk,PCV_date_610wk,DTaP_given_10wk,DTaP_date_10wk,DTaP_given_14wk,DTaP_date_14wk,PCV_given_14wk,PCV_date_14wk,PCV_given_9m,PCV_date_9m,Disease,Serotype_autocolour,vaccine_status_autocolour,Sequence_Type):
        # do some checks
    global failures
    global successes
    global delimiter
    try:
        swab = Swab(    Particcipant_ID=Particcipant_ID,
                        Barcode=Barcode,
                        Week=Week,
                        npa_a4_growth=npa_a4_growth,
                        datecollection=datecollection,
                        Presence_of_Pneumococcus=Presence_of_Pneumococcus,
                        dob=dob,
                        sex=sex,
                        HIVexposed=HIVexposed,
                        site=site,
                        BCG_given_birth=BCG_given_birth,
                        BCG_date_birth=BCG_date_birth,
                        DTaP_given_610wk=DTaP_given_610wk,
                        DTaP_date_610wk=DTaP_date_610wk,
                        PCV_given_610wk=PCV_given_610wk,
                        PCV_date_610wk=PCV_date_610wk,
                        DTaP_given_10wk=DTaP_given_10wk,
                        DTaP_date_10wk=DTaP_date_10wk,
                        DTaP_given_14wk=DTaP_given_14wk,
                        DTaP_date_14wk=DTaP_date_14wk,
                        PCV_given_14wk=PCV_given_14wk,
                        PCV_date_14wk=PCV_date_14wk,
                        PCV_given_9m=PCV_given_9m,
                        PCV_date_9m=PCV_date_9m,
                        Disease=Disease,
                        Serotype_autocolour=Serotype_autocolour,
                        vaccine_status_autocolour=vaccine_status_autocolour,
                        Sequence_Type=Sequence_Type
                        )
        swab.save()
        successes += 1
    except Exception as e: 
        print("Error adding user - ",e)
        failures += 1


def add_swab_line(line_list):
    global failures
    global successes
    global delimiter
    try:
        for i in range(len(line_list)):
            # Dates 9: 6 8 13 15 17 19 21 23 25 
            # Booleans 14: 7 10 12 14 16 18 20 22 24 26 33 34 48 51
            dates=[6,8,13,15,17,19,21,23,25]
            booleans=[7,10,12,14,16,18,20,22,24,26,33,34,48,51]
            ints =[4,]
            doubles=[47,]
            if i in dates:
                if line_list[i]=='':
                    line_list[i]=None
            elif i in booleans:
                if line_list[i]=='':
                    line_list[i]=False
            elif i in ints:
                if '.0' in line_list[i]:
                    line_list[i]=line_list[i][:-2]
            elif i in doubles:                    
                if ',' in line_list[i]:
                    split_list=ine_list[i].split(",")
                    '.'.join(split_list)
            elif line_list[i]=='':
                    line_list[i]=None
        swab = Swab(Particcipant_ID=line_list[0],
                    Barcode=line_list[1],
                    geo_lat=line_list[2],
                    geo_long=line_list[3],
                    Week=line_list[4],
                    npa_a4_growth=line_list[5],
                    datecollection=line_list[6],
                    Presence_of_Pneumococcus=line_list[7],
                    dob=line_list[8],
                    sex=line_list[9],
                    HIVexposed=line_list[10],
                    site=line_list[11],
                    BCG_given_birth=line_list[12],
                    BCG_date_birth=line_list[13],
                    DTaP_given_610wk=line_list[14],
                    DTaP_date_610wk=line_list[15],
                    PCV_given_610wk=line_list[16],
                    PCV_date_610wk=line_list[17],
                    DTaP_given_10wk=line_list[18],
                    DTaP_date_10wk=line_list[19],
                    DTaP_given_14wk=line_list[20],
                    DTaP_date_14wk=line_list[21],
                    PCV_given_14wk=line_list[22],
                    PCV_date_14wk=line_list[23],
                    PCV_given_9m=line_list[24],
                    PCV_date_9m=line_list[25],
                    Disease=line_list[26],
                    Serotype_autocolour=line_list[27],
                    vaccine_status_autocolour=line_list[28],
                    Sequence_Type=line_list[29],
                    education =line_list[30],
                    HHdsize=line_list[31],
                    HomeType=line_list[32],
                    Paraffin_stove=line_list[33],
                    Coal_stove=line_list[34],
                    BenzeneCat=line_list[35],
                    TolueneCat=line_list[36],
                    SO2Cat=line_list[37],
                    NO2Cat=line_list[38],
                    CO_Strict=line_list[39],
                    CO_Broad=line_list[40],
                    SO2Cat_Post=line_list[41],
                    NO2Cat_Post=line_list[42],
                    BenzeneCat_post=line_list[43],
                    TolueneCat_post=line_list[44],
                    CO_Strict_post=line_list[45],
                    CO_Broad_post=line_list[46],
                    weight_birth=line_list[47],
                    mother_smoke_anytime=line_list[48],
                    total_smokers_anytime=line_list[49],
                    delivery_method=line_list[50],
                    antibio_use_1yr=line_list[51],
                    )
        swab.save()
        successes += 1
    except Exception as e: 
        print("Error adding user - ",e)
        failures += 1