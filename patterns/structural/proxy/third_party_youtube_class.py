from typing import List, Any
from .third_party_youtube_lib import ThirdPartyYouTubeLib


class ThirdPartyYouTubeClass(ThirdPartyYouTubeLib):
    def list_videos(self) -> List[Any]:
        pass  # send an API request to YouTube

    def get_video_info(self, id: int) -> Any:
        pass  # get video metadata

    def download_video(self, id: int) -> Any:
        pass  # download video from youtube
