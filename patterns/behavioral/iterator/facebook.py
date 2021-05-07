from __future__ import annotations

from typing import Any

import patterns.behavioral.iterator.iterators.facebook_iterator as fi
from patterns.behavioral.iterator.iterators.profile_iterator import ProfileIterator
from patterns.behavioral.iterator.social_network import SocialNetwork


class Facebook(SocialNetwork):
    def create_friends_iterator(self, profile_id: int) -> ProfileIterator:
        return fi.FacebookIterator(self, profile_id, "friends")

    def create_coworkers_iterator(self, profile_id: int) -> ProfileIterator:
        return fi.FacebookIterator(self, profile_id, "coworkers")

    def social_graph_request(self, profile_id: int, profile_type: str) -> Any:
        # should fetch profiles based on the type
        return []
