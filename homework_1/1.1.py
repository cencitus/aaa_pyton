def main():
    moscow = {201, 202, 203, 204}
    kazan = {203, 204, 205, 206}

    print('что можно забрать в любом из двух городов')
    in_both = moscow & kazan
    print(in_both)

    print('что есть только в Москве')
    only_msk = moscow - kazan
    print(only_msk)

    print('что есть только в Казани')
    only_kzn = kazan - moscow
    print(only_kzn)

    print('сколько разных товаров на обоих складах вместе')
    in_both_different = moscow | kazan
    print(len(in_both_different))


if __name__ == '__main__':
    main()
