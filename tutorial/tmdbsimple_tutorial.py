import tmdbsimple as tmdb

tmdb.API_KEY = '454b6ca4172e455fe7a7d8395c10d6d9'

search = tmdb.Search()

response = search.movie(query='Aliens.mkv')['results']

import pprint

pprint.pprint(response, indent=4)

"https://image.tmdb.org/t/p/original/r1x5JGpyqZU8PYhbs4UcrO1Xb6x.jpg"