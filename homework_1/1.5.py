from itertools import groupby


def main():
    reviews = [
        {"id": 1, "product": "Чехол", "stars": 5},
        {"id": 1, "product": "Чехол", "stars": 3},
        {"id": 1, "product": "Чехол", "stars": 4},
        {"id": 2, "product": "Наушники", "stars": 2},
        {"id": 2, "product": "наушники", "stars": 2},
        {"id": 2, "product": "НАУШНИКИ", "stars": 5},
        {"id": 3, "product": "Планшет", "stars": 5},
        {"id": 4, "product": "Колонка", "stars": 4},
        {"id": 4, "product": "Колонка", "stars": 4},
        {"id": 5, "product": "Кабель", "stars": 1},
    ]

    for review in reviews:
        review['product'] = review['product'].lower().capitalize()

    avg_per_product = {}
    min_avg = None
    for product_id, review in groupby(reviews, key=lambda review: review['id']):
        product_reviews = list(review)
        total_stars = sum(product_review['stars'] for product_review in product_reviews)
        reviw_count = len(product_reviews)
        product_name = product_reviews[0]['product']
        avg_review = total_stars / reviw_count
        avg_per_product[product_name] = avg_review
        if reviw_count >= 2:
            if min_avg is None or avg_review < min_avg:
                min_avg = avg_review
                min_rev_name = product_name
    print(f'средняя оценка каждого товара {avg_per_product}')
    print('худший товар по средней оценке среди тех, у кого хотя бы два отзыва:', min_rev_name)
    one_two_stars = sum(1 for review in reviews if review['stars'] <= 2)
    print('колво отзывов 1 или 2 звезды: ', one_two_stars)
    print('доля 1-2 звезды от всех: ', one_two_stars / len(reviews))


if __name__ == '__main__':
    main()
