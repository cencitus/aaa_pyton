import statistics


def calculate_stats(values: list[int]) -> dict:
    """
    считает основные статистики по списку чисел
    """
    result = {}
    result['count'] = len(values)
    result['mean'] = statistics.mean(values)
    result['median'] = statistics.median(values)
    result['max'] = max(values)
    return result
