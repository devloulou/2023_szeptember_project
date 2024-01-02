import os

class FileHandler:

    def __init__(self, meta):
        self.meta = meta
        self.movie_folder = meta['movie_folder']

    def get_movies_from_folder(self):
        return [item.split('.')[0] for item in os.listdir(self.movie_folder)]

    def write_meta_json(self, file_path, meta_data):
        import json

        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(meta_data, f, ensure_ascii=False, indent=4)

    def write_poster_image(self):
        ...

if __name__ == '__main__':
    from params import meta_params
    test = FileHandler(meta_params)

    print(test.get_movies_from_folder())

