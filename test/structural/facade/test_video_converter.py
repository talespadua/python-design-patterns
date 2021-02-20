import pytest

from patterns.structural.facade.complex_subsystems import File
from patterns.structural.facade.video_converter import VideoConverter


class TestVideoConverter:
    @pytest.fixture()
    def video_converter(self) -> VideoConverter:
        return VideoConverter()

    def test_video_converter(self, video_converter: VideoConverter) -> None:
        converted_video = video_converter.convert("video.mp4", "ogg")
        assert isinstance(converted_video, File)
