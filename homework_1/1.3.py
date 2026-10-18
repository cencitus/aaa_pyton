def main():
    orders = [
        {"id": 1, "buyer": "anya", "status": "delivered", "amount": 900},
        {"id": 2, "buyer": "boris", "status": "returned", "amount": 4_500},
        {"id": 3, "buyer": "anya", "status": "delivered", "amount": 1_500},
        {"id": 4, "buyer": "vera", "status": "delivered", "amount": 3_200},
        {"id": 5, "buyer": "boris", "status": "delivered", "amount": 700},
        {"id": 6, "buyer": "gleb", "status": "returned", "amount": 2_100}
    ]

    # - на какую сумму оформили возвраты
    returned_amount = sum(order['amount'] for order in orders if order['status'] == 'returned')
    print(f'сумма возвратов: {returned_amount}')

    # - кто хотя бы раз вернул зака
    person_who_return = {order['buyer'] for order in orders if order['status'] == 'returned'}
    print(f'хотя бы раз вернули заказ: {person_who_return}')

    # - сколько заказов доставлено покупателю
    delivered_count = sum(1 for order in orders if order['status'] == 'delivered')
    print(f'заказов доставлено: {delivered_count}')

    # - средний чек доставленных заказов
    delivered_sum = sum(order['amount'] for order in orders if order['status'] == 'delivered')
    print(f'средний чек доставленных заказов: {delivered_sum / delivered_count}')


if __name__ == '__main__':
    main()
