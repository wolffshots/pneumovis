from django.test import TestCase
from pages.dash_app_dir import bubbles, patients, map, incidence
import pandas as pd



# test figure is correctly made given valid input and excception raised for invalid input      

class bubblesTestCase(TestCase):
   def test_makeFigure_valid_entry_smoking(self):
      try:
         bubbles.makeFigure("Smoking")
      except Exception:
         self.fail("unexpected exception raised")
         # test will fail if any exception raised during making of HIV exposure graph

   def test_makeFigure_valid_entry_HIV(self):
      try:
         bubbles.makeFigure("HIV")
      except Exception:
         self.fail("unexpected exception raised")
         # test will fail if any exception raised during making of HIV exposure graph

   def test_makeFigure_invalid_entry(self):
        with self.assertRaises(Exception) as context:
            bubbles.makeFigure("InvalidInput")
            self.assertTrue('Invalid x axis variable' in context.exception)

         # test will fail if an exception is NOT raised when an invalid input is entered
   
class patientsTestCase(TestCase):
   def test_gen_graph_valid_df(self):
      df = pd.DataFrame(pd.read_csv('patientData.csv'))
      try:
         patients.gen_graph(df)
      except Exception:
         self.fail("unexpected exception raised")
         # test will fail if any exception raised during making of valid graph (non-empty dataframe with correct data given)

   def test_gen_graph_empty_df(self):
      df=pd.DataFrame()
      with self.assertRaises(Exception) as context:
         patients.gen_graph(df)
         self.assertTrue('Empty dataframe' in context.exception)

class mapTestCase(TestCase):
   def test_gen_map_valid_df(self):
      map_data = pd.read_csv("mapSwabs.csv")
      try:
         map.gen_map(map_data)
      except Exception:
         self.fail("unexpected exception raised")
         # test will fail if any exception raised during making of valid map (non-empty dataframe with correct data given)

   def test_gen_graph_empty_df(self):
      map_data=pd.DataFrame()
      with self.assertRaises(Exception) as context:
         map.gen_map(map_data)
         self.assertTrue('Empty dataframe' in context.exception)




