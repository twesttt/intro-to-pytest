import pytest


def test_append_method(fixture_return_list_of_numbers):
    """
    Проверяет метод 'append' у типа структур данных: список
    """

    fixture_return_list_of_numbers.append(20)
    assert len(fixture_return_list_of_numbers) == 5


def test_extend_method(fixture_return_list_of_numbers):
    """
    Проверяет метод 'extend' у типа структур данных: список
    """
    fixture_return_list_of_numbers.extend([8, 9, 10])
    assert len(fixture_return_list_of_numbers) == 7


@pytest.mark.parametrize("test_input", [[6, 4, 2], [8, 4, 2]])
def test_sort_method(test_input):
    """
    Проверяет метод 'sort' у типа структур данных: список, с использованием параметризации
    """
    test_input.sort()
    print(test_input)
    assert test_input.index(2) == 0


def test_count_method(fixture_return_list_of_numbers):
    """
    Проверяет метод 'count' у типа структур данных: список
    """
    assert fixture_return_list_of_numbers.count(4) == 2


def test_pop_method(fixture_return_list_of_numbers):
    """
    Проверяет метод 'pop' у типа структур данных: список
    """
    assert fixture_return_list_of_numbers.pop() == 4


