#!/bin/env python3

import json
import tmdbsimple as tmdb
tmdb.API_KEY = '800fd6556557cf00577e6f28190b26a8'


# https://www.themoviedb.org/movie/920
identity = tmdb.Movies(920)
response = identity.info()
#print(response)
print(json.dumps(response, indent=4, sort_keys=True))


