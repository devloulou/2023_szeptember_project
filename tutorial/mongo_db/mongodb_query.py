"""

{title: "Aladdin"} - where title='Aladdin'

{title: {$nin: ["Aladdin"]}} - where title not in ('Aladdin')

{title: {$nin: ["Aladdin", "Alien"]}, vote_average: {$lt: 7}}
--> where title not in ('Aladdin', 'Alien') and vote_average < 7

{$or: [{title: "Aladdin"}, {vote_average: {$gt: 6}}]}
--> where title = 'Aladdin' or vote_average > 6

{color: {$exists: false}} - ha a color kulcs nincs benne a documentumokban

{"overview": /alien/} - where overview like "%alien%"

{$and: [{$or: [{color: {$exists: true}},{title: "Aliens"}]}, {price: {$eq: 5000}}]}

-- where (title="Aliens" or color="yellow") and price= 5000



"""


from pymongo import MongoClient

"""
CRUD műveletek - webes terminológia

Create - Insert - insert_one
Read -   select - find
Update - update - update_one, update_many, upsert
Delete - delete - delete_one, delete_many
"""

client = MongoClient("mongodb://localhost:27017")
database = client['test_db']
coll = database['meta']

data = [{"test": "valami"} for i in range(0, 100)]

# egyszerre 1 documentumot tesz a db-be
# coll.insert_one({"test": "valami"})

# bulk insert
# coll.insert_many(data)

# coll.delete_many({})


def time_it(func):
    def wrapper(*args, **kwargs):
        import time
        start_dt = time.time()
        result = func(*args, **kwargs)
        print(f"finished: {time.time() - start_dt} sec")
        return result
    return wrapper

@time_it
def insert_one_test():
    for item in [{"test": f"valami_{i}"} for i in range(0, 5000000)]:
        coll.insert_one(item)


@time_it
def insert_many_test():
    data = [{"test": f"{i}_{i}_valami_{i}"} for i in range(0, 5000000)]
    coll.insert_many(data)


@time_it
def insert_many_test2():
    data = [{f"test_{i}": f"{i}_valami_{i}"} for i in range(0, 5000000)]

    num_part = 3
    temp = [data[i * len(data) // num_part: (i + 1) * len(data) // num_part] for i in range(num_part)]
    
    for item in temp:        
        coll.insert_many(item)

@time_it
def my_func():
    my_data = coll.find({'test': {'$exists': True}})
    cnt = 0
    for idx, item in enumerate(my_data):
        cnt += 1

    print(cnt)

query = {'test': {'$exists': True}}
# update_one csak 1 documentumot fog módosítani, hiába több találat van
# coll.update_one(query, {"$set": {"color": "yellow"}})
# coll.update_many(query, {"$set": {"color": "yellow"}})

query = {'price': {'$exists': True}}
test_data = {
    "adult": False,
    "backdrop_path": "/AmR3JG1VQVxU8TfAvljUhfSFUOx.jpg",
    "genre_ids": [
        27,
        878
    ],
    "id": 348,
    "original_language": "en",
    "original_title": "Alien",
    "overview": "During its return to the earth, commercial spaceship Nostromo intercepts a distress signal from a distant planet. When a three-member team of the crew discovers a chamber containing thousands of eggs on the planet, a creature inside one of the eggs attacks an explorer. The entire crew is unaware of the impending nightmare set to descend upon them when the alien parasite planted inside its unfortunate host is birthed.",
    "popularity": 80.254,
    "poster_path": "/vfrQk5IPloGg1v9Rzbh2Eg3VGyM.jpg",
    "release_date": "1979-05-25",
    "title": "Alien",
    "video": False,
    "vote_average": 8.2,
    "vote_count": 13548
}
# coll.update_one(query, {"$set": test_data}, upsert=True)

from bson import ObjectId


@time_it
def my_func2():
    coll.delete_one({"_id": ObjectId("65a97728bb6cf76b425e9ec8")})

@time_it
def my_func3():
    coll.delete_one({"test": "27_27_valami_27"})

# 65a97728bb6cf76b425e9eb0



if __name__ == '__main__':
    # my_func()
    # insert_one_test()
    # insert_many_test()
    my_func3()
    print("****************************")
    my_func2()
    # my_func2()
    # insert_many_test2()