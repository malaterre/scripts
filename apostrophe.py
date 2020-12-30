#!/bin/env python3

import json
import os
import requests
import tmdbsimple as tmdb
tmdb.API_KEY = '800fd6556557cf00577e6f28190b26a8'
tmdb.debug = True


auth = tmdb.Authentication()
token = auth.token_new()["request_token"]

password = os.environ['TMDB_PASS']
auth.token_validate_with_login(
    request_token=token, username="malaterre", password=password)
session_id = auth.session_new(request_token=token)["session_id"]
acc = tmdb.Account(session_id)
# print(acc.info())
print(session_id)
#s = auth.session_new()
# print(s)
# account = tmdb.Account()

#movies = []
#idx = 1
# while True:
#    res = acc.rated_movies()
#    movies = movies + res["results"]
#    idx = idx + 1
#    if idx > res["total_pages"]:
#        break
#
#print(json.dumps(movies, indent=2))

# https://www.themoviedb.org/movie/920
identity = tmdb.Movies(336313)
response = identity.info(language='fr-FR')
print(json.dumps(response, indent=4, sort_keys=True))
overview_old = response['overview']
overview_new = overview_old.replace("'", "’")


headers = {
    'authority': 'www.themoviedb.org',
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'x-requested-with': 'XMLHttpRequest',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'origin': 'https://www.themoviedb.org',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://www.themoviedb.org/movie/9836-happy-feet/edit?active_nav_item=primary_facts',
    'accept-language': 'fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7',
    'cookie': 'tmdb.prefs=%7B%22adult%22%3Atrue%2C%22i18n_fallback_language%22%3A%22en-US%22%2C%22locale%22%3A%22fr-FR%22%2C%22country_code%22%3A%22FR%22%2C%22timezone%22%3A%22Europe%2FParis%22%7D; tmdb._cookie_policy=true; _ga=GA1.2.514487234.1609250614; _gid=GA1.2.310921039.1609250614; _dc_gtm_UA-2087971-10=1; tmdb.session=ASpqFhZ_ocD0h3sT41QWBclUDTVriwZvFWVsO3DWpcZJZK13vu0wmBN4aiWKA0T1XpFk0d8yCzfV8uu9KMAg9e2Ne7Of76VaaJtJJus9oIY4U_ASix0SvFQad7_ZWoB4vveDZg7_hGL146_EJJc-UP7iPTSYYsyQar5AllB3e0tLmOxky2b6rzYOrtVmVsa4aqU9HX4qqAgnkSimR33eH-lm2iD8u1duo-Kp-LCu5YiIqYhHCkxlX6htEdTW-zpv-ZxmnuL0lRNJGEuviueYulmNlgJQF3XgpRdluI7a8wEjUPDJbl1j6Ow9EiHuxEVoSv7TqKJPVmLSEE0Nqof6tnUR_OWmq4Sw0NtDiuJjVhJfMYPRAjwOr7Xwqa3SefDpVw-DtJQOuH9_6Cb5BTsN4lmIE7ciPcsMWgtBrWncNGF49ypJduOwtuBP5Y_cQdMkOYkEqWao5Xy3UMF3-f77rj-DiSQ0w1_D06N5cwkcji6XjoI9dxVsZLpnPy414x4gLrcK9CEZL7y0zSwim9F4F_Vk8ffL7W9bZqwMjhzkSDLakrhz6nrXyi_yRuLx91WJICUh8Ry8f7PdlcSOEdbli31e623p3AGe_96NDt9avhEyKW1erg5T1Dt8G_w9t2j2Zxi0ZXYDXW6mPRKmWPi7nTUeiForE8W0kZ10Peue0cTR5XERWxUZUkIlq34IpoghuWXE_fRURglZ6dy_9T9ExE8315GerDJjKozJXVIXh2XMmzB9e0t91BSuSc2saaIcFkQZaxtl0hDnMUwVXArB8tRAH1M19H48D8UlKYRxd58fsgRMO2gG_nAWCwhSRLkaz4NdzkbJrhkQypNzldjA4j_B14fGbrvVf_RsION4Evft; _gali=submit',
}

data = {
#    '$fr_FR_translated_title': 'Happy Feet',
#    'fr_FR_tagline': 'Chaque manchot a une chanson... Mais Mumble n\'est pas un manchot comme les autres',
    'fr_FR_overview': 'Un manchot de l\u2019Antarctique n\'arrivera jamais \xE0 rien s\'il ne sait pas chanter, et le pauvre Mumble est sans conteste le pire chanteur du monde. Son talent \xE0 lui, c\'est... les claquettes, qu\'il pratique en virtuose, avec une ardeur confondante.Bien que sa maman, Norma Jean, trouve ce don "tout \xE0 fait charmant", son p\xE8re, Memphis, juge que "\xE7a ne fait vraiment pas pingouin". Tous deux savent aussi que leur rejeton ne trouvera l\'\xE2me soeur que le jour o\xF9 il saura pousser son "chant d\'amour". Le hasard fait bien les choses : Gloria, la seule et unique amie de notre h\xE9ros, est la meilleure chanteuse de la r\xE9gion. Mumble et elle sont copains depuis toujours, bien que cette gracieuse cr\xE9ature ait encore du mal \xE0 accepter son \xE9trange "anomalie".Banni de la tribu, Mumble se lie avec les Amigos de Terre Ad\xE9lie, un groupe latino exub\xE9rant, men\xE9 par Ramon...',
#    'fr_FR_runtime': '108',
#    'budget': '100000000',
#    'fr_FR_homepage': '',
#    'spoken_languages[]': 'en'
}

#response = requests.post(
#    'https://www.themoviedb.org/movie/9836-happy-feet/remote/primary_facts', headers=headers, data=data)


# curl 'https://www.themoviedb.org/movie/9836-happy-feet/remote/primary_facts' \
#  -H 'authority: www.themoviedb.org' \
#  -H 'accept: application/json, text/javascript, */*; q=0.01' \
#  -H 'x-requested-with: XMLHttpRequest' \
#  -H 'user-agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36' \
#  -H 'content-type: application/x-www-form-urlencoded; charset=UTF-8' \
#  -H 'origin: https://www.themoviedb.org' \
#  -H 'sec-fetch-site: same-origin' \
#  -H 'sec-fetch-mode: cors' \
#  -H 'sec-fetch-dest: empty' \
#  -H 'referer: https://www.themoviedb.org/movie/9836-happy-feet/edit?active_nav_item=primary_facts' \
#  -H 'accept-language: fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7' \
#  -H 'cookie: tmdb.prefs=%7B%22adult%22%3Atrue%2C%22i18n_fallback_language%22%3A%22en-US%22%2C%22locale%22%3A%22fr-FR%22%2C%22country_code%22%3A%22FR%22%2C%22timezone%22%3A%22Europe%2FParis%22%7D; tmdb._cookie_policy=true; _ga=GA1.2.514487234.1609250614; _gid=GA1.2.310921039.1609250614; _dc_gtm_UA-2087971-10=1; tmdb.session=ASpqFhZ_ocD0h3sT41QWBclUDTVriwZvFWVsO3DWpcZJZK13vu0wmBN4aiWKA0T1XpFk0d8yCzfV8uu9KMAg9e2Ne7Of76VaaJtJJus9oIY4U_ASix0SvFQad7_ZWoB4vveDZg7_hGL146_EJJc-UP7iPTSYYsyQar5AllB3e0tLmOxky2b6rzYOrtVmVsa4aqU9HX4qqAgnkSimR33eH-lm2iD8u1duo-Kp-LCu5YiIqYhHCkxlX6htEdTW-zpv-ZxmnuL0lRNJGEuviueYulmNlgJQF3XgpRdluI7a8wEjUPDJbl1j6Ow9EiHuxEVoSv7TqKJPVmLSEE0Nqof6tnUR_OWmq4Sw0NtDiuJjVhJfMYPRAjwOr7Xwqa3SefDpVw-DtJQOuH9_6Cb5BTsN4lmIE7ciPcsMWgtBrWncNGF49ypJduOwtuBP5Y_cQdMkOYkEqWao5Xy3UMF3-f77rj-DiSQ0w1_D06N5cwkcji6XjoI9dxVsZLpnPy414x4gLrcK9CEZL7y0zSwim9F4F_Vk8ffL7W9bZqwMjhzkSDLakrhz6nrXyi_yRuLx91WJICUh8Ry8f7PdlcSOEdbli31e623p3AGe_96NDt9avhEyKW1erg5T1Dt8G_w9t2j2Zxi0ZXYDXW6mPRKmWPi7nTUeiForE8W0kZ10Peue0cTR5XERWxUZUkIlq34IpoghuWXE_fRURglZ6dy_9T9ExE8315GerDJjKozJXVIXh2XMmzB9e0t91BSuSc2saaIcFkQZaxtl0hDnMUwVXArB8tRAH1M19H48D8UlKYRxd58fsgRMO2gG_nAWCwhSRLkaz4NdzkbJrhkQypNzldjA4j_B14fGbrvVf_RsION4Evft; _gali=submit' \
#  --data-raw $'fr_FR_translated_title=Happy+Feet&fr_FR_tagline=Chaque+manchot+a+une+chanson...+Mais+Mumble+n\'est+pas+un+manchot+comme+les+autres&fr_FR_overview=Un+manchot+de+l%E2%80%99Antarctique+n\'arrivera+jamais+%C3%A0+rien+s\'il+ne+sait+pas+chanter%2C+et+le+pauvre+Mumble+est+sans+conteste+le+pire+chanteur+du+monde.+Son+talent+%C3%A0+lui%2C+c\'est...+les+claquettes%2C+qu\'il+pratique+en+virtuose%2C+avec+une+ardeur+confondante.Bien+que+sa+maman%2C+Norma+Jean%2C+trouve+ce+don+%22tout+%C3%A0+fait+charmant%22%2C+son+p%C3%A8re%2C+Memphis%2C+juge+que+%22%C3%A7a+ne+fait+vraiment+pas+pingouin%22.+Tous+deux+savent+aussi+que+leur+rejeton+ne+trouvera+l\'%C3%A2me+soeur+que+le+jour+o%C3%B9+il+saura+pousser+son+%22chant+d\'amour%22.+Le+hasard+fait+bien+les+choses+%3A+Gloria%2C+la+seule+et+unique+amie+de+notre+h%C3%A9ros%2C+est+la+meilleure+chanteuse+de+la+r%C3%A9gion.+Mumble+et+elle+sont+copains+depuis+toujours%2C+bien+que+cette+gracieuse+cr%C3%A9ature+ait+encore+du+mal+%C3%A0+accepter+son+%C3%A9trange+%22anomalie%22.Banni+de+la+tribu%2C+Mumble+se+lie+avec+les+Amigos+de+Terre+Ad%C3%A9lie%2C+un+groupe+latino+exub%C3%A9rant%2C+men%C3%A9+par+Ramon...&fr_FR_runtime=108&budget=100000000&fr_FR_homepage=&spoken_languages%5B%5D=en' \
#  --compressed
