from __future__ import annotations

from typing import Optional, List

import patterns.behavioral.iterator.facebook as fb
from patterns.behavioral.iterator.iterators.profile_iterator import ProfileIterator
from patterns.behavioral.iterator.profile import Profile


class FacebookIterator(ProfileIterator):
    def __init__(self, facebook: fb.Facebook, profile_id: int, search_type: str):
        self.facebook = facebook
        self.profile_id = profile_id
        self.search_type = search_type

        self.cache: List[Profile] = []
        self.current_position = 0

    def lazy_init(self) -> None:
        if not self.cache:
            self.cache = self.facebook.social_graph_request(
                self.profile_id, self.search_type
            )

    def get_next(self) -> Optional[Profile]:
        if self.has_more():
            element = self.cache[self.current_position]
            self.current_position += 1
            return element
        return None

    def has_more(self) -> bool:
        self.lazy_init()
        return self.current_position < len(self.cache)
