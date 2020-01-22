import pytest


def test_add_method(fixture_return_set):
    """
    Проверяет метод 'add' у типа структур данных: множество
    """
    fixture_return_set.add('hello')
    assert len(fixture_return_set) == 5


def test_copy_method(fixture_return_set):
    """
    Проверяет метод 'copy' у типа структур данных: множество
    """

    copied_set = fixture_return_set.copy()
    assert copied_set == fixture_return_set


@pytest.mark.parametrize("test_input", ['w', '3'])
def test_remove_method(fixture_return_set, test_input):
    """
    Проверяет метод 'remove' у типа структур данных: множество, с использованием параметризации
    """

    fixture_return_set.remove(test_input)
    print(fixture_return_set)
    assert len(fixture_return_set) == 3


def test_clear_method(fixture_return_set):
    """
    Проверяет метод 'clear' у типа структур данных: множество
    """

    fixture_return_set.clear()
    assert len(fixture_return_set) == 0


def test_update_method(fixture_return_set):
    """
    Проверяет метод 'update' у типа структур данных: множество
    """

    b = {'new', 'elements'}
    fixture_return_set.update(b)
    assert 'new' in fixture_return_set

