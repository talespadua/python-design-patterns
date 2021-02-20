from .datasource_decorator import DataSourceDecorator


class CompressionDecorator(DataSourceDecorator):
    def _compress_data(self, data: str) -> str:
        return data  # compress data

    def _decompress_data(self, compressed_data: str) -> str:
        return compressed_data  # decompress data

    def write_data(self, data: str) -> None:
        data = self._compress_data(data)
        self._wrappee.write_data(data)

    def read_data(self, data: str) -> None:
        data = self._decompress_data(data)
        self._wrappee.read_data(data)
