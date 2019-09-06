from django.test import TestCase
from pages.dash_app_dir import bubbles, patients, map, incidence
from pages import views
import pandas as pd
from django.contrib import messages, auth
from django.shortcuts import render, redirect
from django.http import HttpRequest

from django.urls import reverse

from django.test import TestCase
from django.test.client import Client
from django.contrib.auth.models import User
# reverse resolves a view name + its args into a path, used to avoid hardcoding urls in tests


# Visualisation Unit Tests  

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
      df = pd.DataFrame(pd.read_csv('static/data/patientData.csv'))
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
      map_data = pd.read_csv("static/data/mapSwabs.csv")
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


# Views Tests


# simple view tests of main pages to check correct access patterns
# mock user, check correct status (200=OK) received when attempting to access html page 
class loginViewCase(TestCase):

   def setUp(self):
      self.client = Client()
   
   def test_invalid_user(self):
      url = reverse('login')
      response = self.client.get(url)
     
      self.assertEqual(response.status_code, 200)
      self.assertTemplateUsed(response, 'pages/login.html')

class browseViewCase(TestCase):

   def setUp(self):
      self.client = Client()
   
   def test_invalid_user(self):
      url = reverse('browse')
      response = self.client.get(url)
     
      self.assertEqual(response.status_code, 200)
      self.assertTemplateUsed(response, 'pages/browse.html')

class aboutTestCase(TestCase):

   def setUp(self):
      self.client = Client()
   
   def test_invalid_user(self):
      url = reverse('about')
      response = self.client.get(url)
     
      self.assertEqual(response.status_code, 200)
      self.assertTemplateUsed(response, 'pages/about.html')



# test login process by creating users and checking correct response to valid and invalid credentials
class TestAccountLogin(TestCase):
   def setUp(self):
      self.client = Client()

   def test_login_valid_credentials(self):
      user = User.objects.create_user('testuser', '[some email]', 'password')
      response = self.client.login(username=user.username, password=user.password)
      self.assertTrue(user.is_authenticated)

   def test_login_valid_credentials(self):
      user = User.objects.create_user('testuser', '[some email]', 'password')
      response = self.client.login(username="invalidorincorrect", password="invalidorincorrect")
      self.assertTrue(user.is_authenticated)