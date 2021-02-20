from typing import Any

"""
These are all made up interaction between complex subsystems for video conversion, with
code made for it pass on mypy and flake8 without having to ignore all sorts of errors
"""


class VideoFile:
    def __init__(self, filename: str) -> None:
        self.codec: str = "ogg"


class File:
    def __init__(self, result: Any):
        pass


class Codec:
    pass


class OggCompressionCodec(Codec):
    pass


class MPEG4CompressionCodec(Codec):
    pass


class CodecFactory:
    @staticmethod
    def extract(file: VideoFile) -> Codec:
        if file.codec == "mp4":
            return MPEG4CompressionCodec()
        if file.codec == "ogg":
            return OggCompressionCodec()
        raise KeyError


class BiterateReader:
    @staticmethod
    def read(filename: str, source_codec: Codec) -> str:
        return ""

    @staticmethod
    def convert(buffer: str, destination_codec: Codec) -> str:
        return ""


class AudioMixer:
    @staticmethod
    def fix(byte_stream: str) -> str:
        return byte_stream
