# model.py
# Actor, Director, Genre, Movie

class Actor:
    def __init__(self, actor_full_name):
        self.colleague_list = []
        self.actor_full_name = actor_full_name

    def __repr__(self):
        if self.actor_full_name != "" and isinstance(self.actor_full_name, str):
            return "<Actor {}>".format(self.actor_full_name)
        else:
            return "<Actor None>"

    def __eq__(self, other):
        return self.actor_full_name == other.actor_full_name

    def __lt__(self, other):
        return self.actor_full_name < other.actor_full_name

    def __hash__(self):
        return hash(self.actor_full_name)

    def add_actor_colleague(self, colleague):
        self.colleague_list.append(colleague)

    def check_if_this_actor_worked_with(self, colleague):
        return colleague in self.colleague_list


class Director:
    def __init__(self, director):
        self.director_full_name = director

    def __repr__(self):
        if self.director_full_name != "":
            return "<Director {}>".format(self.director_full_name)
        else:
            return "<Director None>"

    def __eq__(self, other):
        return self.director_full_name == other.director_full_name

    def __lt__(self, other):
        return self.director_full_name < other.director_full_name

    def __hash__(self):
        return hash(self.director_full_name)


class Genre:
    def __init__(self, genre):
        self.genre_name = genre

    def __repr__(self):
        if self.genre_name != "":
            return "<Genre {}>".format(self.genre_name)
        else:
            return "<Genre None>"

    def __eq__(self, other):
        return self.genre_name == other.genre_name

    def __lt__(self, other):
        return self.genre_name < other.genre_name

    def __hash__(self):
        return hash(self.genre_name)


class Movie:
    def __init__(self, title, time):
        if time < 1900:
            raise ValueError("")
        self.title = title
        self.time = time
        self.runtime_minutes = 0
        self.actors = []
        self.genres = []
        self.description = ""
        self.director = ""

    def __repr__(self):
        return "<Movie {}, {}>".format(self.title, self.time)

    def __eq__(self, other):
        return self.title + str(self.time) == other.title + str(other.time)

    def __lt__(self, other):
        return self.title + str(self.time) < other.title + str(other.time)

    def __hash__(self):
        return hash(self.title + str(self.time))

    def add_actor(self, actor):
        self.actors.append(actor)

    def remove_actor(self, actor):
        if actor in self.actors:
            self.actors.remove(actor)

    def add_genre(self, genre):
        self.genres.append(genre)

    def remove_genre(self, genre):
        if genre in self.genres:
            self.genres.remove(genre)

    @property
    def runtime_minutes(self):
        return self.__runtime_minutes

    @runtime_minutes.setter
    def runtime_minutes(self, runtime_minutes):
        if runtime_minutes < 0:
            raise ValueError("")
        self.__runtime_minutes = runtime_minutes