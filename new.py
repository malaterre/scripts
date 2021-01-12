#!/usr/bin/env python3

import argparse
import requests
import os
import json
#from bs4 import BeautifulSoup
import bs4 as bs
#from http import cookies
import urllib.parse


def extract_form_fields(soup):
    "Turn a BeautifulSoup form in to a dict of fields and default values"
    fields = {}
    # for input in soup.findAll('input'):
    pff = soup.find(id='primary_facts_form')
    #  print(input)
    # for input in pff.find(id='primary_facts_form')
    for input in pff.findAll('input'):
        # pff = pff.find(id='primary_facts_form'):
        # ignore submit/image with no name attribute
        if not 'type' in input:
            continue
        if input['type'] in ('submit', 'image') and not 'name' in input:
            continue

        # single element nome/value fields
        if input['type'] in ('text', 'hidden', 'password', 'submit', 'image'):
            value = ''
            if 'value' in input:
                value = input['value']
            fields[input['name']] = value
            continue

        # checkboxes and radios
        if input['type'] in ('checkbox', 'radio'):
            value = ''
            if input.has_attr("checked"):
                if input.has_attr('value'):
                    value = input['value']
                else:
                    value = 'on'
            if 'name' in input and value:
                fields[input['name']] = value

            if not 'name' in input:
                fields[input['name']] = value

            continue

        assert False, 'input type %s not supported' % input['type']

    # textareas
    for textarea in soup.findAll('textarea'):
        fields[textarea['name']] = textarea.string or ''

    # select fields
    for select in soup.findAll('select'):
        value = ''
        options = select.findAll('option')
        is_multiple = select.has_attr('multiple')
        selected_options = [
            option for option in options
            if option.has_attr('selected')
        ]

        # If no select options, go with the first one
        if not selected_options and options:
            selected_options = [options[0]]

        if not is_multiple:
            assert(len(selected_options) < 2)
            if len(selected_options) == 1:
                value = selected_options[0]['value']
        else:
            value = [option['value'] for option in selected_options]

        fields[select['name']] = value

    return fields


def urlencode(s):
    return urllib.parse.quote(s)


def urldecode(s):
    return urllib.parse.unquote(s)


def encode_prefs(prefs):
    return urlencode(bytes(json.dumps(prefs, separators=(',', ':')), 'utf-8'))


def get_location(url):
    response = requests.head(url, allow_redirects=True)
    return response.url


def main(args):
    verbose = args.verbose
    movie_id = args.movie_id
    lang = args.lang

    # url = 'https://www.themoviedb.org/movie/366644-little-door-gods/edit?active_nav_item=primary_facts'
    root_url = 'https://www.themoviedb.org/movie/'
    #    'referer': 'https://www.themoviedb.org/movie/9836-happy-feet/edit?active_nav_item=primary_facts',
    url = get_location(root_url + str(movie_id)) + \
        '/edit?active_nav_item=primary_facts'
    if verbose:
        print(referer)

    headers = requests.utils.default_headers()
    tmdb_session = os.environ['TMDB_SESSION']

    cookies = {}
    tmdb_prefs = {"adult": True, "i18n_fallback_language": "en-US",
                  "locale": "fr-FR", "country_code": "FR", "timezone": "Europe/Paris"}
    cookies['tmdb.prefs'] = encode_prefs(tmdb_prefs)
    # cookies['tmdb.session'] # write access !!
    cookies['tmdb.session'] = tmdb_session
    # cookies['tmdb.prefs'] # default language (fr) !!
    cookie_string = "; ".join([str(x)+"="+str(y) for x, y in cookies.items()])
    headers['cookie'] = cookie_string
    r = requests.get(url, headers=headers)
    soup = bs.BeautifulSoup(r.content, 'html.parser')
    # print(soup.prettify())
    # print(soup.find(id='primary_facts_form'))
    ret = extract_form_fields(soup)
    print(ret)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="tmdb typo")
    parser.add_argument("movie_id", help='movie id')
    #
    parser.add_argument("--dry-run",
                        help="dry run", action='store_true')
    # verbose
    parser.add_argument("--lang",
                        help="verbose output", action='store_true')
    parser.add_argument("--verbose",
                        help="verbose output", action='store_true')
    main(parser.parse_args())
