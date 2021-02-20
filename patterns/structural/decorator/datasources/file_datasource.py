from .abstract_datasource import DataSource


class FileDataSource(DataSource):
    def write_data(self, data: str) -> None:
        pass  # write data to file

    def read_data(self, data: str) -> None:
        pass  # read_data_from_file
