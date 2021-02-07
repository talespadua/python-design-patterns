from patterns.creational.singleton.singleton import Database


def test_singleton() -> None:
    database = Database()
    new_database = Database()

    assert id(database) == id(new_database)
