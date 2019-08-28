from swabs.models import Swab
successes = 0
failures = 0

def process_csv(filename,header,delimiter):
    global failures
    global successes
    print("Processing file: ", filename)
    print("Header status: ", header)
    print("Using delimiter: ", delimiter)
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
    return result

def test():
    return True

def add_swab(Particcipant_ID,Barcode,Week,npa_a4_growth,datecollection,
Presence_of_Pneumococcus,dob,sex,HIVexposed,site,BCG_given_birth,BCG_date_birth,DTaP_given_610wk,DTaP_date_610wk,PCV_given_610wk,PCV_date_610wk,DTaP_given_10wk,DTaP_date_10wk,DTaP_given_14wk,DTaP_date_14wk,PCV_given_14wk,PCV_date_14wk,PCV_given_9m,PCV_date_9m,Disease,Serotype_autocolour,vaccine_status_autocolour,Sequence_Type):
        # do some checks
    global failures
    global successes
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
    try:
        for i in range(len(line_list)):
            # Dates 9: 6 8 13 15 17 19 21 23 25 
            # Booleans 14: 7 10 12 14 16 18 20 22 24 26 33 34 48 51
            dates=[6,8,13,15,17,19,21,23,25]
            booleans=[7,10,12,14,16,18,20,22,24,26,33,34,48,51]
            if i in dates:
                if line_list[i]=='':
                    line_list[i]=None
            elif i in booleans:
                if line_list[i]=='':
                    line_list[i]=False
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