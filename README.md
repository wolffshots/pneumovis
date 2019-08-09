# PneumoVis
Capstone Pneumococal Infection Visualisation Project - [PneumoVis](https://github.com/jadonwolffs/csc3003s-capstone)
## Implementation and releases
Click [here](http://165.73.96.80) to check out the live site

## Installation
1.  Clone the repo and navigate into it
2.  Create a new Python virtual environment
    *   `python -m venv nameofvenv` - will create a virtual environment name "nameofvenv"
3.  Activate the virtual environment 
    *   Linux and MacOS: `source nameofvenv/bin/activate`
    *   Windows: `.\nameofvenv\Scripts\activate`
4.  Navigate into the `pneumovis` directory
    *   `cd pneumovis`
5.  Install the requirements
    *   `pip install -r requirements.txt`
6.  Run the Django migrations
    *   `python manage.py migrate`
7.  Run the server
    *   `python manage.py runserver`

## Docs
*   [django](https://docs.djangoproject.com/en/2.2/)
*   [dash plotly](https://dash.plot.ly/)
*   [django-plotly-dash](https://django-plotly-dash.readthedocs.io/en/latest/index.html)

## Credits
* [A'aisha Dout](https://github.com/adout1902)
* [Kiara Beilinsohn](https://github.com/kiaraBeilinsohn)
* [Jadon Wolffs](https://github.com/jadonwolffs)

## Requirements
* [csvkit](https://github.com/wireservice/csvkit) (not included in requirements.txt, has to be set up manually)
* Django==2.2.4
* gunicorn==19.9.0
* Pillow==5.2.0
* psycopg2==2.7.5
* psycopg2-binary==2.7.5
* pytz==2019.1
* sqlparse==0.3.0
* django-plotly-dash==1.0.1

## Things to inspire
* [Information is Beautiful](https://informationisbeautiful.net/)

