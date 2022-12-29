import json


default_locale="en-gb"
cached_string={}

def refresh():
    global cached_string
    with open(f"strings/{default_locale}.json") as f:
        cached_string=json.load(f)
def gettext(name):
    return cached_string[name]



refresh()

