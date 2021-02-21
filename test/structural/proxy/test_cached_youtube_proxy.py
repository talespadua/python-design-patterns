import pytest
from unittest.mock import MagicMock
from typing import cast
from patterns.structural.proxy.cached_youtube_class import CachedYouTubeClass
from patterns.structural.proxy.third_party_youtube_lib import ThirdPartyYouTubeLib


class TestCachedYouTubeProxy:
    @pytest.fixture()
    def youtube_service(self) -> ThirdPartyYouTubeLib:
        mocked_service = MagicMock()
        mocked_service.list_videos = MagicMock(return_value=["video1", "video2"])
        return cast(ThirdPartyYouTubeLib, mocked_service)

    @pytest.fixture()
    def cached_youtube_proxy(
        self, youtube_service: ThirdPartyYouTubeLib
    ) -> CachedYouTubeClass:
        return CachedYouTubeClass(youtube_service)

    def test_cached_youtube_proxy(
        self,
        youtube_service: ThirdPartyYouTubeLib,
        cached_youtube_proxy: CachedYouTubeClass,
    ) -> None:
        cached_youtube_proxy.list_videos()
        cached_youtube_proxy.list_videos()

        youtube_service.list_videos.assert_called_once()  # type: ignore
