import os

class FileHandler:

    def __init__(self, meta):
        self.meta = meta
        self.movie_folder = self.meta['movie_folder']
        self.web_server = self.meta['image_web_path']

    def get_movies_from_folder(self, folder_path):
        return [item.split('.')[0] for item in os.listdir(folder_path)]

    def write_meta_json(self, file_path, meta_data):
        import json

        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(meta_data, f, ensure_ascii=False, indent=4)

    def write_poster_image(self, image_path, poster_path):
        from urllib.request import urlopen
    
        link = f"{self.web_server}{poster_path}"
        image = urlopen(link).read()

        with open(image_path, "wb") as poster:
            poster.write(image)

    def remove_file(self, file_path):
        os.remove(file_path)


if __name__ == '__main__':
    from params import meta_params
    test = FileHandler(meta_params)

    print(test.get_movies_from_folder())

