import pytest


def test_count_method(fixture_return_string):
    """
    Проверяет метод 'count' у строковых данных
    """
    assert fixture_return_string.count('l') == 3


def test_find_method(fixture_return_string):
    """
    Проверяет метод 'find' у строковых данных
    """
    assert fixture_return_string.find('h') == 0


@pytest.mark.parametrize("test_input", ['my', 'hey'])
def test_replace_method(fixture_return_string, test_input):
    """
    Проверяет метод 'replace' у строковых данных c помощью параметризации
    """

    a = test_input.format()
    txt = fixture_return_string.replace("hello", a)
    assert txt.find(test_input) == 0


def test_split_method(fixture_return_string):
    """
    Проверяет метод 'split' у строковых данных
    """

    new_list = fixture_return_string.split(' ')
    assert len(new_list) == 2


def test_title_method(fixture_return_string):
    """
     Проверяет метод преобразования первых букв слов в заглавные
    """

    converted_text = fixture_return_string.title()
    assert converted_text == 'Hello World'
