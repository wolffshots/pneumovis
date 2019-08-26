from swabs.models import Swab


def process_csv(filename,header,delimiter):
    successes = 0
    failures = 0
    print("Processing file: ", filename)
    print("Using delimiter: ", delimiter)
    lines = open(filename, "r")
    for i in range(10):
        if(test()): # TODO change to process actual lines
            successes += 1
        else:
            failures += 1
    result = {'s': successes,
              'f': failures}
    return result

def test():
    return True

def add_swab(Particcipant_ID,Barcode,Week,npa_a4_growth,datecollection,
Presence_of_Pneumococcus,dob,sex,HIVexposed,site,BCG_given_birth,BCG_date_birth,DTaP_given_610wk,DTaP_date_610wk,PCV_given_610wk,PCV_date_610wk,DTaP_given_10wk,DTaP_date_10wk,DTaP_given_14wk,DTaP_date_14wk,PCV_given_14wk,PCV_date_14wk,PCV_given_9m,PCV_date_9m,Disease,Serotype_autocolour,vaccine_status_autocolour,Sequence_Type):
        # do some checks
    swab = Swab(Particcipant_ID=Particcipant_ID,
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
    return True
