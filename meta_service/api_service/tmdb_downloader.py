import tmdbsimple as tmdb

class APIService: # == APIService(object)
    # ez szenzitív adat, egy production ready
    # rendszerben ezt nem így kell megvalósítani
    # így nem biztonságos
    tmdb.API_KEY = '454b6ca4172e455fe7a7d8395c10d6d9'

    def __init__(self):
        # SOLID priciples -> ez ellent mond a D-nek: Dependancy inversion
        self.search = tmdb.Search()

    def get_meta_by_title(self, title):
        return self.search.movie(query=title)['results'][0]


if __name__ == '__main__':
    test = APIService()

    meta = test.get_meta_by_title('Aliens')

    print(meta)


