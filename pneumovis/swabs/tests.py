from django.test import TestCase
from swabs.models import Swab
from pages.files import add_swab_line

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
class SwabTestCase(TestCase):
    global example_line
    example_line = ["PT0","0","-33.674530029296875","18.995084762573242","21","Growth","2013-05-28","True","2012-08-05","Male","False","Gugulethu","True","2012-08-05","True","2012-09-17","True","2012-09-17","True","2012-10-15","True","2012-11-12","True","2012-11-12","True","2013-05-20","False","13","NVT","5647","some secondary","8","House","False","False","","","","","","","Below","Below","Below","Below","Below expected Freq.","Below.","3.559999942779541","False","","Vaginal","True"]
    def setUp(self):
        pass
    def test_create(self):
        """Swabs are created successfully"""
        global example_line
        # Create swab
        add_swab_line(example_line)
        # Pull swab from DB and compare
        swabs=Swab.objects.order_by('-Particcipant_ID').filter(Particcipant_ID=example_line[0])
        for swab in swabs:
            self.assertEqual(swab.get_Particcipant_ID(), 'PT0')
            self.assertEqual(swab.get_Barcode(), '0')
    # DELETE TEST
    def test_delete(self):
        """Swabs are deleted correctly"""
        global example_line
        add_swab_line(example_line)
        # Delete swab
        Swab.objects.order_by('-Particcipant_ID').filter(Particcipant_ID=example_line[0]).delete()
        # Check DB for swab
        swabs=Swab.objects.order_by('-Particcipant_ID').filter(Particcipant_ID=example_line[0])
        for swab in swabs:
            self.assertNotEqual(swab.get_Particcipant_ID(), 'PT0')
            self.assertNotEqual(swab.get_Barcode(), '0')
