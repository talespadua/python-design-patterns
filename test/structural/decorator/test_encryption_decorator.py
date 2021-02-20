from typing import cast

import pytest
from unittest.mock import MagicMock

from patterns.structural.decorator.datasources.abstract_datasource import DataSource
from patterns.structural.decorator.datasources.decorators.encryption_decorator import (
    EncryptionDecorator,
)


class TestEncryptionDecorator:
    @pytest.fixture()
    def datasource(self) -> DataSource:
        datasource = MagicMock()
        datasource.read_data = MagicMock()
        datasource.write_data = MagicMock()
        return cast(DataSource, datasource)

    @pytest.fixture()
    def encryption_decorator(self, datasource: DataSource) -> EncryptionDecorator:
        return EncryptionDecorator(datasource)

    def test_encryption_decorator_reads_data(
        self, encryption_decorator: EncryptionDecorator, datasource: DataSource
    ) -> None:
        encrypted_data = "abc123456"
        encryption_decorator.read_data(encrypted_data)
        datasource.read_data.assert_called_with("abc")  # type: ignore

    def test_encryption_write_data(
        self, encryption_decorator: EncryptionDecorator, datasource: DataSource
    ) -> None:
        decrypted_data = "abc"
        encryption_decorator.write_data(decrypted_data)
        datasource.write_data.assert_called_with("abc123456")  # type: ignore
