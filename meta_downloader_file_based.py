"""
Itt lesz megvalósítva a teljes flowja a letöltésnek / tárolásnak.
"""
from meta_service.file_service.file_handler import FileHandler
from meta_service.file_service.params import meta_params

from meta_service.api_service.tmdb_downloader import APIService

def downloader():
    file = FileHandler(meta_params)
    api = APIService()

    movies = file.get_movies_from_folder(meta_params['movie_folder'])
    meta = file.get_movies_from_folder(meta_params['meta_folder'])

    need_to_delete = [item for item in meta if item not in movies]
    need_to_download = [item for item in movies if item not in meta]

    print(f"need_to_delete: {need_to_delete}")
    print(f"need_to_download: {need_to_download}")

    for item in need_to_delete:
        image_path = f"{meta_params['poster_folder']}/{item}.jpg"
        meta_path = f"{meta_params['meta_folder']}/{item}.json"

        file.remove_file(image_path)
        file.remove_file(meta_path)

    for movie in need_to_download:        
        data = api.get_meta_by_title(movie)
        file_path = f"{meta_params['meta_folder']}/{movie}.json"

        file.write_meta_json(file_path=file_path, meta_data=data)

        image_path = f"{meta_params['poster_folder']}/{movie}.jpg"
        file.write_poster_image(image_path=image_path, poster_path=data['poster_path'])

if __name__ == '__main__':
    downloader()
