"""
Itt lesz megvalósítva a teljes flowja a letöltésnek / tárolásnak
"""
from meta_service.file_service.file_handler import FileHandler
from meta_service.file_service.params import meta_params
from meta_service.api_service.tmdb_downloader import APIService

from meta_service.db_service.initial_scripts import db_tables
from meta_service.db_service.postgre_service import PostgreHandler

from meta_service.db_service.sql_helper import (select_meta,
                                                insert_meta,
                                                insert_genre_ids,
                                                del_genre,
                                                del_meta)


def downloader ():
    url = "postgresql://postgres:postgres@localhost:5432/postgres"

    file = FileHandler(meta_params)
    api = APIService()
    sql= PostgreHandler(url, db_tables)

    movie = file.get_movies_from_folder(meta_params['movie_folder'])
    meta = [item[0] for item in sql.run_query(query=select_meta,is_select=True).fetchall()]
   
    need_to_delete = [item for item in meta if item not in movie]
    need_to_download = [item for item in movie if item not in meta]
    
    for item in need_to_delete:
        image_path=f"{meta_params['poster_folder']}/{item}.jpg"

        sql.run_query(del_genre.format(movie=item))
        sql.run_query(del_meta.format(movie=item))

        file.remove_file(image_path)

    for movie in need_to_download:
        data=api.get_meta_by_title(movie)

        data ['original_title'] = movie

        sql.run_query(insert_meta, data)

        ids = []
        for item in data ['genre_ids']:
            ids.append({
                "meta_id": data['id'],
                "genre_id": item
            })

        sql.run_query(insert_genre_ids, ids)
        
        image_path=f"{meta_params['poster_folder']}/{movie}.jpg"
        file.write_poster_image(image_path=image_path,poster_path=data['poster_path'])

if __name__=="__main__":
    downloader()
