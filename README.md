cyspell2: Spell Harder
========
This is a rewriting of the CySpell project, originally authored by jsaun.

This version uses the Flask framework to implement cleaner and more modern code.It uses the Twitter Bootstrap CSS framework and assets to provide a fast but pleasing user interface. It uses the jinja2 templating library to provide consistant HTML across all pages, and so that it can be easily extended to include more pages.

Usage
========
Flask applications can be configured to run on any WSGI-capable server with Python. Since this application was not actually written for production deployment, some changes may need to be made to run it on your server.

To test this application, assuming you have Python and pip installed, install Flask 
```bash
pip install flask
```

and then simply run 
```bash
python index.py
```
