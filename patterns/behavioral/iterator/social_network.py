from abc import ABC, abstractmethod

from patterns.behavioral.iterator.iterators.profile_iterator import ProfileIterator


class SocialNetwork(ABC):
    @abstractmethod
    def create_friends_iterator(self, profile_id: int) -> ProfileIterator:
        ...

    @abstractmethod
    def create_coworkers_iterator(self, profile_id: int) -> ProfileIterator:
        ...
