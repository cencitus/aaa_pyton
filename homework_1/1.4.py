def main():
    days = [
        {"day": "пн", "orders": 20, "revenue": 40_000, "returns": 2},
        {"day": "вт", "orders": 16, "revenue": 19_200, "returns": 4},
        {"day": "ср", "orders": 25, "revenue": 55_000, "returns": 1},
        {"day": "чт", "orders": 10, "revenue": 12_000, "returns": 3},
        {"day": "пт", "orders": 30, "revenue": 48_000, "returns": 3},
    ]

    # - выручку за всю неделю
    revenue = sum(day['revenue'] for day in days)
    print(f'выручка за неделю {revenue}')

    # - день с самой большой выручкой
    max_revenue = max(day['revenue'] for day in days)
    day_with_max = [day['day'] for day in days if day['revenue'] == max_revenue]
    print('день с максимальной выручкой:', ''.join(day_with_max))

    # - среднюю выручку на один заказ в каждый день
    avg_rev_per_day = {day['day']: (day['revenue'] / day['orders']) for day in days}
    print(avg_rev_per_day)

    # - дни, где возвратов больше 20% заказов
    days_top_returns = [day['day'] for day in days if day['returns'] > day['orders'] * 0.2]
    print(days_top_returns)


if __name__ == '__main__':
    main()
