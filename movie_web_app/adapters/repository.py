# repository.py
import abc
from typing import List

from movie_web_app.domain.model import Actor, Director, Genre, Movie

repo_instance = None


class AbstractRepository(abc.ABC):

    @abc.abstractmethod
    def add_actor(self, actor: Actor):
        # Adds an actor to repository
        raise NotImplementedError

    @abc.abstractmethod
    def get_actor(self, actor_name) -> Actor:
        # Returns the Actor named actor_name from the repository.
        # If there is no Actor with the given username, this method returns None.
        raise NotImplementedError

    
