#!/usr/bin/env python3

import requests
import os
import json
#from bs4 import BeautifulSoup
import bs4 as bs
from http import cookies
import urllib.parse


def urlencode(s):
    return urllib.parse.quote(s)


def urldecode(s):
    return urllib.parse.unquote(s)

def encode_prefs(prefs):
  return urlencode(bytes(json.dumps(prefs, separators=(',', ':')), 'utf-8'))

url = 'https://www.themoviedb.org/movie/366644-little-door-gods/edit?active_nav_item=primary_facts'
headers = requests.utils.default_headers()
rawdata = os.environ['TMDB_COOKIE']
tmdb_session = os.environ['TMDB_SESSION']
#headers['cookie'] = cookie

headers['cookie'] = rawdata
cookie = cookies.SimpleCookie()
# d=urldecode(headers['cookie'])
#cookie = SimpleCookie()
cookie.load(rawdata)
# cookie.load(rawdataold)
cookies = {}
for key, morsel in cookie.items():
    cookies[key] = morsel.value
# print(cookies)
# print(headers)
tmdb_prefs = cookies['tmdb.prefs']
print(tmdb_prefs)
#j = json.loads(urldecode(tmdb_prefs))
#print(json.dumps(j, indent=4, sort_keys=True))
tmdb_prefs2 = {"adult": True, "i18n_fallback_language": "en-US",
               "locale": "fr-FR", "country_code": "FR", "timezone": "Europe/Paris"}
#print(urlencode(json.dumps(tmdb_prefs2,separators=(',', ':')), 'utf-8')))
print(encode_prefs(tmdb_prefs2))
#cookies['tmdb.prefs'] = urlencode(json.dumps(tmdb_prefs2, separators=(',', ':')), 'utf-8'))
cookies['tmdb.prefs'] = encode_prefs(tmdb_prefs2)
del cookies['_ga']
del cookies['_gali']
del cookies['_gid']
del cookies['tmdb._cookie_policy']
# del cookies['tmdb.session'] # write access !!
# del cookies['tmdb.prefs'] # default language (fr) !!
del cookies['_dc_gtm_UA-2087971-10']
print(json.dumps(cookies, indent=4, sort_keys=True))
cookie_string = "; ".join([str(x)+"="+str(y) for x, y in cookies.items()])
headers['cookie'] = cookie_string
#del headers['cookie']
r = requests.get(url, headers=headers)
soup = bs.BeautifulSoup(r.content, 'html.parser')
print(soup.prettify())
