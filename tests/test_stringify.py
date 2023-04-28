import os

import pytest

from stringify.stringify import stringify

# Вернуть полный путь к файлу в директории fixtures
def get_fixture_path(file_name):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(current_dir, 'fixtures', file_name)

# Прочитать файл по указанному пути
def read(file_path):
    with open(file_path, 'r') as f:
        result = f.read()
    return result

# Создаем несколько тестовых значений примитивных типов данных для проверки функции stringify()
primitives = {
    "string": "value",
    "boolean": True,
    "number": 5,
}

# Создаем сложную вложенную структуру данных для проверки функции stringify()
nested = {
    "string": "value",
    "boolean": True,
    "number": 5,
    "dict": {
        5: "number",
        None: "None",
        True: "boolean",
        "value": "string",
        "nested": {
            "boolean": True,
            "string": 'value',
            "number": 5,
            None: "None",
        },
    },
}

# Создаем список тестовых случаев для проверки функции stringify()
# Каждый случай содержит три параметра: заменитель (replacer), количество пробелов (spases_count) и индекс 
# соответствующей строки в файлах plain.txt и nested.txt
cases = [
    ('|-', 1, 0),  # первый уровень вложенности, 1 пробел
    ('|-', 2, 1),  # второй уровень вложенности, 2 пробела
    (' ', 3, 2),   # третий уровень вложенности, 3 пробела
]

# Тест функции stringify() на примитивных типах данных
# Проверяем, что функция правильно преобразует строку, логическое значение и число в строку
@pytest.mark.parametrize("value", primitives.values())
def test_primitives(value):
    assert stringify(value) == str(value)

plain_data = read(get_fixture_path('plain.txt')).rstrip().split('\n\n\n')
nested_data = read(get_fixture_path('nested.txt')).rstrip().split('\n\n\n')

# Тест функции stringify() на сложной вложенной структуре данных
# Проверяем, что функция правильно преобразует словарь с вложенными словарями и списками в строку с заданным 
# количеством пробелов и заменителями
@pytest.mark.parametrize("replacer,spases_count,case_index", cases)
def test_plain(replacer, spases_count, case_index):
    expected = nested_data[case_index]
    assert stringify(nested, replacer, spases_count) == expected

# Тест функции stringify() на примитивных типах данных
# Проверяем, что функция правильно преобразует словарь с примитивными типами данных в строку с заданным 
# количеством пробелов и заменителями
@pytest.mark.parametrize("replacer,spases_count,case_index", cases)
def test_nested(replacer, spases_count, case_index):
    expected = plain_data[case_index]
    assert stringify(primitives, replacer, spases_count) == expected


def test_default_values():
    assert stringify(primitives) == plain_data[3]
    assert stringify(primitives, ' ') == plain_data[3]
    assert stringify(primitives, '...') == plain_data[4]
    assert stringify(nested) == nested_data[3]
    assert stringify(nested, ' ') == nested_data[3]
    assert stringify(nested, '...') == nested_data[4]
