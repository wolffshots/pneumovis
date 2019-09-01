# #these two lines and the part of the program that distinguishes it as a django-ised version of plotly


# Importing from the app definitions
# import sys
# sys.path.insert(1, 'pages/dash_apps_dir')
from pages.dash_app_dir import incidence
from pages.dash_app_dir import bubbles
from pages.dash_app_dir import map
from pages.dash_app_dir import patients
print("Imported Dash apps")
