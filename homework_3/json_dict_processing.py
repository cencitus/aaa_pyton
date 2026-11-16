def extract_nested_value(obj: dict, keys: list[str]) -> object | None:
    """
    извлекает значение из вложенного словаря по списку ключей
    если путь не найден вернет None
    """
    for key in keys:
        if not isinstance(obj, dict):
            return None
        obj = obj.get(key)
    return obj


def process_dictionary_with_config(dictionary: dict, config: dict) -> dict:
    """
    обрабатывает словарь по конфигу
    извлекает нужные поля и при необходимости преобразует их типы
    возвращает новый словарь
    """
    result = {}
    for field_name, field_config in config.items():
        flag = 0

        if isinstance(field_config, tuple):
            field_config, type_ = field_config
            flag = 1
        value = extract_nested_value(dictionary, field_config)
        if value is not None and flag == 1:
            value = type_(value)
        result[field_name] = value
    return result


def process_list_of_dicts_with_config(
        list_of_dicts: list[dict],
        config: dict) -> list[dict]:
    """
    обрабатывает список словарей по конфигу
    возвращает список обработанных словарей
    """
    result = []
    for dictionary in list_of_dicts:
        dct = process_dictionary_with_config(dictionary, config)
        result.append(dct)
    return result


def create_processor(config: dict, list_processor: bool = False):
    """
    создат функцию обработки данных с заданным конфигом.
    в зависимости от list_processor выбирает обработку одного словаря
    или списка словарей
    """
    def processor(data):
        if list_processor:
            return process_list_of_dicts_with_config(data, config)
        else:
            return process_dictionary_with_config(data, config)
    return processor
