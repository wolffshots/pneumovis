@echo off
echo Some modules have import errors
python -m pydoc -w pneumovis
python -m pydoc -w pneumovis.pages
python -m pydoc -w pneumovis.pages.admin
python -m pydoc -w pneumovis.pages.apps
python -m pydoc -w pneumovis.pages.dash_app
python -m pydoc -w pneumovis.pages.migrations
python -m pydoc -w pneumovis.pages.models
python -m pydoc -w pneumovis.pages.tests
python -m pydoc -w pneumovis.pages.urls
python -m pydoc -w pneumovis.pages.views
echo Finished writing pages submodules
python -m pydoc -w pneumovis.manage
python -m pydoc -w pneumovis.pneumovis
echo skipping writing for local_settings for privacy
python -m pydoc -w pneumovis.pneumovis.settings
python -m pydoc -w pneumovis.pneumovis.urls
python -m pydoc -w pneumovis.pneumovis.wsgi
echo Finished writing pneumovis submodules
python -m pydoc -w pneumovis.swabs
python -m pydoc -w pneumovis.swabs.admin
python -m pydoc -w pneumovis.swabs.apps
python -m pydoc -w pneumovis.swabs.migrations
python -m pydoc -w pneumovis.swabs.models
python -m pydoc -w pneumovis.swabs.tests
python -m pydoc -w pneumovis.swabs.views