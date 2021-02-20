from patterns.structural.decorator.datasources.abstract_datasource import DataSource


class DataSourceDecorator(DataSource):
    def __init__(self, source: DataSource):
        self._wrappee = source

    def write_data(self, data: str) -> None:
        self._wrappee.write_data(data)

    def read_data(self, data: str) -> None:
        self._wrappee.read_data(data)
