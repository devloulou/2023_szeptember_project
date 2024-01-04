from collections import OrderedDict

movies_cre_table = f"""
create table meta(
adult boolean,
backdrop_path varchar(50),
id integer primary key,
original_language varchar(3),
original_title varchar(50),
overview text,
popularity decimal,
poster_path varchar(50) ,
release_date date ,
title varchar(50) ,
video boolean,
vote_average decimal,
vote_count integer
)
"""

genre_cre_table = f"""
create table genre_ids (
meta_id integer,
genre_id integer,
constraint fk_meta_id
foreign key (meta_id)
references meta(id)
)
"""

db_tables = OrderedDict({
"meta":movies_cre_table,
"genre_ids":genre_cre_table
})









