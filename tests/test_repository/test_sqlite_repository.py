import logging

from bookkeeper.models.category import Category
from bookkeeper.repository.sqlite_repository import SQLiteRepository
from dataclasses import dataclass
import pytest

DB_NAME = 'test.db'


@pytest.fixture
def custom_class():
    @dataclass
    class Custom:
        pk: int = 0
        test_field: str = 'abc'

    return Custom


@pytest.fixture
def repo(custom_class):
    return SQLiteRepository(DB_NAME, custom_class)


def test_add_get_and_delete(repo, custom_class):
    obj = custom_class()
    pk = repo.add(obj)
    o = repo.get(5555)
    assert obj.pk == pk
    assert repo.get(pk) == obj
    assert o is None
    repo.delete(pk)
    assert repo.get(pk) is None


def test_update(repo, custom_class):
    obj = custom_class
    pk = repo.add(obj)
    o = repo.get(pk)
    o.test_field = 'def'
    repo.update(o)
    assert repo.get(pk) == o


# def test_getall(repo, custom_class):
#     obj = custom_class
#     pk = repo.add(obj)
#     assert repo.get_all({'test_field': 'abc'})[0].test_field == 'abc'
