def main():
    queries = [
        "чехол",
        "iphone",
        "чехол",
        "наушники",
        "iphone",
        "iphone",
        "кабель",
        "чехол",
        "iphone",
        ]
    queries_amount = len(queries)
    print(f'Всего запросов: {queries_amount}')

    query_counts = {}
    maximum = 0
    for query in queries:
        query_counts[query] = query_counts.get(query, 0) + 1
        if query_counts[query] > maximum:
            maximum_key = query
            maximum = query_counts[query]

    print('сколько раз ввели каждый запрос', query_counts)
    print('самый частый запрос - ', maximum_key)
    print(f'доля самого популярного запроса {maximum / queries_amount * 100:.2f}%')

    one_time_query = []
    for query, value in query_counts.items():
        if value == 1:
            one_time_query.append(query)
    print('встретились один раз - ', one_time_query)


if __name__ == '__main__':
    main()
