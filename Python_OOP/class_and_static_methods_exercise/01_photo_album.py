from math import ceil


class PhotoAlbum:

    def __init__(self, pages: int):
        self.pages = pages
        self.photos = [[] for _ in range(self.pages)]

    @classmethod
    def from_photos_count(cls, photos_count: int):
        return cls(ceil(photos_count / 4))

    def add_photo(self, label: str):
        for i, page in enumerate(self.photos, start=1):
            if len(page) < 4:
                page.append(label)
                return f'{label} photo added successfully on page {i} slot {len(page)}'
        return 'No more free slots'

    def display(self):
        separation = "-" * 11
        result = []
        for page in self.photos:
            result.append(separation)
            result.append(" ".join(['[]' for _ in page]))

        result.append(separation)
        return '\n'.join(result)

