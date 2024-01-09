select_meta = """
select original_title from meta
"""

insert_meta = """
insert into meta
    (adult,
    backdrop_path,
    id,
    original_language,
    original_title,
    overview,
    popularity,
    poster_path,
    release_date,
    title,
    video,
    vote_average,
    vote_count)
values (
    :adult,
    :backdrop_path,
    :id,
    :original_language,
    :original_title,
    :overview,
    :popularity,
    :poster_path,
    :release_date,
    :title,
    :video,
    :vote_average,
    :vote_count
)
"""

insert_genre_ids = """
insert into genre_ids (
    meta_id,
    genre_id)
values (
    :meta_id,
    :genre_id
)
"""

del_genre = """
delete from genre_ids
where meta_id = (select id from meta
			where original_title = '{movie}')"""
			
del_meta = """
delete from meta where original_title = '{movie}'
"""