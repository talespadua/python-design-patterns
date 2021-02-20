import pytest

from patterns.structural.decorator.datasources.abstract_datasource import DataSource
from patterns.structural.decorator.datasources.decorators.encryption_decorator import (
    EncryptionDecorator,
)


class TestEncryptionDecorator:
    @pytest.fixture()
    def datasource(self) -> DataSource:
        class MemoryDataSource(DataSource):
            def __init__(self) -> None:
                self._data: str = ""

            def write_data(self, data: str) -> None:
                self._data = data

            def read_data(self) -> str:
                return self._data

        return MemoryDataSource()

    @pytest.fixture()
    def encryption_decorator(self, datasource: DataSource) -> EncryptionDecorator:
        return EncryptionDecorator(datasource)

    def test_encryption_decorator(
        self, encryption_decorator: EncryptionDecorator, datasource: DataSource
    ) -> None:
        data = "abc"
        encryption_decorator.write_data(data)
        assert datasource.read_data() == "abc123456"

        assert encryption_decorator.read_data() == "abc"
