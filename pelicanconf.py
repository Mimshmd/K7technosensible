AUTHOR = 'Myriam Hammad'
SITENAME = 'K7 technosensible'
SITEURL = 'http://127.0.0.1:8000'
PATH = 'content'
TIMEZONE = 'Europe/Paris'



DEFAULT_LANG = 'fr'

FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

OUTPUT_PATH = "output/"

STATIC_PATHS = ['images', 'audio']
# EXTRA_PATH_METADATA = {
#     'extra/custom.css': {'path': 'theme/css/custom.css'},
#     'extra/main.css': {'path': 'theme/css/main.css'},
# }


DEFAULT_SORT_BY = 'date'


PAGE_PATHS = ['pages']


LINKS = (
    ("Pelican", "https://getpelican.com/"),
    ("Python.org", "https://www.python.org/"),
    ("Jinja2", "https://palletsprojects.com/p/jinja/"),
)

SOCIAL = (
    ("Twitter", "https://twitter.com/yourprofile"),
    ("GitHub", "https://github.com/yourprofile"),
)
SITEURL = ''

MARKDOWN = {
    'extensions': [
        'markdown.extensions.extra',
        'markdown.extensions.codehilite',
        'markdown.extensions.toc',
        'markdown.extensions.tables',
        'markdown.extensions.smarty',
    ]
}

DEFAULT_PAGINATION = False

THEME = 'theme/notmyidea-cms'

CUSTOM_CSS = 'notmyidea-cms/static/css/main.css'
DISPLAY_CATEGORIES_ON_MENU = True

