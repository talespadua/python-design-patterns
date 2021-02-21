from abc import ABC, abstractmethod
from typing import List, Any


class ThirdPartyYouTubeLib(ABC):
    @abstractmethod
    def list_videos(self) -> List[Any]:
        ...

    @abstractmethod
    def get_video_info(self, id: int) -> Any:
        ...

    @abstractmethod
    def download_video(self, id: int) -> Any:
        ...
