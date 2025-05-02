import random
import datetime
from faker import Faker
fake = Faker()

genres = [
    "Action",
    "Adventure",
    "Animation",
    "Biography",
    "Comedy",
    "Crime",
    "Documentary",
    "Drama",
    "Family",
    "Fantasy",
    "History",
    "Horror",
    "Music",
    "Musical",
    "Mystery",
    "Romance",
    "Sci-Fi",
    "Sport",
    "Thriller",
    "War",
    "Western"
]
class Video:
    def __init__(self, title, year, genre, view_count):
        self.title = title.title()[:-1]
        self.year = year
        self.genre = genre
        self.view_count = view_count

    def play(self, number_of_times=1):
        self.view_count += number_of_times

    __repr__ = lambda self: f"{self.title} ({self.year}) {self.genre} {self.view_count} views"

class Movie(Video):
    def __init__(self, title, year, genre, view_count):
        super().__init__(title, year, genre, view_count)

    __str__ = lambda self: f"{self.title} ({self.year})"


class Series(Video):
    def __init__(self, title, year, genre, view_count, seasons, episodes):
        super().__init__(title, year, genre, view_count)
        self.seasons = seasons
        self.episodes = episodes

    __str__ = lambda self: f"{self.title} S{self.seasons:02}E{self.episodes:02}"


def get_movies(libs):
    items = []
    for i in libs:
        if isinstance(i, Movie):
            items.append(i)
    return sorted(items, key=lambda x: x.title, reverse=False)


def get_series(libs):
    items = []
    for i in libs:
        if isinstance(i, Series):
            items.append(i)
    return sorted(items, key=lambda x: x.title, reverse=False)


def create_lib(movies=5, series=5):
    items = []
    for i in range(movies):
        item = Movie(fake.sentence(nb_words=random.randint(1, 4)), fake.year(), genres[random.randint(0, len(genres)-1)], random.randint(0, 100))
        items.append(item)

    for i in range(series):
        item = Series(
            fake.sentence(nb_words=random.randint(1, 5)),
            fake.year(),
            genres[random.randint(0, len(genres)-1)],
            random.randint(0, 100),
            random.randint(1, 10),
            random.randint(3, 20))
        items.append(item)

    return items

def generate_views(libs):
    nb = random.randint(0, len(libs) - 1)
    item = libs[nb]
    item.play(random.randint(1, 100))
    libs[nb] = item
    return libs

def generate_views_n_time(libs, n=100):
    for i in range(n):
        libs = generate_views(libs)
    return libs

def top_title(libs, nb=3):
    libs.sort(key=lambda x: x.view_count, reverse=True)
    return libs[:nb]

def print_list(libs, top_title):
    print("\n{}".format(top_title))
    for i in libs:
        print("\t{}".format(i))


if __name__ == "__main__":
    blockbuster_list = create_lib()
    print_list(generate_views(blockbuster_list), 'Biblioteka filmów i seriali:')
    print_list(top_title(blockbuster_list, 3), "Najpopularniejsze filmy i seriale dnia {}".format(datetime.datetime.now().strftime("%d.%m.%Y")))
