from .datasource_decorator import DataSourceDecorator


class EncryptionDecorator(DataSourceDecorator):
    def _encrypt_data(self, data: str) -> str:
        return data + "123456"  # encrypt data

    def _decrypt_data(self, encrypted_data: str) -> str:
        return encrypted_data.rstrip("123456")  # decrypt data

    def write_data(self, data: str) -> None:
        data = self._encrypt_data(data)
        self._wrappee.write_data(data)

    def read_data(self, data: str) -> None:
        data = self._decrypt_data(data)
        self._wrappee.read_data(data)
