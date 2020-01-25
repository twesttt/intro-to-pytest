import pytest


def test_update_method(fixture_return_dictionary):
    """Проверяет метод 'update' у типа структур данных: словарь """

    fixture_return_dictionary.update({'Tanya': 4})
    assert len(fixture_return_dictionary) == 4


def test_get_method(fixture_return_dictionary):
    """Проверяет метод 'get' у типа структур данных: словарь """

    assert fixture_return_dictionary.get('Misha') == 5


@pytest.mark.parametrize("test_input", ['Misha', 'Gena'])
def test_pop_method(fixture_return_dictionary, test_input):
    """Проверяет метод 'pop' у типа структур данных: словарь, с использованием параметризации """

    fixture_return_dictionary.pop(test_input)
    assert len(fixture_return_dictionary) == 2


def test_clear_method(fixture_return_dictionary):
    """ Проверяет метод 'clear' у типа структур данных: словарь """

    fixture_return_dictionary.clear()
    assert len(fixture_return_dictionary) == 0


def test_copy_method(fixture_return_dictionary):
    """Проверяет метод 'copy' у типа структур данных: словарь """

    copied_dict = fixture_return_dictionary.copy()
    assert copied_dict == fixture_return_dictionary
