from typing import List, Any

from .third_party_youtube_lib import ThirdPartyYouTubeLib


class CachedYouTubeClass(ThirdPartyYouTubeLib):
    def __init__(self, service: ThirdPartyYouTubeLib):
        self.service = service
        self.video_cache: List[Any] = []
        self.list_cache: List[Any] = []
        self.need_reset = False

    def list_videos(self) -> List[Any]:
        if not self.list_cache or self.need_reset:
            self.list_cache = self.service.list_videos()
        return self.list_cache

    def get_video_info(self, video_id: int) -> Any:
        if not self.video_cache or self.need_reset:
            self.video_cache = self.service.get_video_info(video_id)
        return self.video_cache

    def download_video(self, video_id: int) -> None:
        self.download_video(video_id)
