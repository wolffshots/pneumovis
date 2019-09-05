"""
This is essentially a directory of the apps that django-plotly-dash should be able to see. This is imported into the main views.py thereby running it and it imports the specific charts, running them in parallel.
"""
# Importing from the app definitions
from pages.dash_app_dir import incidence
from pages.dash_app_dir import bubbles
from pages.dash_app_dir import map
from pages.dash_app_dir import patients
# from pages.dash_app_dir import patientGraph
print("Imported Dash apps")
