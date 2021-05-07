from __future__ import annotations

from unittest.mock import MagicMock

import pytest

from patterns.behavioral.iterator.facebook import Facebook
from patterns.behavioral.iterator.iterators.facebook_iterator import FacebookIterator
from patterns.behavioral.iterator.profile import Profile


class TestFacebookIterator:
    @pytest.fixture()
    def facebook_client(self) -> Facebook:
        facebook_client = Facebook()
        profile_list = [
            Profile(name="Foo", email="foo@gmail.com"),
            Profile(name="Bar", email="bar@gmail.com"),
        ]
        facebook_client.social_graph_request = MagicMock(  # type: ignore
            return_value=profile_list
        )

        return facebook_client

    @pytest.fixture()
    def facebook_iterator(self, facebook_client: Facebook) -> FacebookIterator:
        return FacebookIterator(facebook_client, 123, "friends")

    def test_iterate_all(self, facebook_iterator: FacebookIterator) -> None:
        total_elements = 0
        while facebook_iterator.has_more():
            facebook_iterator.get_next()
            total_elements += 1

        assert total_elements == 2
