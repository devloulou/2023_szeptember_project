"""
Itt lesz megvalósítva a teljes flowja a letöltésnek / tárolásnak.
"""
from meta_service.file_service.file_handler import FileHandler
from meta_service.file_service.params import meta_params

from meta_service.api_service.tmdb_downloader import APIService

def downloader():
    file = FileHandler(meta_params)
    api = APIService()

    movies = file.get_movies_from_folder()

    for movie in movies:        
        data = api.get_meta_by_title(movie)
        file_path = f"{meta_params['meta_folder']}/{movie}.json"

        file.write_meta_json(file_path=file_path, meta_data=data)


if __name__ == '__main__':
    downloader()
