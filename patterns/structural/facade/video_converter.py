from .complex_subsystems import (
    MPEG4CompressionCodec,
    CodecFactory,
    VideoFile,
    OggCompressionCodec,
    BiterateReader,
    AudioMixer,
    File,
    Codec,
)


class VideoConverter:
    def convert(self, filename: str, file_format: str) -> File:
        file = VideoFile(filename)
        source_codec = CodecFactory.extract(file)

        if file_format == "mp4":
            destination_codec: Codec = MPEG4CompressionCodec()
        else:
            destination_codec = OggCompressionCodec()

        buffer = BiterateReader.read(filename, source_codec)
        result = BiterateReader.convert(buffer, destination_codec)
        result = AudioMixer.fix(result)
        return File(result)
