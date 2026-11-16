def split_laureates(
        laureates_data: list[dict]) -> tuple[list[dict], list[dict]]:
    """
    разделяет лауреатов на людей и организации
    """
    persons = []
    orgs = []
    for laureate in laureates_data:
        if laureate['type_'] == 'person':
            persons.append(laureate)
        else:
            orgs.append(laureate)
    return persons, orgs


def calculate_missing(
        persons: list[dict]) -> tuple[dict[str, int], dict[str, float]]:
    """
    считает количество и долю пропусков по каждому полю
    """
    missings = {}
    for person in persons:
        for key, value in person.items():
            missings[key] = missings.get(key, 0)
            if value is None:
                missings[key] += 1
    missing_share = {}
    for key, value in missings.items():
        missing_share[key] = round(value / len(persons) * 100, 2)
    return missings, missing_share


def find_laureate_by_id(
        laureates_data: list[dict], id_value: int) -> dict | None:
    """
    ищет лауреата по ID
    возвращает словарь лауреата или None, если ID не найден
    """
    for laureate in laureates_data:
        if int(laureate['id']) == id_value:
            return laureate
    return None


def get_ids_info(
        laureates_data: list[dict]) -> tuple[list[int], int]:
    """
    собирает ID лауреатов и считает количество повторов
    """
    ids = []
    ids_uniq = set()
    for laureate in laureates_data:
        ids.append(int(laureate['id']))
        ids_uniq.add(int(laureate['id']))
    duplicates = len(ids) - len(ids_uniq)
    return ids, duplicates


def find_id_gaps(ids: list[int]) -> list[tuple[int, int]]:
    """
    находит пары соседних ID с разницей больше единицы
    """
    ids_sorted = sorted(ids)
    gaps = []
    for i in range(len(ids_sorted) - 1):
        if ids_sorted[i + 1] - ids_sorted[i] > 1:
            gaps.append((ids_sorted[i], ids_sorted[i + 1]))
    return gaps


def group_by_attributes(
        data: list[dict],
        attributes: list[str]) -> dict[tuple, list[dict]]:
    """
    группирует словари по указанным полям
    """
    result = {}
    for row in data:
        key = []
        for attribute in attributes:
            key.append(row[attribute])

        key = tuple(key)
        if key not in result:
            result[key] = []
        result[key].append(row)
    return result
