from entity.shop import Shop
from entity.store import Store
from entity.request import Request
from exceptions import RequestError, LogisticError

store = Store(
    items={
        "печенька": 25,
        "собачка": 25,
        "елка": 25,
        "пончик": 3,
        "зонт": 5,
        "ноутбук": 1,
    },
)

shop = Shop(
    items={
        "печенька": 2,
        "собачка": 2,
        "елка": 2,
        "зонт": 1,
        "пончик": 1,
    },
)

storages = {
    "магазин": shop,
    "склад": store,
}


def main():
    print('\nДобрый день!\n')

    while True:

        for storage_name in storages:
            print(f'Сейчас в {storage_name}:\n {storages[storage_name].get_items()}')

        user_input = input(
            'Введите запрос в формате "Доставить 2 печеньки из склада в магазин"\n'
            'Введите "стоп" или "stop", если хотите закончить:\n'
        )
        if user_input in ('стоп', 'stop'):
            break

        try:
            request = Request(request=user_input, storages=storages)
        except RequestError as error:
            print(error.message)
            continue

        try:
            storages[request.departure].remove(request.product, request.amount)
            print(f'Курьер забрал {request.amount} {request.product} из {request.departure}')
        except LogisticError as error:
            print(error.message)
            continue

        try:
            storages[request.destination].add(request.product, request.amount)
            print(f'Курьер доставил {request.amount} {request.product} в {request.destination}')
        except LogisticError as error:
            print(error.message)
            storages[request.departure].add(request.product, request.amount)
            print(f'Курьер вернул {request.amount} {request.product} в {request.departure}')
            continue


if __name__ == '__main__':
    main()
