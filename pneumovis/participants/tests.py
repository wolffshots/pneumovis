"""
Runs tests to ensure that the model for swabs works with participants, is created, read and deleted correctly
"""

from django.test import TestCase
from swabs.models import Swab
from pages.files import add_swab_line
from django.db.models import Count
from django.shortcuts import render, get_object_or_404

# FORMAT
# class AnimalTestCase(TestCase):
#     def setUp(self):
#         Animal.objects.create(name="lion", sound="roar")
#         Animal.objects.create(name="cat", sound="meow")

#     def test_animals_can_speak(self):
#         """Animals that can speak are correctly identified"""
#         lion = Animal.objects.get(name="lion")
#         cat = Animal.objects.get(name="cat")
#         self.assertEqual(lion.speak(), 'The lion says "roar"')
#         self.assertEqual(cat.speak(), 'The cat says "meow"')

# CREATE TEST
class ParticipantTestCase(TestCase):
    global example_line 
    global example_line2
    global example_line3
    example_line = ["PT0","0","-33.674530029296875","18.995084762573242","21","Growth","2013-05-28","True","2012-08-05","Male","False","Gugulethu","True","2012-08-05","True","2012-09-17","True","2012-09-17","True","2012-10-15","True","2012-11-12","True","2012-11-12","True","2013-05-20","False","13","NVT","5647","some secondary","8","House","False","False","","","","","","","Below","Below","Below","Below","Below expected Freq.","Below.","3.559999942779541","False","","Vaginal","True"]
    example_line2 = ["PT0","1","-33.674530029296875","18.995084762573242","21","Growth","2013-05-28","True","2012-08-05","Male","False","Gugulethu","True","2012-08-05","True","2012-09-17","True","2012-09-17","True","2012-10-15","True","2012-11-12","True","2012-11-12","True","2013-05-20","False","13","NVT","5647","some secondary","8","House","False","False","","","","","","","Below","Below","Below","Below","Below expected Freq.","Below.","3.559999942779541","False","","Vaginal","True"]
    example_line3 = ["PT1","2","-33.674530029296875","18.995084762573242","21","Growth","2013-05-28","True","2012-08-05","Male","False","Gugulethu","True","2012-08-05","True","2012-09-17","True","2012-09-17","True","2012-10-15","True","2012-11-12","True","2012-11-12","True","2013-05-20","False","13","NVT","5647","some secondary","8","House","False","False","","","","","","","Below","Below","Below","Below","Below expected Freq.","Below.","3.559999942779541","False","","Vaginal","True"]
    def setUp(self):
        pass
    def test_create(self):
        """Participants are created successfully"""
        global example_line 
        global example_line2
        global example_line3
        # Create part
        add_swab_line(example_line)
        add_swab_line(example_line2)
        add_swab_line(example_line3)
        # Pull part from DB and compare
        participants=Swab.objects.order_by('Particcipant_ID').values('Particcipant_ID').annotate(dcount=Count('Particcipant_ID'))
        # for part in participants:
        self.assertEqual(participants[0]['Particcipant_ID'], 'PT0')
        self.assertEqual(participants[0]['dcount'], 2)
        self.assertEqual(participants[1]['Particcipant_ID'], 'PT1')
        self.assertEqual(participants[1]['dcount'], 1)
    # DELETE TEST
    def test_delete(self):
        """Particpants are deleted correctly"""
        global example_line
        global example_line2
        add_swab_line(example_line)
        add_swab_line(example_line2)
        add_swab_line(example_line3)
        # Delete part
        # Swab.objects.order_by('-Particcipant_ID').filter(Barcode=example_line2[1]).delete()
        # instance = Swab.objects.get(pk=)
        swab = get_object_or_404(Swab, pk=example_line2[1])
        swab.delete()
        # Check DB for part
        participants=Swab.objects.order_by('Particcipant_ID').values('Particcipant_ID').annotate(dcount=Count('Particcipant_ID'))
        # Make sure the first participant is decremented
        self.assertEqual(participants[0]['Particcipant_ID'], 'PT0')
        self.assertEqual(participants[0]['dcount'], 1)
        # Make sure the other participant is not affected
        self.assertEqual(participants[1]['Particcipant_ID'], 'PT1')
        self.assertEqual(participants[1]['dcount'], 1)
